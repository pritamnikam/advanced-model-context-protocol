# my-python-project/README.md

# My Python Project

This project consists of a client-server architecture for fetching weather data. The client interacts with the server to retrieve weather information.

## Setup Instructions

1. **Create a Python Virtual Environment**:
   Run the command:
   ```
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Run the command:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   - Start the weather server:
     ```
     python weather_server.py
     ```
   - Run the client:
     ```
     python mcp_client.py
     ```

## Project Structure

```
my-python-project
├── mcp_client.py
├── weather_server.py
├── requirements.txt
├── .env
└── README.md
```

## Environment Variables

Create a `.env` file in the project root and add the following variables:

```
API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
```

## Dependencies

This project requires the following Python packages:

- Flask
- requests

Make sure to install them using the `requirements.txt` file.