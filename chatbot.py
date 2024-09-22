import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyCY9bZ4hcxwR2pi_sosuSzzgtCRtAOZDDk"
genai.configure(api_key=GOOGLE_API_KEY)

# Model Initiate
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Custom Styles
st.markdown("""
<style>
    .css-1v3fv1e {
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .css-1v3fv1e:hover {
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
    .response-area {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f0f0f0;
        border: 1px solid #ddd;
    }
    .response-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #fff;
        border: 1px solid #ccc;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.title("🤖 S M O K I E | C H A T B O T 🤖")
st.write("Ask Smokie AI Anything 🤔")

# Chat Form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000, placeholder="Type your question or prompt...")
    submit_button = st.form_submit_button("Send 💬", help="Click to get a response from Smokie AI")

    if submit_button:
        if user_input:
            response = getResponseFromModel(user_input)
            st.write("You: " + user_input)
            with st.container():
                    st.markdown(f"Smokie: {response}", unsafe_allow_html=True)
                    st.write("")
        else:
            st.warning("Please Enter A Prompt ⚠️")