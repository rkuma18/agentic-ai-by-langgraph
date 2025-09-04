# Agentic AI Workflows with LangGraph

A comprehensive collection of modular, agentic AI workflows built using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchainchain), and OpenAI LLMs. Features include interactive chatbots, persistent conversations, and a modern Streamlit interface.

![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-0.x-success?logo=github)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-3.x-green?logo=sqlite)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## 🚀 Project Overview

This project demonstrates the power of LangGraph for building sophisticated AI workflows, from simple calculations to interactive chatbots with persistent memory. Each workflow showcases different aspects of agentic AI development.

### 🔥 Featured Workflows

| # | Filename | Description | Type |
|--|----------|-------------|------|
| 1 | `1_bmi_workflow.ipynb` | BMI calculation workflow | Notebook |
| 2 | `2_simple_llm_workflow.ipynb` | Simple LLM Q&A | Notebook |
| 3 | `3_prompt_chaining.ipynb` | Prompt chaining demo | Notebook |
| 4 | `4_batsman_workflow.ipynb` | Cricket batsman stats analyzer | Notebook |
| 5 | `5_UPSC_essay_workflow.ipynb` | UPSC essay topic generator | Notebook |
| 6 | `6_quadratic_equation_workflow.ipynb` | Quadratic equation solver | Notebook |
| 7 | `7_review_reply_workflow.ipynb` | Auto-generated review replies | Notebook |
| 8 | `8_X_post_generator.ipynb` | Loop-based X (Twitter) post creator | Notebook |
| 9 | `9_basic_chatbot.ipynb` | Basic chatbot workflow | Notebook |

### 💬 Interactive Chatbot (New!)

The **Chatbot/** directory contains a fully-featured, production-ready chatbot with:

- **Persistent Conversations**: SQLite database storage for all chat history
- **Modern UI**: Beautiful Streamlit interface with real-time streaming
- **Thread Management**: Organize conversations with automatic title generation
- **Memory Persistence**: Conversations survive app restarts
- **Real-time Streaming**: Instant AI responses with typing indicators
- **Tool Integration**: Advanced chatbot with calculator, stock prices, and web search

#### Chatbot Features:

**🔧 Tool-Enabled Chatbot (Latest!)**
- `v1_streamlit_frontend_tool.py` - Advanced chatbot with integrated tools
- `v1_langgraph_tool_backend.py` - Backend with calculator, stock lookup, and web search
- **Tools Available**:
  - 🧮 **Calculator**: Basic arithmetic operations (add, subtract, multiply, divide)
  - 📈 **Stock Prices**: Real-time stock price lookup via Alpha Vantage API
  - 🔍 **Web Search**: DuckDuckGo search integration for current information
  - 📊 **Visual Tool Status**: Real-time indicators showing when tools are being used

**💾 Database Chatbot**
- `streamlit_frontend_database.py` - Main chatbot with database persistence
- `langgraph_database_backend.py` - LangGraph backend with SQLite checkpointing

**⚡ Streaming Chatbot**
- `streamlit_frontend_streaming.py` - Streaming version without persistence
- `streamlit_frontend.py` - Basic version for comparison

---

## 🛠️ Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/rkuma18/agentic-ai-by-langgraph.git
cd agentic-ai-by-langgraph
```

### 2. Set Up Environment
```bash
python -m venv myenv
source myenv/bin/activate    # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Workflows

#### Jupyter Notebooks
```bash
jupyter notebook  # for .ipynb files
```

#### Interactive Chatbot

**🔧 Tool-Enabled Chatbot (Recommended)**
```bash
cd Chatbot
streamlit run v1_streamlit_frontend_tool.py
```

**💾 Database Chatbot**
```bash
cd Chatbot
streamlit run streamlit_frontend_database.py
```

**⚡ Other Chatbot Versions**
```bash
streamlit run streamlit_frontend_streaming.py  # Streaming without persistence
streamlit run streamlit_frontend.py           # Basic version
```

---

## 🏗️ Tech Stack

### Core Technologies
- **LangGraph** – State-driven agentic workflows and conversation management
- **LangChain** – Language model orchestration and message handling
- **OpenAI API** – GPT models for intelligent responses
- **Python 3.13+** – Modern Python with latest features

### Tool Integration
- **DuckDuckGo Search** – Real-time web search capabilities
- **Alpha Vantage API** – Stock market data and price lookups
- **Custom Tools** – Calculator and other utility functions
- **Tool Orchestration** – Automatic tool selection and execution

### Frontend & UI
- **Streamlit** – Modern, responsive web interface
- **Real-time Streaming** – Live typing indicators and instant responses
- **Responsive Design** – Works on desktop and mobile devices

### Data Persistence
- **SQLite** – Lightweight, reliable database storage
- **LangGraph Checkpoints** – Persistent conversation state management
- **Thread Management** – Organized conversation history

### Development Tools
- **Jupyter Notebooks** – Interactive workflow development
- **Environment Management** – Virtual environments and dependency isolation
- **Git Version Control** – Collaborative development and version tracking

---

## 🔧 Environment Setup

### 1. API Configuration
Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Dependencies
All required packages are listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Database Setup
The chatbot automatically creates and manages its SQLite database (`chatbot.db`) in the Chatbot directory.

---

## 📱 Using the Chatbot

### Getting Started

**🔧 Tool-Enabled Chatbot (Recommended)**
1. Navigate to the Chatbot directory
2. Run `streamlit run v1_streamlit_frontend_tool.py`
3. Open your browser to the provided URL
4. Start chatting with access to tools!

**💾 Database Chatbot**
1. Navigate to the Chatbot directory
2. Run `streamlit run streamlit_frontend_database.py`
3. Open your browser to the provided URL
4. Start chatting!

### Features

**🔧 Tool-Enabled Chatbot Features:**
- **Smart Tools**: Calculator, stock prices, and web search
- **Visual Tool Status**: See when tools are being used with status indicators
- **Automatic Tool Selection**: AI chooses the right tool for your request
- **Real-time Tool Execution**: Watch tools work in real-time
- **Persistent Conversations**: All chats saved with SQLite database

**💾 Database Chatbot Features:**
- **New Chat**: Start fresh conversations
- **Conversation History**: Access all previous chats from the sidebar
- **Auto-titles**: Conversations are automatically titled based on your first message
- **Persistent Memory**: All conversations are saved and restored
- **Real-time Responses**: See AI responses as they're generated

### Conversation Management
- Each conversation gets a unique thread ID
- Titles are automatically generated from your first message
- Conversations are organized chronologically in the sidebar
- Switch between conversations seamlessly

---

## 🧪 Development & Testing

### Running Tests
```bash
# Test individual workflows
python -m pytest tests/

# Run specific notebook
jupyter notebook 1_bmi_workflow.ipynb
```

### Adding New Workflows
1. Create a new `.ipynb` file in the root directory
2. Follow the naming convention: `{number}_{description}_workflow.ipynb`
3. Update this README with your new workflow
4. Submit a pull request!

### Chatbot Customization
- Modify `langgraph_database_backend.py` to change AI behavior
- Customize the UI in `streamlit_frontend_database.py`
- Add new features like file uploads, image generation, etc.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
- 🐛 **Report Bugs**: Open an issue with detailed descriptions
- 💡 **Suggest Features**: Share your ideas for new workflows
- 🔧 **Code Contributions**: Submit pull requests with improvements
- 📚 **Documentation**: Help improve docs and examples
- 🌟 **Star the Repo**: Show your support!

### Development Workflow
```bash
# Fork and clone
git clone https://github.com/your-username/agentic-ai-by-langgraph.git

# Create feature branch
git checkout -b feature/amazing-new-workflow

# Make changes and commit
git add .
git commit -m "Add amazing new workflow"

# Push and create PR
git push origin feature/amazing-new-workflow
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

---

## 🔗 Connect & Support

### Developer
- **GitHub**: [@rkuma18](https://github.com/rkuma18)
- **Twitter/X**: [@rkuma07](https://x.com/rkuma07) 
- **Portfolio**: [Roushan Kumar](https://itsrkumar.com/)

### Project Links
- **Repository**: [GitHub](https://github.com/rkuma18/agentic-ai-by-langgraph)
- **Issues**: [Bug Reports](https://github.com/rkuma18/agentic-ai-by-langgraph/issues)
- **Discussions**: [Community Chat](https://github.com/rkuma18/agentic-ai-by-langgraph/discussions)

---

## 🎯 Roadmap

### Upcoming Features
- [ ] Multi-modal support (images, documents)
- [ ] Advanced conversation analytics
- [ ] Custom AI model integration
- [ ] API endpoints for external access
- [ ] Mobile app version
- [ ] Multi-language support

### Recent Updates
- ✅ **v2.1**: Added tool-enabled chatbot with calculator, stock prices, and web search
- ✅ **v2.0**: Added persistent chatbot with database storage
- ✅ **v1.5**: Implemented real-time streaming responses
- ✅ **v1.0**: Core workflow collection with Jupyter notebooks

---

> Built with ❤️ using LangGraph, LangChain, OpenAI, and Streamlit.
> 
> *Empowering developers to build intelligent, conversational AI applications.*