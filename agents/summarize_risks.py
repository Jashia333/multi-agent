import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")  # or "gemini-1.5", etc.    

def summarize_risks(news):
    prompt = f"Summarize the cybersecurity risks mentioned in the following news articles:\n\n{news}\n\nProvide a concise summary highlighting key threats and vulnerabilities."
    for a in news:
        prompt += f"\n- 
        {a["text"]}\n 
        CVEs: {a['cves']}\n 
        Keywords: {a['keywords']}"

        response = model.generate_content(prompt)
        return response.text.strip()