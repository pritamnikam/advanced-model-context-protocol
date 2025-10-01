# Advanced Model Context Protocol

A Python-based client-server architecture demonstrating the Model Context Protocol (MCP) with secure environment management, weather data integration, AI model support, resource/task management, prompt-based workflows, and Retrieval-Augmented Generation (RAG).

## Subprojects

- `01-building-single-server-mcp-architecture/`  
  Single server MCP implementation with weather and AI model APIs.
- `02-adding-prompts-in-single-server-mcp/`  
  Adds prompt-based AI model interaction to the single server MCP.
- `03-adding-resources-insingle-server-mcp/`  
  Adds resource management endpoints and advanced context handling.
- `04-building-multi-server-mcp-architecture/`  
  Demonstrates a multi-server MCP architecture with separate weather and task servers.
- `05-adding-prompts-to-multi-server-mcp/`  
  Adds prompt-based workflows and multi-server prompt orchestration.
- `06-adding-resources-to-multi-server-mcp/`  
  Adds resource management features to both Weather and Task servers, enabling resource-driven workflows.
- `07-implement-rag-server-using-mcp/`  
  Implements a Retrieval-Augmented Generation (RAG) server using MCP, LangChain, LangGraph, and Google Gemini.

## Getting Started

Each subproject contains its own `README.md` with setup and usage instructions.  
Clone this repository and follow the steps in the relevant subproject folder.

## Example Features

- **Weather Server**:  
  - Provides weather data using OpenWeatherMap API.
  - Exposes resource endpoints (e.g., delivery logs).
- **Task Server**:  
  - Manages tasks and supports prompt-based workflows.
  - Exposes resource endpoints (e.g., meeting notes).
- **RAG Server**:  
  - Supports document ingestion and retrieval using generative AI and embeddings.
- **MCP Client**:  
  - Interacts with all servers for weather, tasks, resource-driven operations, and RAG queries.

## Repository Structure

```
advanced-model-context-protocol/
├── 01-building-single-server-mcp-architecture/
├── 02-adding-prompts-in-single-server-mcp/
├── 03-adding-resources-insingle-server-mcp/
├── 04-building-multi-server-mcp-architecture/
├── 05-adding-prompts-to-multi-server-mcp/
├── 06-adding-resources-to-multi-server-mcp/
├── 07-implement-rag-server-using-mcp/
├── README.md
└── .gitignore
```

## Best Practices

- Use `.env-example` to share required environment variable names.
- Never commit your `.env` file or generated files (like `tasks.txt`) to version control.
- Each subproject is self-contained and can be run independently.

## License

MIT License. See [LICENSE](LICENSE) for details.