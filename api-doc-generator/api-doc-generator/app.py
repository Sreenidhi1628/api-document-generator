import streamlit as st
from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="API Doc Generator", page_icon="📄")
st.title("📄 API Documentation Generator")
st.write("Paste your Python code and get professional documentation instantly!")

input_method = st.radio("How do you want to input your code?", ["Paste code", "Upload .py file"])

code = ""

if input_method == "Paste code":
    code = st.text_area("Paste your Python code here", height=250)
else:
    uploaded_file = st.file_uploader("Upload a .py file", type=["py"])
    if uploaded_file:
        code = uploaded_file.read().decode("utf-8")
        st.code(code, language="python")

fmt_md = st.checkbox("Markdown (.md)", value=True)
fmt_html = st.checkbox("HTML page", value=True)

if st.button("Generate Documentation"):
    if not code.strip():
        st.warning("Please enter some code first!")
    else:
        with st.spinner("Generating documentation..."):
            prompt = f"""You are an API documentation generator. Analyze this Python code and generate professional documentation.

Return ONLY a valid JSON object with this structure:
{{
  "markdown": "...full markdown documentation...",
  "html": "...full HTML documentation snippet..."
}}

Each function should have: description, parameters, return value, example usage.

Python code:
{code}"""

            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}]
                )

                result = response.choices[0].message.content
                result = result.replace("```json", "").replace("```", "").strip()
                parsed = json.loads(result, strict=False)

                if fmt_md and "markdown" in parsed:
                    st.subheader("Markdown Documentation")
                    st.text_area("", parsed["markdown"], height=300)
                    st.download_button("⬇ Download .md", parsed["markdown"], file_name="documentation.md")

                if fmt_html and "html" in parsed:
                    st.subheader("HTML Documentation")
                    st.download_button("⬇ Download .html", parsed["html"], file_name="documentation.html")
                    st.components.v1.html(parsed["html"], height=400, scrolling=True)

            except Exception as e:
                st.error(f"Something went wrong: {e}")