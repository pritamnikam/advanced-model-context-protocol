# Advanced Model Context Protocol: Building Multi-Server MCP Architecture

This project demonstrates a multi-server Model Context Protocol (MCP) architecture in Python. The system consists of multiple backend services (e.g., Weather and Task servers) that the MCP client can interact with for advanced context management, weather data, and task handling. The architecture supports secure environment variable management and modular, scalable design.

---

## 🚀 Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/pritamnikam/advanced-model-context-protocol.git
cd 04-building-multi-server-mcp-architecture
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

> **Note:**  
> If you get a script execution error in PowerShell, run:  
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

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
OPENWEATHERMAP_API_KEY=your_openweather_api_key
OPENWEATHERMAP_API_URL=openweather_api_url

GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
MODEL_ID=name_of_model
TEMPRATURE=temprature_between_0_to_1
```

---

## 🗂️ Project Structure

```
04-building-multi-server-mcp-architecture/
├── mcp_client.py
├── weather_server.py
├── task_server.py
├── requirements.txt
├── .env
├── .env-example
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables

Set these in your `.env` file:

- `OPENWEATHERMAP_API_KEY` – *(Required)* Your OpenWeatherMap API key.
- `OPENWEATHERMAP_API_URL` – *(Required)* The OpenWeatherMap API endpoint URL.
- `GOOGLE_GEMINI_API_KEY` – *(Required for Gemini features)* Your Google Gemini API key.
- `MODEL_ID` – *(Optional)* The model ID to use with Gemini or other AI services.
- `TEMPRATURE` – *(Optional)* Temperature parameter for model inference (between 0 and 1).

**Example `.env`:**
```
OPENWEATHERMAP_API_KEY=your_openweather_api_key
OPENWEATHERMAP_API_URL=https://api.openweathermap.org/data/2.5/weather
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
MODEL_ID=gemini-pro
TEMPRATURE=0.7
```

> **Never commit your `.env` file to version control.**  
> Use `.env-example` to share required variable names with collaborators.

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```
Flask
requests
dotenv
mcp
langchain
langgraph
langchain-google-genai
langchain-mcp-adapters
```

Install them with:

```sh
pip install -r requirements.txt
```

---

## 🏃 Example: How to Run the App

1. **Start the backend servers (in separate terminals):**
   ```sh
   python weather_server.py
   python task_server.py
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

Below is a sample session running the client:

```
python mcp_client.py
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1759034564.829053   19436 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.
MCP Agent is ready (connected to Weather and Task servers).

You: I’m writing a travel report on Tokyo. Get me the current weather and remind me to “Write the Tokyo weather section”.
AI: OK. The current weather in Tokyo is 27.86°C, feels like 28.13°C, with overcast clouds and a wind speed of 7.38 m/s. I've also added "Write the Tokyo weather section" to your to-do list.

You: Show my to-do list.
AI: Here is your to-do list:
1. Write the Tokyo weather section

You: exit
```

---

## 📝 Notes

- This project demonstrates a multi-server MCP architecture with advanced context and resource management.
- Ensure your `.env` file is not committed to version control.
- For additional configuration, see `.env-example`.
- Some dependencies (like `langchain`, `langgraph`, and adapters) are for advanced AI/model integration.

---

## 🖥️ Troubleshooting

- **PowerShell script execution error:**  
  Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in an Administrator PowerShell window.

- **Virtual environment not activating?**  
  Make sure you are using the correct command for your shell and OS.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.