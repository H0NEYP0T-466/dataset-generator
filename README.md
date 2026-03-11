<h1>dataset-generator</h1>
<p>
  <strong><strong>Generates LLM fine-tuning datasets with real-time pipeline tracking</strong></strong>
</p>
<p>
  <em><em>An AI-powered platform that transforms prompts into structured training data through an interactive, multi-stage pipeline.</em></em>
</p>
<p>

  <img src="https://img.shields.io/github/license/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=brightgreen">
  <img src="https://img.shields.io/github/stars/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=yellow">
  <img src="https://img.shields.io/github/forks/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=blue">
  <img src="https://img.shields.io/github/issues/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=red">
  <img src="https://img.shields.io/github/issues-pr/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=orange">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge">

  <img src="https://img.shields.io/github/last-commit/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=purple">
  <img src="https://img.shields.io/github/commit-activity/m/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=teal">
  <img src="https://img.shields.io/github/repo-size/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=blueviolet">
  <img src="https://img.shields.io/github/languages/code-size/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=indigo">

  <img src="https://img.shields.io/github/languages/top/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=critical">
  <img src="https://img.shields.io/github/languages/count/H0NEYP0T-466/dataset-generator?style=for-the-badge&amp;color=success">

  <img src="https://img.shields.io/badge/Docs-Available-green?style=for-the-badge&amp;logo=readthedocs&amp;logoColor=white">
  <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge">

</p>

---

## 🔗 Quick Links

- <a href="#abstract">📄 Abstract</a>
- <a href="#key-highlights">✨ Key Highlights</a>
- <a href="#features">✨ Features</a>
- <a href="#tech-stack">🛠 Tech Stack</a>
- <a href="#dependencies-packages">📦 Dependencies & Packages</a>
- <a href="#prerequisites">📋 Prerequisites</a>
- <a href="#installation">⚙️ Installation</a>
- <a href="#quick-start">🚀 Quick Start</a>
- <a href="#usage">💡 Usage</a>
- <a href="#api-endpoints">🌐 API Endpoints</a>
- <a href="#configuration">⚙️ Configuration</a>
- <a href="#environment-variables">🔧 Environment Variables</a>
- <a href="#project-structure">📂 Project Structure</a>
- <a href="#development">🛠️ Development</a>
- <a href="#contributing">🤝 Contributing</a>
- <a href="#code-of-conduct">📜 Code of Conduct</a>

---

## 📑 Table of Contents

1. <a href="#abstract">Abstract</a>
2. <a href="#key-highlights">Key Highlights</a>
3. <a href="#features">Features</a>
4. <a href="#tech-stack">Tech Stack</a>
5. <a href="#dependencies-packages">Dependencies & Packages</a>
6. <a href="#prerequisites">Prerequisites</a>
7. <a href="#installation">Installation</a>
8. <a href="#quick-start">Quick Start</a>
9. <a href="#usage">Usage</a>
10. <a href="#api-endpoints">API Endpoints</a>
11. <a href="#configuration">Configuration</a>
12. <a href="#environment-variables">Environment Variables</a>
13. <a href="#project-structure">Project Structure</a>
14. <a href="#development">Development</a>
15. <a href="#contributing">Contributing</a>
16. <a href="#code-of-conduct">Code of Conduct</a>

---

## Abstract

DataForge is an intelligent LLM dataset generator that transforms raw user prompts into high-quality, structured training data through a multi-stage AI pipeline. Built with FastAPI and React, it leverages advanced language models to expand prompts, generate diverse scenarios, and create question-answer pairs in ShareGPT format. The system features real-time progress tracking via Server-Sent Events, automatic deduplication using FAISS embeddings, and supports configurable dataset sizes with memory fact integration. With a modern dark-themed UI and modular architecture, DataForge streamlines the creation of fine-tuning datasets while maintaining transparency through live logging and model status monitoring.

## Key Highlights

This project is a **fully-featured LLM dataset generator** built with a modern Python FastAPI backend and a React/TypeScript frontend, enabling automated creation of high-quality training data for machine learning models. 🚀

Key capabilities include real-time **progress tracking** via Server-Sent Events (SSE), intelligent **prompt expansion** using AI agents, and **duplicate detection** through vector embeddings with FAISS. The system supports multiple AI model providers with automatic routing and includes a **collapsible dashboard** for monitoring model status and usage.

Built with a focus on developer experience, the codebase features strict TypeScript configuration, comprehensive ESLint rules, and structured logging throughout. The UI provides an intuitive interface for configuring dataset generation parameters, viewing pipeline stages, and downloading results—all within a sleek dark-themed design optimized for productivity.

The architecture separates concerns cleanly between frontend components (ConfigPanel, PipelineProgress, ModelDashboard) and backend services (agents, dedup, storage, streaming), making it both scalable and maintainable.

## Features

- **Real-time Pipeline Progress Tracking** – Visual progress dashboard showing stage-by-stage completion with live logs and status updates via Server-Sent Events (SSE) 📊
- **Multi-Model AI Orchestration** – Intelligent routing between multiple LLM providers based on availability, usage limits, and performance 🤖
- **Automated Dataset Generation** – End-to-end pipeline that transforms user prompts into structured ShareGPT-format datasets with customizable size and content 🧠
- **Advanced Deduplication System** – Uses FAISS vector search with cosine similarity to detect and eliminate duplicate content using Mistral AI embeddings 🔍
- **Interactive Configuration Interface** – Web-based UI for setting dataset parameters including prompt expansion, memory facts, size limits, and deduplication toggle ⚙️
- **Live Model Dashboard** – Real-time monitoring of model usage, status badges, and availability with automatic refresh during generation 🖥️
- **Secure File Management** – Structured storage system for saving generated datasets in JSON/JSONL formats with logging and directory management 💾
- **Responsive Dark Theme UI** – Modern React interface with monospace typography, neon accents, and mobile-friendly design optimized for data workflows 🎨

## Tech Stack

The DataForge LLM Dataset Generator leverages a modern, full-stack tech stack designed for scalability and real-time interactivity.

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
</p>

<p>
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/Uvicorn-FFD43B?style=for-the-badge&logo=gunicorn&logoColor=black" alt="Uvicorn">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js">
</p>

Built with **FastAPI** for high-performance backend APIs and **React + TypeScript** for a responsive frontend, the system uses **Vite** for fast development builds. Real-time updates are powered by **Server-Sent Events (SSE)**. The backend is written in Python with async support, while the frontend uses modern React patterns with ESLint and strict TypeScript configuration.

## Dependencies & Packages

The project relies on a well-defined set of dependencies for both frontend and backend functionality:

**Backend (Python)** – Powered by **FastAPI** with **Uvicorn**, the core framework for building the dataset generation API. It uses **FAISS** for vector-based deduplication, **Mistral AI** for embedding generation, and integrates multiple LLM providers through configurable routing. Real-time progress tracking is handled via **Server-Sent Events (SSE)**, while structured logging is managed through a custom logger setup. Data persistence is supported via file operations, and all dependencies are listed in `backend/requirements.txt`.

**Frontend (TypeScript/React)** – Built with **Vite** as the build tool and **React 18** using modern hooks and `createRoot`. The UI leverages **ESLint** with React Refresh for development efficiency, styled with custom CSS, and communicates with the backend via REST and SSE APIs. All frontend packages are defined in `package.json` and locked in `package-lock.json`.

This separation ensures clean architecture, scalability, and maintainability across both layers.

## Prerequisites

Before setting up the **DataForge** LLM dataset generator, ensure your environment meets these technical requirements:

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
</p>

You'll need:
- **Python 3.10+** for the backend FastAPI server and ML agents
- **Node.js 18+** and **npm** for the React frontend build system
- **TypeScript** support enabled in your editor or IDE
- A working internet connection to install dependencies and access external APIs (like Mistral AI)

The project uses a virtual environment for Python packages and Vite for frontend bundling. Ensure you have standard development tools like `git` and a terminal with proper PATH configuration.

## Installation

To set up the DataForge LLM Dataset Generator locally, follow these steps:

1. **Clone the repository** and navigate into the project directory:
   ```bash
   git clone https://github.com/H0NEYP0T-466/dataset-generator.git
   cd dataset-generator
   ```

2. **Install backend dependencies** using pip:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Set up the frontend** by installing Node.js packages:
   ```bash
   npm install
   ```

4. **Configure environment variables** as needed (see `backend/config.py` for reference).

5. **Start the development server** with:
   ```bash
   npm run dev
   ```

The application runs on port 8005 (backend) and uses Vite for frontend hot-reloading. Ensure Python 3.9+ and Node.js 18+ are installed before proceeding.

## Quick Start

Get your dataset generation pipeline running in minutes with this streamlined setup:

**1. Launch the Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8005
```

**2. Start the Frontend**
```bash
npm install
npm run dev
```

**3. Configure & Generate**
- Visit `http://localhost:5173` (Vite default)
- Enter your prompt and memory facts in the config panel
- Set dataset size and enable/disable deduplication
- Click "Start Generation" to begin the multi-stage pipeline

The system will automatically:
- Expand your prompt into detailed briefs
- Generate diverse scenarios using multiple AI models
- Create question-answer pairs in ShareGPT format
- Stream real-time progress via Server-Sent Events (SSE)
- Detect duplicates using FAISS vector similarity
- Provide download link when complete

Monitor live progress, model switching, and logs through the intuitive dashboard interface.

## Usage

Start the application by running the backend server and frontend development environment. Use the provided commands in `backend/run_commands.txt` to activate the virtual environment and launch the FastAPI server with Uvicorn on port 8005. The React frontend, built with Vite, will automatically proxy API requests from `/api` to the backend.

Once running, open your browser to access the DataForge interface at `http://localhost:5173`. Configure your dataset generation parameters using the intuitive form in the **ConfigPanel**, including your prompt, memory facts, desired dataset size, and deduplication settings. Click **Start Generation** to begin the multi-stage pipeline.

Monitor real-time progress through the **PipelineProgress** component, which displays stage-by-stage completion, live logs, and model switching notifications via Server-Sent Events (SSE). When complete, download your generated dataset through the **DownloadSection**, which provides metadata and a direct download link.

The system supports asynchronous processing with automatic status tracking and includes a collapsible **ModelDashboard** showing current model usage and availability. All interactions are handled through the RESTful API endpoints exposed by the FastAPI backend.

## API Endpoints

The DataForge backend exposes several key API endpoints through its FastAPI application running on port 8005. These endpoints enable full control over the dataset generation pipeline:

- **Start Generation** (`POST /start`): Initiates a new dataset generation job with user-provided prompts, memory facts, and configuration parameters
- **Check Status** (`GET /status`): Returns current pipeline status, progress percentage, and stage information for active jobs
- **SSE Stream** (`GET /events`): Provides real-time Server-Sent Events stream for live progress updates, model switches, and log messages
- **Download Dataset** (`GET /download`): Allows downloading completed datasets in JSONL format with metadata
- **Reset System** (`POST /reset`): Clears all active jobs and resets the generation state

All endpoints support structured request/response formats defined in `src/types.ts`, with error handling and validation built into the FastAPI routes. The frontend uses these endpoints via the `/api` proxy configured in Vite to interact with the backend services.

## Configuration

The project provides several configuration options through environment variables and file-based settings to customize the dataset generation process.

**Backend Configuration**: The `backend/config.py` file defines settings for multiple LLM providers, including API keys, base URLs, and model-specific rate limits. This allows you to configure which AI models are available and their usage parameters.

**Frontend Configuration**: The Vite build tool is configured in `vite.config.ts` with a development server proxy that forwards `/api` requests to `http://localhost:8005`, enabling seamless communication between the React frontend and FastAPI backend during development.

**Logging Setup**: Custom logging configuration is implemented in `backend/logger/setup.py`, providing colored, structured log output with predefined levels and formatting for better debugging and monitoring.

**TypeScript Configuration**: Strict compilation settings are defined in both `tsconfig.app.json` (for React) and `tsconfig.node.json` (for Node.js), ensuring type safety across the full stack.

These configurations work together to provide a flexible, production-ready setup for generating LLM datasets with real-time progress tracking and multi-model support.

## Environment Variables

This project relies on environment variables to securely configure external services and API keys. The backend expects specific environment variables to be set for LLM provider authentication and system configuration.

**Required Environment Variables:**
- `OPENAI_API_KEY` — Your OpenAI API key for GPT model access
- `MISTRAL_API_KEY` — Your Mistral AI API key for embedding generation
- `DATASET_STORAGE_PATH` — Directory path for storing generated datasets (defaults to `./datasets`)
- `LOG_LEVEL` — Logging verbosity level (`DEBUG`, `INFO`, `WARNING`, `ERROR`)

⚠️ **Important Notes:**
- This project does **not** use dotenv or similar libraries to load `.env` files automatically
- All environment variables must be set in your shell or deployment environment before starting the application
- Never commit API keys or sensitive values to version control

Example setup in bash:
```bash
export OPENAI_API_KEY="sk-your-openai-key"
export MISTRAL_API_KEY="your-mistral-api-key"
export LOG_LEVEL="INFO"
```

Refer to each provider's official documentation to obtain valid API credentials.

## Project Structure

The project follows a **monorepo** structure with clear separation between frontend and backend components:

- **Frontend (`src/`)**: Built with React 18, TypeScript, and Vite. Contains UI components for configuration, progress tracking, model dashboard, and dataset download functionality.
- **Backend (`backend/`)**: FastAPI application handling LLM dataset generation pipeline with multiple agent stages including prompt expansion, scenario generation, and data synthesis.
- **Configuration**: TypeScript configurations split for app (`tsconfig.app.json`) and Node.js (`tsconfig.node.json`) environments.
- **Storage & Deduplication**: FAISS-based vector store for duplicate detection and file management system for dataset persistence.
- **Real-time Communication**: SSE manager for streaming progress updates and live logging to the frontend.

The architecture enables modular development with dedicated agents for each pipeline stage, real-time monitoring capabilities, and a responsive React interface for dataset generation control.

## Development

The project follows a modern full-stack architecture with a **FastAPI backend** and a **React frontend**, both powered by TypeScript. The backend runs on port 8005 using Uvicorn with auto-reload, while the frontend uses Vite for fast development and hot module replacement.

To start development:

```bash
# Install dependencies
npm install
pip install -r backend/requirements.txt

# Start backend (from backend directory)
uvicorn main:app --reload --port 8005

# Start frontend (from root)
npm run dev
```

Key development features include:
- 🔄 Real-time progress tracking via Server-Sent Events (SSE)
- 🧠 Multi-stage AI pipeline with prompt expansion, scenario generation, and dataset synthesis
- 🎯 FAISS-based deduplication using vector embeddings
- 📊 Live model dashboard showing usage and status
- ⚙️ Configurable LLM routing with fallback mechanisms

The codebase enforces strict type safety with TypeScript across both frontend and backend, and uses ESLint with React Refresh for consistent code quality during development.

## Contributing

We welcome contributions to the **DataForge LLM Dataset Generator**! This project is built with a Python FastAPI backend and a TypeScript React frontend, designed for collaborative development.

To get started:
- **Fork the repository** and create your feature branch from `main`.
- **Backend**: Write Python code following existing patterns in `backend/agents/`, `backend/dedup/`, and `backend/streaming/`. Ensure new packages are added to `backend/requirements.txt`.
- **Frontend**: Develop React components using TypeScript and plain CSS files (e.g., `*.css`). Maintain consistency with dark theming and neon-green accents.
- **Testing**: Preserve real-time functionality—any changes must not break Server-Sent Events (SSE) streaming used throughout the pipeline.
- **Documentation**: Update relevant sections of `CONTRIBUTING.md` or `SUPPORT.md` if introducing new features.

Before submitting a pull request:
- Run ESLint (`npm run lint`) on frontend code.
- Verify TypeScript compilation succeeds (`tsc --noEmit`).
- Test API endpoints locally using the commands in `backend/run_commands.txt`.

Please report bugs via GitHub Issues and discuss major changes through Discussions. See `CODE_OF_CONDUCT.md` for community guidelines.

## Code of Conduct

We are committed to fostering a **respectful, inclusive, and harassment-free** environment for everyone who participates in the DataForge project — whether you're contributing code, reporting bugs, asking questions, or engaging with the community.

This project adheres to the [Contributor Covenant](https://www.contributor-covenant.org/) as outlined in our `CODE_OF_CONDUCT.md` file. All contributors are expected to act professionally and respectfully. This includes:

- 🤝 Being welcoming and open to diverse perspectives  
- 🗣️ Using clear, constructive communication  
- 🛡️ Respecting differing opinions and experiences  
- 🚫 Avoiding discriminatory language or behavior  

Unacceptable behavior such as harassment, trolling, or personal attacks will not be tolerated. Violations may result in moderation, warnings, or removal from the project, depending on severity.

If you experience or witness inappropriate conduct, please report it immediately via GitHub Issues or contact the maintainers directly. All reports will be handled confidentially and promptly.

Let’s build great datasets — together, with kindness.

---

<p align="center">Made with ❤️ by <a href="https://github.com/H0NEYP0T-466">H0NEYP0T-466</a></p>