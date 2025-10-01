# Advanced Model Context Protocol: Implement RAG Server Using MCP

This project demonstrates how to implement a Retrieval-Augmented Generation (RAG) server using the Model Context Protocol (MCP) in Python. The RAG server enables document ingestion and retrieval, allowing users to ask questions based on ingested documents. The architecture leverages LangChain, LangGraph, and Google Gemini for generative AI and embeddings, and supports secure environment variable management.

---

## 🚀 Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/pritamnikam/advanced-model-context-protocol.git
cd 07-implement-rag-server-using-mcp
```

### 2. Create a Python Virtual Environment

```sh
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows (Command Prompt):**
  ```sh
  venv\Scripts\activate
  ```
- **On Windows (PowerShell):**
  ```sh
  .\venv\Scripts\Activate.ps1
  ```
- **On macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 4. Install Dependencies

```sh
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Copy `.env-example` to `.env` and update the values:

```sh
cp .env-example .env
```

Edit `.env` and set your API keys and configuration:

```
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
MODEL_ID=name_of_model
TEMPRATURE=temprature_between_0_to_1
```

---

## 🗂️ Project Structure

```
07-implement-rag-server-using-mcp/
├── mcp_client.py
├── rag_server.py
├── requirements.txt
├── .env
├── .env-example
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables

Set these in your `.env` file:

- `GOOGLE_GEMINI_API_KEY` – *(Required)* Your Google Gemini API key.
- `MODEL_ID` – *(Required)* The model ID to use with Gemini.
- `TEMPRATURE` – *(Optional)* Temperature parameter for model inference (between 0 and 1).

**Example `.env`:**
```
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
MODEL_ID=gemini-pro
TEMPRATURE=0.7
```

> **Never commit your `.env` file to version control.**  
> Use `.env-example` to share required variable names with collaborators.

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`.  
If not present, add these:

```
mcp
langchain
langgraph
langchain-google-genai
langchain-mcp-adapters
python-dotenv
Flask
requests
```

Install them with:

```sh
pip install -r requirements.txt
```

---

## 🏃 Example: How to Run the App

1. **Start the RAG server:**
   ```sh
   python rag_server.py
   ```

2. **In a new terminal, activate your virtual environment and run the client:**
   ```sh
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate

   python mcp_client.py
   ```

---

## 💻 Example Run

```
You: ingest_document employee_handbook.txt
AI: It appears I've exceeded my quota for the embedding model. Unfortunately, I cannot ingest the document at this time. Is there anything else I can help you with?
```

---

## 📝 Notes

- If you encounter quota errors, check your Google Gemini API usage and consider upgrading your plan or requesting a quota increase.
- Ensure your `.env` file is not committed to version control.
- For additional configuration, see `.env-example`.

---

## 🖥️ Troubleshooting

- **PowerShell script execution error:**  
  Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in an Administrator PowerShell window.

- **Virtual environment not activating?**  
  Make sure you are using the correct command for your shell and OS.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.