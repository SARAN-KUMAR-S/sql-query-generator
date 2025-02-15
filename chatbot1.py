import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="SQL Query Generator",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        text-align: center;
        color: #2E4053;
        font-size: 3rem !important;
        margin-bottom: 2rem !important;
    }
    .stTextInput {
        border-radius: 10px;
    }
    .stButton button {
        width: 100%;
        border-radius: 20px;
        background-color: #2E4053;
        color: white;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #34495E;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .css-1v0mbdj.etr89bj1 {
        width: 100%;
        max-width: 800px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Gemini
genai.configure(api_key="AIzaSyAzK5B5SW7Js7ECStWmk1aNtKXi3DMa74w")

def generate_sql(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        system_prompt = "You are an expert at converting natural language into SQL queries. Convert the following text into a SQL query:"
        response = model.generate_content(system_prompt + prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# App Header with Animation
st.markdown("""
    <h1 style='text-align: center; color: #2E4053; animation: fadeIn 1.5s;'>
        ✨ SQL Query Generator ✨
    </h1>
    """, unsafe_allow_html=True)

# Info Box
with st.container():
    st.info("""
    👋 Welcome to the SQL Query Generator! 
    Simply type your request in natural language, and I'll convert it into a SQL query for you.
    """)

# Main Input Section
with st.container():
    # User Input
    user_input = st.text_area(
        "What would you like to query?",
        placeholder="Example: Show me all customers who made purchases over $1000 last month",
        height=100
    )

    # Generate Button
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        generate_button = st.button("🚀 Generate SQL Query", use_container_width=True)

# Results Section
if generate_button and user_input:
    with st.spinner("🤔 Generating your SQL query..."):
        result = generate_sql(user_input)
        
        # Display Result in a Nice Box
        st.markdown("### 🎉 Generated SQL Query")
        st.code(result, language="sql")
        
        # Copy Button
        st.button("📋 Copy to Clipboard", key="copy")

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 2rem; padding: 1rem; background-color: #f8f9fa; border-radius: 10px;'>
        <p style='color: #6c757d;'>Made with ❤️ by GCT</p>
    </div>
    """, unsafe_allow_html=True)