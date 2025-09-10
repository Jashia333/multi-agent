# 🛡️ CyberSec Threat Analyzer (MCP + FastAPI)

This project is a lightweight **Multi-Agent Cyber Threat Analyzer** built with:
- **FastAPI** for API serving
- **FastMCP** for agent workflows (Model Context Protocol)
- **Google Gemini API** for summarization
- **RSS Feeds** for real-time threat aggregation

---

## 🚀 Features

- ✅ **Fetch Cybersecurity News** (Google News RSS)
- ✅ **Detect Threats** using regex + keyword analysis
- ✅ **Optional LLM-based Summarization** via Gemini
- ✅ **MCP Agent Chaining**: Fetch → Analyze → Summarize
- ✅ **FastAPI REST Endpoints** and MCP workflow exposed

---

## 🧠 MCP Agent Structure

### 1. `fetch_news_tool`
- Tool registered with `@mcp.tool()`
- Pulls top 5 headlines from Google News RSS

### 2. `analyze_threats_tool`
- Scans news for CVE patterns (e.g., `CVE-2023-XXXXX`)
- Identifies threat keywords: `vulnerability`, `exploit`, etc.

### 3. `summarize_threats_tool`
- Uses Google Gemini to summarize threat reports

---

## 🧪 Example Endpoints

| Endpoint                  | Method | Description                          |
|--------------------------|--------|--------------------------------------|
| `/fetch-news`            | GET    | Returns latest top 5 cybersecurity headlines |
| `/analyze-threats`       | POST   | Accepts news list, returns threat report |
| `/run`                   | GET    | Runs chained: fetch → analyze        |
| `/mcp/...`               | ANY    | FastMCP-powered tool execution       |

---

## 📂 File Structure

```
multi-agent/
├── agents/
│   ├── fetch_news.py         # RSS fetch logic
│   ├── analyze_threats.py    # Regex-based CVE/threat parsing
│   └── summarize_threats.py  # LLM-based summarizer (optional)
├── run_mcp.py                # FastAPI + FastMCP integrated app
├── .env                      # Contains GEMINI_API_KEY
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

```bash
git clone https://github.com/yourname/multi-agent-threat-analyzer
cd multi-agent-threat-analyzer

python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file with your Google API Key:

```
GEMINI_API_KEY=your-key-here
```

---

## ✅ Run the API

```bash
uvicorn run_mcp:app --reload
```

Then open your browser:
- 🔗 http://localhost:8000/docs — Swagger UI

---

## 📌 Notes

- Be aware of Gemini’s **quota limits** on free tier (rate-limited)
- You can list models using the Gemini SDK (`genai.list_models()`)
- Use `summarize_threats_tool` only when needed to save quota

---

## 🧠 Credits

- Built using [FastMCP](https://gofastmcp.com/)
- Google Gemini API by Google AI
- RSS Feed from Google News

---

## 📜 License

MIT License © 2025 Maahir Mitayeegiri
