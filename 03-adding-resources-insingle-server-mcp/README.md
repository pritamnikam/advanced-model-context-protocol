# Advanced Model Context Protocol: Adding Resources in Single Server MCP

This project further extends the Model Context Protocol (MCP) single server architecture by introducing resource management features. The server now provides weather data, AI model responses, and additional resource endpoints via APIs. The client can fetch weather information, interact with AI models using prompts, and access or manage resources. Secure environment variable management and modular Python structure are maintained.

---

## 🚀 Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/pritamnikam/advanced-model-context-protocol.git
cd 03-adding-resources-insingle-server-mcp
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
03-adding-resources-insingle-server-mcp/
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

1. **Start the server:**
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

Below is a sample session running the client:

```
python mcp_client.py
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1758989537.175191    3720 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.
Weather MCP agent is ready.
Type a question, or use one of the following commands:
  /resources                       - to list available resources
  /resource <resource_uri>         - to load a resource for the agent

You: /resources

Available Resources:
--------------------
  Resource URI: file://delivery_log/
    Description: Reads a delivery log file and returns its contents as a list of lines.
Each line contains an order number and a delivery location.

Usage: /resource <resource_uri>
--------------------

You: /resource file://delivery_log/

--- Fetching resource 'file://delivery_log/'... ---
--- Resource loaded successfully. ---
Resource loaded. What should I do with this content? (Press Enter to just save to context)
> Give me weather report for all the cities listed in the delivery log and show the structured response for all the orders
AI: Here is the weather report for each city:

*   **San Diego:** 21.06°C, broken clouds, humidity 80%, wind speed 2.31 m/s
*   **Austin:** 28.9°C, broken clouds, humidity 52%, wind speed 1.55 m/s
*   **Raleigh:** 23.39°C, overcast clouds, humidity 94%, wind speed 1.2 m/s
*   **Omaha:** 22.28°C, few clouds, humidity 69%, wind speed 4.28 m/s
*   **Orlando:** 28.37°C, overcast clouds, humidity 72%, wind speed 2.65 m/s
*   **Denver:** 19.75°C, clear sky, humidity 49%, wind speed 1.52 m/s
*   **Seattle:** 14.53°C, overcast clouds, humidity 81%, wind speed 0.27 m/s
*   **Kansas City:** 25.43°C, overcast clouds, humidity 58%, wind speed 2.83 m/s
*   **Madison:** 24.93°C, clear sky, humidity 76%, wind speed 1.64 m/s
*   **Sacramento:** 20.1°C, clear sky, humidity 66%, wind speed 1.61 m/s

You: exit
```

---

## 📝 Notes

- This project adds resource management endpoints to the MCP server.
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