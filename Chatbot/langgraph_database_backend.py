from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import sqlite3

load_dotenv()

llm = ChatOpenAI()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)
# Checkpointer
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)

def get_thread_title_from_messages(thread_id: str) -> str:
    """Get the title for a thread by looking at its first user message."""
    try:
        state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
        if state and state.values and state.values.get('messages'):
            messages = state.values['messages']
            # Find the first user message
            for msg in messages:
                if hasattr(msg, 'type') and msg.type == 'human':
                    content = msg.content
                    if content:
                        # Generate title from first line
                        first_line = content.strip().splitlines()[0]
                        words = first_line.split()
                        title = " ".join(words[:8])  # first ~8 words
                        # Soft max length ~50 chars with ellipsis
                        if len(first_line) > 50:
                            title = (title[:50]).rstrip() + "…"
                        return title if title else "New chat"
        return "New chat"
    except Exception:
        return "New chat"