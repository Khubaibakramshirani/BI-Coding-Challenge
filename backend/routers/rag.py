#backend/routers/rag.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.storage import InMemoryByteStore
from langchain_chroma import Chroma
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
import uuid

# Initialize the FastAPI APIRouter
router_fast_api = APIRouter()

# Load .env file and set API keys
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize language model
llm = ChatOpenAI(model="gpt-4o-mini")  # Make sure the model is available for your use

# # # Dataset paths
# sustainability_data_path = "/home/sparlay/Coding/JB/backend/data/Dataset 1 (Sustainability Research Results).xlsx"
# christmas_data_path = "/home/sparlay/Coding/JB/backend/data/Dataset 2 (Christmas Research Results).xlsx"

#Updated dataset paths using relative paths from the current working directory
sustainability_data_path = "backend/data/Dataset 1 (Sustainability Research Results).xlsx"
christmas_data_path = "backend/data/Dataset 2 (Christmas Research Results).xlsx"

# Load the datasets using absolute paths
sustainability_loader = UnstructuredExcelLoader(sustainability_data_path)
sustainability_docs = sustainability_loader.load_and_split()

christmas_loader = UnstructuredExcelLoader(christmas_data_path)
christmas_docs = christmas_loader.load_and_split()

# Combine both datasets into one list of documents
docs = sustainability_docs + christmas_docs

# Set up vector store and byte store for retriever
vectorstore = Chroma(collection_name="summaries", embedding_function=OpenAIEmbeddings())
store = InMemoryByteStore()
id_key = "doc_id"

# Summarization chain setup
chain = (
    {"doc": lambda x: x.page_content}
    | ChatPromptTemplate.from_template("Summarize the following document:\n\n{doc}")
    | llm
    | StrOutputParser()
)

# Summarize all the documents
summaries = chain.batch(docs, {"max_concurrency": 1})

# Generate unique document IDs
doc_ids = [str(uuid.uuid4()) for _ in docs]

# Create Document objects for the summaries
summary_docs = [
    Document(page_content=s, metadata={id_key: doc_ids[i]})
    for i, s in enumerate(summaries)
]

# Add summarized documents to retriever
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,
)

# Add documents to the vector store and memory
retriever.vectorstore.add_documents(summary_docs)
retriever.docstore.mset(list(zip(doc_ids, docs)))

# Define RAG chain with context formatting and querying
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Pydantic model for the request
class QueryRequest(BaseModel):
    question: str

# Process query function with the router
import time

@router_fast_api.post("/query")
async def process_query(request: QueryRequest):
    try:
        start_time = time.time()

        # Retrieve documents related to the question
        retrieved_docs = retriever.vectorstore.similarity_search(request.question)
        retrieval_time = time.time()
        print(f"Document retrieval took: {retrieval_time - start_time} seconds")

        # Format the retrieved documents for the RAG chain
        formatted_docs = format_docs(retrieved_docs)

        # Set up the input dictionary for the chain
        input_dict = {"context": formatted_docs, "question": request.question}

        # Create a prompt and pass it to the language model
        chain = (
            {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        # Get the answer from the RAG chain
        result = chain.invoke(input_dict)
        end_time = time.time()
        print(f"Total processing time: {end_time - start_time} seconds")

        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

