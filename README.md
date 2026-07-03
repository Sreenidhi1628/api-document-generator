# api-document-generator
AI-powered API documentation generator built with Streamlit and Groq's LLaMA 3.3 70B model — turns code into clear, structured API docs.

# 📄 API Documentation Generator

An AI-powered tool that automatically generates clear, structured API documentation from code, using Groq's LLaMA 3.3 70B model for fast, high-quality generation.

## Features
- Generates structured API documentation from source code
- Powered by Groq API (LLaMA 3.3 70B Versatile) for fast inference
- Simple, interactive Streamlit interface
- Supports pasting or uploading code directly

## Tech Stack
- **Backend/Frontend:** Streamlit
- **AI/LLM:** Groq API (`llama-3.3-70b-versatile`)
- **Language:** Python

## How It Works
1. User pastes or uploads their code/API endpoint definitions
2. The code is sent to Groq's LLaMA 3.3 70B model with a documentation-generation prompt
3. The app returns clean, structured documentation (endpoints, parameters, descriptions, examples)

## Setup
\`\`\`bash
git clone https://github.com/Sreenidhi1628/api-doc-generator.git
cd api-doc-generator
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## Environment Variables
Create a `.env` file in the root folder with your Groq API key:
\`\`\`
GROQ_API_KEY=your_api_key_here
\`\`\`

## Live Demo
🔗 [Add your deployed Streamlit app link here]

## Future Improvements
- Support for multiple programming languages
- Export documentation as Markdown/PDF
- Auto-detect API framework (Flask, FastAPI, Express, etc.)
