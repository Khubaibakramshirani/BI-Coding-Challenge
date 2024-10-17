# main.py
from fastapi import FastAPI
from backend.routers import rag
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


# Add CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the RAG router
app.include_router(rag.router_fast_api, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
