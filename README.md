
# BI Coding Challenge

This repository contains the implementation of a RAG (Retrieval-Augmented Generation) system using FastAPI for backend development and React with TypeScript for the frontend. The project allows users to ask questions and get responses from a RAG-based system.

# Project Structure

   ```markdown
      BI/
      |----backend/
      |    |----routers/
      |        |----rag.py
      |    |----main.py
      |    |----data/
      |        |----Dataset 1 (Sustainability Research Results).xlsx
      |        |----Dataset 2 (Christmas Research Results).xlsx
      |        |----faiss_document_store.db
      |    |----web/
      |        |----static
      |        |-- more files related to frontend build
      |----frontend/
      |    |----src/
      |        |----components/
      |            |----QueryForm.tsx
      |            |----ResultsDisplay.tsx
      |        |----services/
      |            |----api.ts
      |        |----App.tsx
      |        |----App.css
      |        |----index.tsx
      |        |----index.css
      |        |----constants.ts
      |    |----public/
      |    |----package.json
      |    |----tsconfig.json
      |----README.md
      |----requirements.txt
      |----build.sh
   ```

## Installation and Setup

### Prerequisites
- Python 3.8+
- fastapi==0.115.2
- npm or yarn
- Virtual Environment (venv)

### Setup Locally

1. Clone the respository:

   ```bash
   git clone https://github.com/Khubaibakramshirani/BI-Coding-Challenge.git
   cd BI-Coding-Challenge/backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   OR you could run build.sh file - this will install the requirements as well build frontend files
   ```bash
   ./build.sh
   ```
   
4. Create .venv file for enviornment variable in backend folder
   ```markdown
      OPENAI_API_KEY="Your OPENAI API KEY Here"
      PORT=8000
   ```
5. Update the BASE_API_URL for local running the backend and as well as frontend.
   ```markdown
   export const BASE_API_URL = 'http://127.0.0.1:8000/api'
   ```
   
6. Update the dataset path in the backend/routers/rag.py file
   ```bash
   sustainability_data_path = "backend/data/Dataset 1 (Sustainability Research Results).xlsx"
   christmas_data_path = "backend/data/Dataset 2 (Christmas Research Results).xlsx"
   ```
   
7. Run the FastAPI server in the root directory where you cloned the repo:
   ```bash
   uvicorn backend.main:app --reload
   ```
   
8. The frontend will be available at `http://localhost:3000` and will communicate with the backend running at `http://127.0.0.1:8000`.

### Setup on Render
1. Create a Web Service on the https://dashboard.render.com/
2. Setting
   ```markdown
      General:
         |--Name: Write custom Name
         |--Region: Select Nearest Region
         |--Instance Type: Free
      Build and Deploy:
         |--Repository: https://github.com/Khubaibakramshirani/BI-Coding-Challenge
         |--Branch: "main" or "render"
         |--Root Directory: 
         |--Build Command: pip install -r requirements.txt
         |--Start Command: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
   ```
   
3. Environment Variable - Create two 
```markdown
   |--Create OPENAI_API_KEY variable with your openAI api key
   |--Create PORT=8000
```

4. Deploy Latest Commit. 
5. Wait for it to start then go to your deployed URL

## Usage

1. Navigate to `http://localhost:8000` in your browser for local deployed
2. For Live deployed on Render go to your deployed URL given by Render. If my web service name on Render is "BI-coding-challenge" then my deployed URl will look something like this 
      For example, https://BI-coding-challenge.onrender.com
2. Ask a question using the input box and submit.
3. View the response displayed in a chat-like interface.

## Technologies Used

- **Backend**: Python, FastAPI, LangChain
- **Frontend**: React, TypeScript, Axios
- **Other Tools**: Git, Docker (Optional for deployment), Virtual Environment (venv)

## Contributing

Feel free to open issues and submit pull requests for any changes.

## License

This project is open source and available under the [MIT License](LICENSE).
```

This `README.md` file provides an overview, installation instructions, usage guide, and future improvements. Make sure to customize it to better reflect your project's needs! Let me know if you need further help.
