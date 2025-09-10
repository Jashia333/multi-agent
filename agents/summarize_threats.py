import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a lower-quota model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def summarize_threats(threat_report: list[dict]) -> str:
    try:
        summary_input = "Summarize the following cyber security incidents:\n\n"
        for item in threat_report:
            summary_input += f"- {item['text']}\n"

        # Optional truncation for safety
        summary_input = summary_input[:5000]

        response = model.generate_content(summary_input)
        return response.text.strip()
    except Exception as e:
        return f"[Summarization failed] {str(e)}"
