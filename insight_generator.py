import pandas as pd
from groq import Groq
import streamlit as st

def generate_insights(file_path):
    data = pd.read_csv(file_path)
    prompt = f"Here is a summary of the dataset:\n{data.describe()}. Provide key insights from this summary."
    client = Groq(api_key=st.secrets['GROQ_API_KEY'])
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    output = ""

    for chunk in completion:
        output+=chunk.choices[0].delta.content or ""
    
    return output