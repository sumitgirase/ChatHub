import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(
    page_title="Chat with OpenRouter!",
    page_icon=":robot_face:",  # Set your desired favicon
    layout="wide",  # Choose layout style ('wide' or 'centered')
)

# Initialize OpenRouter client (OpenAI-compatible API)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

MODEL_NAME = "google/gemini-2.5-flash"  # swap for any OpenRouter model you like

# Add a chat history list to Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display Form Title
st.title("Chat with OpenRouter!")

# Display chat messages from history above current input box
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user's next message, add to context, resubmit context to OpenRouter
if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # # Send full conversation history to OpenRouter and read the response
    # response = client.chat.completions.create(
    #     model=MODEL_NAME,
    #     messages=st.session_state.chat_history,
    # )
    # reply = response.choices[0].message.content
        # Send full conversation history to OpenRouter and read the response
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=st.session_state.chat_history,
        max_tokens=1000,  # keep this well under your free credit limit
    )
    reply = response.choices[0].message.content

    # Display and store the assistant's reply
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

     