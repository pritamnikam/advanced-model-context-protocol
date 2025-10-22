# Advanced Model Context Protocol: Adding Resources to Multi-Server MCP

This project extends the multi-server Model Context Protocol (MCP) architecture in Python by introducing resource management features to both the Weather and Task servers. The MCP client can interact with these servers for advanced context management, weather data, task handling, and resource-driven workflows. The architecture supports secure environment variable management and modular, scalable design.

---

## 🚀 Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/pritamnikam/advanced-model-context-protocol.git
cd 06-adding-resources-to-multi-server-mcp
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
06-adding-resources-to-multi-server-mcp/
├── mcp_client.py
├── weather_server.py
├── task_server.py
├── delivery_log.txt
├── meeting_notes.txt
├── requirements.txt
├── .env
├── .env-example
├── .gitignore
├── tasks.txt
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
python .\mcp_client.py
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1759278999.526151    7920 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.
MCP Agent is ready (connected to Weather and Task servers).
Type a question, or use one of the following commands:
  /resources                             - to list available resources
  /resource <server_name> <resource_uri>      - to load a resource for the agent

You: /resources

Available Resources from all servers:
-------------------------------------

--- Server: 'weather' ---
  Resource URI: file://delivery_log/
    Description:
Reads a delivery log file and returns its contents as a list of lines.
Each line contains an order number and a delivery location.

--- Server: 'tasks' ---
  Resource URI: file://meeting_notes/
    Description:
Reads a meeting notes file and returns its contents as a list of lines.
The notes contain discussion points and action items for an Ed Tech company.

Use: /resource <server_name> <resource_uri>
-----------------------------------

You: /resource weather file://delivery_log

--- Fetching resource 'file://delivery_log' from server 'weather'... ---
--- Resource content loaded successfully. ---
Resource loaded. What should I do with this content? (Press Enter to just save to context)
> Give me weather report for all the locations listed in the delivery log file and show a structured response for all orders.
AI: Here is the weather report for all the locations listed in the delivery log file:

*   **Order #10583: San Diego:** 23.9°C, clear sky, feels like 24.02°C
*   **Order #10584: Austin:** 30.37°C, clear sky, feels like 29.18°C
*   **Order #10585: Raleigh:** 20.99°C, overcast clouds, feels like 21.29°C
*   **Order #10586: Omaha:** 23.66°C, overcast clouds, feels like 23.44°C
*   **Order #10587: Orlando:** 25.25°C, scattered clouds, feels like 26°C
*   **Order #10588: Denver:** 22.54°C, broken clouds, feels like 21.74°C
*   **Order #10589: Seattle:** 18.41°C, light rain, feels like 17.74°C
*   **Order #10590: Kansas City:** 23.53°C, overcast clouds, feels like 23.37°C
*   **Order #10591: Madison:** 23.59°C, broken clouds, feels like 23.91°C
*   **Order #10592: Sacramento:** 21.82°C, overcast clouds, feels like 21.44°C

You: /resource tasks file://meeting_notes

--- Fetching resource 'file://meeting_notes' from server 'tasks'... ---
--- Resource content loaded successfully. ---
Resource loaded. What should I do with this content? (Press Enter to just save to context)
> Process notes from the recent meeting and add all of the action items on my to-do list.
AI: OK. I've added the following action items to your to-do list:

*   Arjun to design a lightweight “quick recap” section before quizzes to test if it improves retention.
*   Dani will prototype a visual progress tracker for module pages by next week.
*   Jenna to draft 2–3 motivational nudge email templates for A/B testing.

You: exit
```

---

## 🌐 Features

- **Weather Server**:  
  - Provides weather data using OpenWeatherMap API.
  - Exposes a resource endpoint (`file://delivery_log`) to read delivery logs from `delivery_log.txt`.
- **Task Server**:  
  - Manages tasks and supports prompt-based workflows.
  - Exposes a resource endpoint (`file://meeting_notes`) to read meeting notes from `meeting_notes.txt`.
- **MCP Client**:  
  - Interacts with both servers for weather, tasks, and resource-driven operations.

---

## 📝 Notes

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