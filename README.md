# Agentic AI Workflows with LangGraph

A growing collection of modular, agentic AI workflows built using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and OpenAI LLMs.

![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-0.x-success?logo=github)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## Project Overview

**Current Workflows:**
| # | Filename | Description |
|--|----------|-------------|
| 1 | `1_bmi_workflow.ipynb` | BMI calculation workflow |
| 2 | `2_simple_llm_workflow.ipynb` | Simple LLM Q&A |
| 3 | `3_prompt_chaining.ipynb` | Prompt chaining demo |
| 4 | `4_batsman_workflow.ipynb` | Cricket batsman stats analyzer |
| 5 | `5_UPSC_essay_workflow.ipynb` | UPSC essay topic generator |
| 6 | `6_quadratic_equation_workflow.ipynb` | Quadratic equation solver |
| 7 | `7_review_reply_workflow.ipynb` | Auto-generated review replies |
| 8 | `8_X_post_generator.ipynb` | Loop-based X (Twitter) post creator |
| 9 | `9_stream_chat_workflow.py` | Streaming chatbot with LangGraph and memory checkpointing |

> *More workflows coming soon! Stay tuned.*

---

## Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/rkuma18/agentic-ai-by-langgraph.git
cd agentic-ai-by-langgraph
````

### 2. Set Up Environment

```bash
python -m venv myenv
source myenv/bin/activate    # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Workflows

```bash
jupyter notebook  # for .ipynb files
python 9_stream_chat_workflow.py  # for chat workflow
```

---

## Tech Stack

* **LangGraph** – State-driven agentic workflows
* **LangChain** – Language model orchestration
* **OpenAI API** – Powering LLM tasks
* **Python 3.13+**
* **Jupyter Notebooks**
* **MemorySaver** – For LLM memory checkpoints

---

## Environment Setup

Create a `.env` file in the root directory to securely store secrets like your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_key_here
```

Load them in your scripts with:

```python
from dotenv import load_dotenv
load_dotenv()
```

`.env` is already included in `.gitignore` for your safety.

---

## Contributing

Got a new workflow idea or want to improve an existing one? Contributions are welcome!

```bash
# Fork the repo and create a new branch
git checkout -b feature/my-awesome-workflow
```

Pull requests, ideas, and issues are encouraged.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Connect with Me

* GitHub: [@rkuma18](https://github.com/rkuma18)
* Twitter/X: [@rkuma07](https://x.com/rkuma07) 
* Portfolio: [Roushan Kumar](https://itsrkumar.com/)

---

> Built with ❤️ using LangGraph, LangChain, and OpenAI.