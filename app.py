

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# ---  CONFIGURATION & CLIENT INITIALIZATION ---
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY") 

st.set_page_config(page_title="Tiny AI Q&A App", layout="centered")
st.title("🤖 Tiny AI Q&A Bot")
st.caption("Built with Streamlit (UI) and OpenAI (AI engine).")

# API Key check and client setup
try:
    if not API_KEY:
        st.error("API Key not found. Please check your .env file.")
        st.stop()
    client = OpenAI(api_key=API_KEY)
except Exception as e:
    st.error(f"Error connecting to OpenAI: {e}")
    st.stop()


# ---  SESSION STATE FOR CHAT HISTORY (MEMORY) ---

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm an enthusiastic AI assistant. Ask me anything about technology, science, or general knowledge!"}
    ]

# ---  CORE LOGIC TO INTERACT WITH THE AI ---
def get_ai_response(prompt_messages):
    """Sends the full conversation history to the model and streams the response."""

    with st.spinner("Bot is thinking..."):
        try:
           
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages=prompt_messages,
                stream=True 
            )
            return response
        except Exception as e:
            st.error(f"An API Error Occurred: {e}")
            st.stop()


# --- UI RENDERING AND INPUT HANDLING ---

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("Ask me a question..."):
    
    # a. Add user message to session state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # b. Get and display the streamed response from the AI
    with st.chat_message("assistant"):
        
        # Get response stream from the AI
        stream = get_ai_response(st.session_state.messages)
        
        # Stream the full response to the UI
        full_response = st.write_stream(stream)
    
    # c. Add the final, full response to the session state for memory
    st.session_state.messages.append({"role": "assistant", "content": full_response})