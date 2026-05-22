import streamlit as st

from assistants.memory import ConversationMemory
from assistants.safety import is_safe
from assistants.oss_assistant import OSSAssistant
from assistants.frontier_assistant import FrontierAssistant

st.set_page_config(page_title="AI Assistant Comparison")

st.title("AI Assistant Comparison")

assistant_choice = st.sidebar.selectbox(
    "Choose Assistant",
    ["OSS Assistant", "Frontier Assistant"]
)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "oss" not in st.session_state:
    st.session_state.oss = OSSAssistant()

if "frontier" not in st.session_state:
    st.session_state.frontier = FrontierAssistant()

messages = st.session_state.memory.get_messages()

for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask something...")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.memory.add_message(
        "user",
        user_input
    )

    if not is_safe(user_input):

        response = "I cannot help with harmful requests."

    else:

        try:

            if assistant_choice == "OSS Assistant":

                response = st.session_state.oss.generate_response(
                    st.session_state.memory.get_messages()
                )

            else:

                response = st.session_state.frontier.generate_response(
                    st.session_state.memory.get_messages()
                )

        except Exception as e:

            response = f"Error: {str(e)}"

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.memory.add_message(
        "assistant",
        response
    )