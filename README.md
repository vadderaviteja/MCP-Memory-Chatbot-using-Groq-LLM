# 🧠 MCP Memory Chatbot using Groq LLM

This project is an **interactive AI chatbot** built using **MCP (Model Context Protocol)** with **conversation memory enabled**. It uses **Groq's LLaMA-4 model** for fast inference and integrates with an **Airbnb MCP Server** for tool-based reasoning.

The chatbot supports:

* Multi-turn conversations
* Built-in memory (context persistence)
* Tool calling via MCP
* Interactive CLI-based chat

---

## 🚀 Features

* 🔗 **MCP Client–Server Architecture** (Airbnb MCP Server)
* 🧠 **Conversation Memory Enabled**
* ⚡ **Groq LLM Integration** (LLaMA-4 Maverick)
* 🛠️ **Tool Invocation with Structured JSON**
* 🧹 Commands to clear memory and exit chat
* 🖥️ Fully **async** Python implementation

---

## 🏗️ Project Architecture

```
User (CLI)
   ↓
MCPAgent (Memory + Reasoning)
   ↓
Groq LLM (LLaMA-4)
   ↓
MCP Client
   ↓
Airbnb MCP Server (Tools)
```

---

## 📁 Project Structure

```
MCP-Memory-Chatbot/
│
├── main.py                # Entry point (async chat loop)
├── mcp_config.json        # MCP server configuration
├── .env                   # Environment variables (API keys)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Requirements

* Python **3.11**
* Groq API Key
* Airbnb MCP Server

### Python Libraries

* `mcp_use`
* `langchain-groq`
* `python-dotenv`
* `asyncio`

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```
GROQ_API=your_groq_api_key_here
```

---

## 🧩 MCP Configuration

Ensure `mcp_config.json` is correctly set up to connect to the **Airbnb MCP Server**.

Example:

```
{
    "mcpServers": {
      "airbnb": {
        "command": "npx",
        "args": [
          "-y",
          "@openbnb/mcp-server-airbnb"
        ]
      }
    }
  }
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start the chatbot:

```
python main.py
```

---

## 💬 Chat Commands

| Command         | Description               |
| --------------- | ------------------------- |
| `exit` / `quit` | End the chat              |
| `clear`         | Clear conversation memory |

---

## 🧠 Memory Behavior

* The chatbot **remembers previous messages** within a session
* Memory can be cleared manually using the `clear` command
* Memory helps in contextual follow-up questions

---

## 🤖 LLM Details

* **Provider:** Groq
* **Model:** `meta-llama/llama-4-maverick-17b-128e-instruct`
* **Inference:** Ultra-low latency via Groq

---

## 🛠️ Key Code Highlights

* Uses `MCPAgent` with `memory_enabled=True`
* Enforces **strict JSON typing** for tool calls
* Graceful session cleanup using async context

---

## 🔮 Future Enhancements

* Web UI using Streamlit or React
* Persistent memory (vector DB)
* Authentication & user sessions
* Multi-agent MCP workflows

---

## 📌 Use Case

This project is ideal for:

* MCP learning & experimentation
* Tool-augmented LLM systems
* Enterprise AI assistants
* Research on conversational memory

---

## 👤 Author

**Raviteja**
AI / Data Science Enthusiast
Focused on GenAI, MCP, LangGraph, and LLM Systems

---

## 📄 License

This project is for educational and research purposes.
