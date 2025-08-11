import streamlit as st
from langgraph_database_backend import chatbot, retrieve_all_threads, get_thread_title_from_messages
from langchain_core.messages import HumanMessage
import uuid

# =========================================
# Helpers
# =========================================

def generate_thread_id() -> str:
    return str(uuid.uuid4())

def init_session():
    if 'message_history' not in st.session_state:
        st.session_state['message_history'] = []
    if 'thread_id' not in st.session_state:
        st.session_state['thread_id'] = generate_thread_id()
    if 'chat_threads' not in st.session_state:
        # Convert thread IDs to the expected dict format with proper titles
        thread_ids = retrieve_all_threads()
        st.session_state['chat_threads'] = [{"id": tid, "title": get_thread_title_from_messages(tid)} for tid in thread_ids]

def reset_chat():
    """Start a brand-new, not-yet-listed chat (no sidebar entry until first user message)."""
    st.session_state['thread_id'] = generate_thread_id()
    st.session_state['message_history'] = []

def add_thread(thread_id: str, title: str):
    """Add a chat thread to the list."""
    st.session_state['chat_threads'].append({"id": thread_id, "title": title})

def load_conversation(thread_id: str):
    """Load conversation from backend and convert to simple dicts for UI."""
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    messages = state.values['messages'] if state and state.values else []

    temp_messages = []
    for msg in messages:
        role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
        temp_messages.append({'role': role, 'content': msg.content})
    return temp_messages

def set_thread_title_from_text(thread_id: str, text: str):
    """Generate a short title from the first user message and update the thread."""
    first_line = (text or "").strip().splitlines()[0]
    words = first_line.split()
    title = " ".join(words[:8])  # first ~8 words
    # Soft max length ~50 chars with ellipsis
    if len(first_line) > 50:
        title = (title[:50]).rstrip() + "…"
    # Update title in session
    for t in st.session_state['chat_threads']:
        if t['id'] == thread_id:
            t['title'] = title if title else "New chat"
            break

def get_thread_title(thread_id: str) -> str:
    for t in st.session_state['chat_threads']:
        if t['id'] == thread_id:
            return t['title']
    return "New chat"

def thread_exists(thread_id: str) -> bool:
    return any(t["id"] == thread_id for t in st.session_state['chat_threads'])

# =========================================
# Session setup
# =========================================
init_session()

# =========================================
# Sidebar UI
# =========================================
st.sidebar.title('Personal Chatbot')

if st.sidebar.button('New Chat', use_container_width=True):
    reset_chat()

st.sidebar.header('My Conversations')

# Show latest first
for thread in reversed(st.session_state['chat_threads']):
    label = (thread["title"] or "New chat").strip()
    if st.sidebar.button(label, key=f"thread-btn-{thread['id']}", use_container_width=True):
        st.session_state['thread_id'] = thread['id']
        st.session_state['message_history'] = load_conversation(thread['id'])

# Current chat title (only if it already exists), else show a neutral header
current_title = get_thread_title(st.session_state['thread_id']) if thread_exists(st.session_state['thread_id']) else "New chat"
st.subheader(current_title)

# =========================================
# Main Chat UI
# =========================================

# Render message history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:
    # Is this the first user message in this (UI) session?
    is_first_user_message = not any(m['role'] == 'user' for m in st.session_state['message_history'])

    # If the thread isn't listed yet, this is a brand-new chat → create it now
    if is_first_user_message and not thread_exists(st.session_state['thread_id']):
        # Add temporary title, then immediately set from the user message
        add_thread(st.session_state['thread_id'], title="New chat")
        set_thread_title_from_text(st.session_state['thread_id'], user_input)

    # Append user message to UI/history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    # Stream assistant response
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )

    # Append assistant message to in-memory history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
