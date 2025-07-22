# Agentic AI by LangGraph

A collection of modular agentic AI workflows and demos built with [LangGraph](https://github.com/langchain-ai/langgraph).

---

## 📂 Project Overview

**Current Workflows:**
- `1_bmi_workflow.ipynb` — BMI calculation workflow
- `2_simple_llm_workflow.ipynb` — Simple LLM Q&A workflow
- `3_prompt_chaining.ipynb` — Prompt chaining demo
- `4_batsman_workflow.ipynb` — Cricket batsman stats analyzer
- `5_UPSC_essay_workflow.ipynb` — UPSC essay workflow
- `6_quadratic_equation_workflow.ipynb` — Quadratic equation solver workflow
- `7_review_reply_workflow.ipynb` — Automated review reply generator workflow
- `8_X_post_generator.ipynb` - Loop in Langchain

**Tech Stack:**
- Python 3.13+
- Jupyter Notebooks
- LangGraph, LangChain, OpenAI

> **More workflows and features coming soon!**

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rkuma18/agentic-ai-by-langgraph.git
   cd agentic-ai-by-langgraph
   ```
2. **Set up your environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the notebooks:**
   ```bash
   jupyter notebook
   ```

---

## Environment & Secrets
- **Never commit your `.env` file or any secrets.**
- Store API keys and environment variables in a local `.env` file (see `.gitignore`).
- Example usage:
  ```python
  from dotenv import load_dotenv
  load_dotenv()
  ```

---

## 📢 Contributing
Pull requests and suggestions are welcome! More workflows and improvements are on the way.

---

## 📄 License
MIT 
