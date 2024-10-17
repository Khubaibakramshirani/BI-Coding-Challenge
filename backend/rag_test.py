# # rag.py
# from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration
# import torch

# class RAGModel:
#     def __init__(self):
#         # Initialize the RAG model components
#         self.tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
#         self.retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="exact", use_dummy_dataset=True)
#         self.model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")
    
#     def get_answer(self, question: str) -> str:
#         # Tokenize input
#         input_ids = self.tokenizer(question, return_tensors="pt").input_ids
#         # Generate answer
#         with torch.no_grad():
#             generated_ids = self.model.generate(input_ids, num_beams=2, min_length=1, max_length=50)
#         answer = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
#         return answer
