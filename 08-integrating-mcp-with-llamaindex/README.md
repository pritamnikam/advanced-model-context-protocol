# Advanced Model Context Protocol: Integrating MCP with LlamaIndex

This project demonstrates how to integrate the Model Context Protocol (MCP) with LlamaIndex for advanced agent workflows in Python. The agent uses Google Gemini for LLM capabilities and MCP tools for weather queries, supporting multi-block responses and secure environment variable management.

---

## 🚀 Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/pritamnikam/advanced-model-context-protocol.git
cd 08-integrating-mcp-with-llamaindex
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
08-integrating-mcp-with-llamaindex/
├── mcp_client.py
├── weather_server.py
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

**requirements.txt**
```
llama-index
llama-index-core
llama-index-llms-google-genai
llama-index-tools-mcp
mcp
python-dotenv
Flask
requests
```
> Update or add these if missing.

Install them with:

```sh
pip install -r requirements.txt
```

---

## 🏃 Example: How to Run the App

1. **Start the weather server:**
   ```sh
   python weather_server.py
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
You: What is the weather in London?
Running step init_run
Step init_run produced event AgentInput
Running step setup_agent
Step setup_agent produced event AgentSetup
Running step run_agent_step
Step run_agent_step produced event AgentOutput
Running step parse_agent_output
Step parse_agent_output produced no event
Running step call_tool
Step call_tool produced event ToolCallResult
Running step aggregate_tool_results
Step aggregate_tool_results produced event AgentInput    
Running step setup_agent
Step setup_agent produced event AgentSetup
Running step run_agent_step
Step run_agent_step produced event AgentOutput
Running step parse_agent_output
An error occurred: ChatMessage contains multiple blocks, use 'ChatMessage.blocks' instead.
```

---

## 📝 Notes

- If you encounter the error `ChatMessage contains multiple blocks, use 'ChatMessage.blocks' instead.`, ensure all code and dependencies use `.blocks` for multi-block messages.
- Update all related libraries (`llama_index`, `mcp`, etc.) to the latest version.
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