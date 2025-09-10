import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Import functions
from agents.fetch_news import fetch_news
from agents.analyze_threats import analyze_threats
from agents.summarize_threats import summarize_threats

# MCP setup
mcp = FastMCP("CyberSec Threat Analyzer")

@mcp.tool()
def fetch_news_tool(ctx: Context) -> list[str]:
    return fetch_news()

@mcp.tool()
def analyze_threats_tool(news_list: list[str], ctx: Context) -> list[dict]:
    return analyze_threats(news_list)

# Mount MCP
mcp_app = mcp.http_app(path="/mcp")

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with mcp_app.lifespan(app):
        yield

app = FastAPI(title="CyberSec API + MCP", lifespan=lifespan)
app.mount("/mcp", mcp_app)

# Direct REST endpoints
@app.get("/fetch-news")
def fetch_news_api():
    return fetch_news()

@app.post("/analyze-threats")
def analyze_threats_api(news_list: list[str]):
    return analyze_threats(news_list)

@app.get("/run")
def run_chain():
    news = fetch_news()
    report = analyze_threats(news)
    summary = summarize_threats(report)
    return JSONResponse(content={
        "news": news,
        "report": report,
        "summary": summary
    })
