# Advanced Model Context Protocol (MCP)

A Python-based framework for building advanced client-server architectures that leverage the Model Context Protocol (MCP) for modular, scalable, and context-aware AI applications. The repository demonstrates secure environment management, weather data integration, AI model orchestration, resource/task management, prompt-based workflows, and Retrieval-Augmented Generation (RAG) using modern tools like LangChain, LlamaIndex, and Google Gemini.

---

## 📚 Subprojects

- **01-building-single-server-mcp-architecture/**  
  Single server MCP implementation with weather and AI model APIs.

- **02-adding-prompts-in-single-server-mcp/**  
  Adds prompt-based AI model interaction to the single server MCP.

- **03-adding-resources-insingle-server-mcp/**  
  Adds resource management endpoints and advanced context handling.

- **04-building-multi-server-mcp-architecture/**  
  Demonstrates a multi-server MCP architecture with separate weather and task servers.

- **05-adding-prompts-to-multi-server-mcp/**  
  Adds prompt-based workflows and multi-server prompt orchestration.

- **06-adding-resources-to-multi-server-mcp/**  
  Adds resource management features to both Weather and Task servers, enabling resource-driven workflows.

- **07-implement-rag-server-using-mcp/**  
  Implements a Retrieval-Augmented Generation (RAG) server using MCP, LangChain, LangGraph, and Google Gemini.

- **08-integrating-mcp-with-llamaindex/**  
  Integrates MCP with LlamaIndex for advanced agent workflows and multi-block response support.

---

## 🚀 Getting Started

Each subproject contains its own `README.md` with setup and usage instructions.  
Clone this repository and follow the steps in the relevant subproject folder.

### Example Workflow

- Start the relevant servers (e.g., weather, task, RAG).
- Run the MCP client to interact with the servers using natural language, prompts, or resource-driven commands.
- Use `.env-example` to configure environment variables for API keys and model parameters.

---

## 🗂️ Repository Structure

```
advanced-model-context-protocol/
├── 01-building-single-server-mcp-architecture/
├── 02-adding-prompts-in-single-server-mcp/
├── 03-adding-resources-insingle-server-mcp/
├── 04-building-multi-server-mcp-architecture/
├── 05-adding-prompts-to-multi-server-mcp/
├── 06-adding-resources-to-multi-server-mcp/
├── 07-implement-rag-server-using-mcp/
├── 08-integrating-mcp-with-llamaindex/
├── README.md
└── .gitignore
```

---

## 🛡️ Best Practices

- Use `.env-example` to share required environment variable names.
- Never commit your `.env` file or generated files (like `tasks.txt`) to version control.
- Each subproject is self-contained and can be run independently.
- Keep dependencies updated for compatibility with multi-block message support.

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for details.