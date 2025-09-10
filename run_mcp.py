import os
from fastmcp import FastMCP, Context
from dotenv import load_dotenv
import google.generativeai as genai

from agents.fetch_news import fetch_news
from agents.analyze_threats import analyze_threats

# Load Gemini key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create server
mcp = FastMCP("cybersec-mcp")

@mcp.tool()
def fetch_news_tool(ctx: Context) -> list[str]:
    return fetch_news()

@mcp.tool()
def analyze_threats_tool(news_list: list[str], ctx: Context) -> list[dict]:
    return analyze_threats(news_list)

@mcp.tool()
async def run_news_summary(ctx: Context) -> str:
    news_list = fetch_news()
    threats = analyze_threats(news_list)

    prompt = "Summarize the following cybersecurity threats:\n"
    for item in threats:
        prompt += f"\n- {item['text']}\nCVEs: {item['cves']}\nKeywords: {item['keywords']}\n"

    result = await ctx.sample(prompt, model="gemini-pro")
    return result.text.strip()

if __name__ == "__main__":
    mcp.run()  # 🔥 Do not pass flow_path here!
