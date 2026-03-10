# Getting Support for H0NEYP0T-466/dataset-generator

Welcome to the **DataForge — LLM Dataset Generator** project! We're excited you're here and want to get help. This guide will walk you through how to ask for support effectively so we can assist you quickly and efficiently.

---

## 🛠️ What Is This Project?

**DataForge** is a powerful tool that automates the creation of high-quality fine-tuning datasets for Large Language Models (LLMs). It uses AI agents, real-time progress tracking, deduplication, and streaming via Server-Sent Events (SSE) to generate structured, diverse, and clean question-answer pairs in ShareGPT format.

Built with:
- **Frontend**: React + Vite + TypeScript
- **Backend**: FastAPI + Uvicorn + FAISS + OpenAI-compatible models
- **Features**: Real-time pipeline monitoring, model switching, deduplication, logging, and more.

---

## 📬 Available Support Channels

We offer several ways to get help:

| Channel | Best For | Link |
|-------|--------|------|
| 🐛 **GitHub Issues** | Bug reports, feature requests, code problems | [Issues Page](https://github.com/H0NEYP0T-466/dataset-generator/issues) |
| 💬 **GitHub Discussions** | General questions, usage tips, community help | [Discussions Page](https://github.com/H0NEYP0T-466/dataset-generator/discussions) |

> ✅ **Recommended First Step**: Start with [GitHub Discussions](https://github.com/H0NEYP0T-466/dataset-generator/discussions) for quick answers or general help. Use [Issues](https://github.com/H0NEYP0T-466/dataset-generator/issues) only when something isn’t working as expected.

---

## 🐛 GitHub Issues: When & How to Use

Use **GitHub Issues** for:

- ❌ **Bugs** (e.g., app crashes, API errors, incorrect output)
- 🚀 **Feature Requests** (new functionality ideas)
- 🔧 **Configuration Problems** (e.g., environment setup, dependency issues)
- 🧪 **Integration Errors** (e.g., model not responding, SSE disconnects)

### ✅ What to Include in an Issue:

1. **Clear Title**: e.g., "Error starting backend: ModuleNotFoundError for 'faiss'"
2. **Description**:
   - What you were trying to do
   - What happened vs. what you expected
3. **Steps to Reproduce**:
   ```bash
   git clone https://github.com/H0NEYP0T-466/dataset-generator.git
   cd dataset-generator
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r backend/requirements.txt
   uvicorn backend.main:app --reload --port 8005
   ```
4. **Logs/Screenshots**: Attach terminal logs, error messages, or screenshots.
5. **Environment Details**:
   - OS (Windows/macOS/Linux)
   - Python version (`python --version`)
   - Node.js & npm versions
   - Browser (if frontend issue)

> 💡 Tip: Run `backend/run_commands.txt` exactly as written to avoid common setup issues.

---

## 💬 GitHub Discussions: Community Help

Use **GitHub Discussions** for:

- ❓ General questions (e.g., "How do I set up memory facts?")
- 📚 Usage examples
- 🤝 Collaboration ideas
- 💡 Feature brainstorming
- 🔍 Debugging help (with context)

👉 Go to: [https://github.com/H0NEYP0T-466/dataset-generator/discussions](https://github.com/H0NEYP0T-466/dataset-generator/discussions)

You can:
- Browse existing topics
- Ask a new question
- Answer others (help builds community!)

---

## 📚 Documentation & Resources

While full docs aren't yet published, here are key resources:

| File | Purpose |
|------|--------|
| `README.md` *(soon)* | Main project overview (check repo root) |
| `backend/config.py` | Model providers, API keys, rate limits |
| `src/types.ts` | Data structures (pipeline stages, status, etc.) |
| `vite.config.ts` | Frontend proxy setup (API calls to port 8005) |
| `backend/run_commands.txt` | How to start backend server |
| `package.json` | Frontend dependencies & scripts |

> 🔗 Always check the latest code in the `main` branch for accurate info.

---

## 🤔 How to Ask a Good Question

To get fast, accurate help:

1. **Be Specific**: Instead of “It doesn’t work,” say “The pipeline fails at stage 2 with ‘No embeddings found’.”
2. **Include Context**: What prompt did you use? What size dataset?
3. **Show Your Effort**: Mention what you’ve already tried.
4. **Use Code Blocks** for logs/configs:
   ```python
   # Example from config.py
   GROQ_API_KEY = os.getenv("GROQ_API_KEY")
   ```
5. **Tag Wisely**: Use labels like `bug`, `frontend`, `backend`, `setup` when opening an issue.

---

## ❌ What NOT to Use Issues For

Avoid creating issues for:

- ❓ General questions (