
# BounceInsights Coding Challenge

This repository contains the implementation of a RAG (Retrieval-Augmented Generation) system using FastAPI for backend development and React with TypeScript for the frontend. The project allows users to ask questions and get responses from a RAG-based system.

# Project Structure
   ```markdown
      BounceInsights/
      |----backend/
      |    |----routers/
      |        |----rag.py
      |    |----main.py
      |    |----data/
      |        |----Dataset1.xlsx
      |        |----Dataset2.xlsx
      |----frontend/
      |    |----src/
      |        |----components/
      |            |----QueryForm.tsx
      |            |----ResultsDisplay.tsx
      |        |----services/
      |            |----api.ts
      |        |----App.tsx
      |    |----public/
      |    |----package.json
      |    |----tsconfig.json
      |----README.md
      |----requirements.txt
   ```

## Installation and Setup

### Prerequisites
- Python 3.8+
- Node.js (v14+ recommended)
- npm or yarn
- Virtual Environment (venv)

### Backend Setup

1. Clone the respository:

   ```bash
   git clone https://github.com/Khubaibakramshirani/BounceInsights-Coding-Challenge.git
   cd BounceInsights-Coding-Challenge/backend
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

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the React development server:
   ```bash
   npm start
   ```

4. The frontend will be available at `http://localhost:3000` and will communicate with the backend running at `http://127.0.0.1:8000`.

## Usage

1. Navigate to `http://localhost:3000` in your browser.
2. Ask a question using the input box and submit.
3. View the response displayed in a chat-like interface.

## Technologies Used

- **Backend**: Python, FastAPI, LangChain
- **Frontend**: React, TypeScript, Axios
- **Other Tools**: Git, Docker (Optional for deployment), Virtual Environment (venv)

## To Do
- [ ] Add more features to the RAG system.
- [ ] Improve the frontend UI/UX.
- [ ] Add Docker support for easy deployment.

## Contributing

Feel free to open issues and submit pull requests for any changes.

## License

This project is open source and available under the [MIT License](LICENSE).
```

This `README.md` file provides an overview, installation instructions, usage guide, and future improvements. Make sure to customize it to better reflect your project's needs! Let me know if you need further help.
