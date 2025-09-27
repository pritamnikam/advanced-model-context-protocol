# Advanced Model Context Protocol: Single Server MCP Architecture

This project implements a Model Context Protocol (MCP) using a Python client-server architecture. The server provides weather and AI model data via APIs, and the client fetches this data. The project demonstrates secure environment variable management and modular Python application structure, with support for OpenWeatherMap and Google Gemini APIs.

---

## 🚀 Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/pritam.nikam/.git
cd 01-building-single-server-mcp-architecture
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
01-building-single-server-mcp-architecture/
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