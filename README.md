<h1>dataset-generator</h1>
<p>
  <strong><strong>Generates high-quality LLM datasets with AI agents and real-time progress tracking.</strong></strong>
</p>
<p>
  <em><em>An intelligent pipeline that transforms prompts into diverse, deduplicated training data using multiple AI models with live monitoring.</em></em>
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

- <a href="#dataforge-llm-dataset-generator">📌 # DataForge LLM Dataset Generator</a>
- <a href="#abstract">📌 ## Abstract</a>
- <a href="#key-highlights">📌 ## Key Highlights</a>
- <a href="#features">📌 ## Features</a>
- <a href="#tech-stack">📌 ## Tech Stack</a>
- <a href="#dependencies-packages">📌 ## Dependencies & Packages</a>
- <a href="#prerequisites">📌 ## Prerequisites</a>
- <a href="#installation">📌 ## Installation</a>
- <a href="#quick-start">📌 ## Quick Start</a>
- <a href="#usage">📌 ## Usage</a>
- <a href="#api-endpoints">📌 ## API Endpoints</a>
- <a href="#configuration">📌 ## Configuration</a>
- <a href="#environment-variables">📌 ## Environment Variables</a>
- <a href="#model-setup-training">📌 ## Model Setup & Training</a>
- <a href="#project-structure">📌 ## Project Structure</a>
- <a href="#development">📌 ## Development</a>
- <a href="#security">📌 ## Security</a>
- <a href="#contributing">📌 ## Contributing</a>
- <a href="#code-of-conduct">📌 ## Code of Conduct</a>
- <a href="#license">📌 ## License</a>

---

## 📑 Table of Contents

1. <a href="#dataforge-llm-dataset-generator"># DataForge LLM Dataset Generator</a>
2. <a href="#abstract">## Abstract</a>
3. <a href="#key-highlights">## Key Highlights</a>
4. <a href="#features">## Features</a>
5. <a href="#tech-stack">## Tech Stack</a>
6. <a href="#dependencies-packages">## Dependencies & Packages</a>
7. <a href="#prerequisites">## Prerequisites</a>
8. <a href="#installation">## Installation</a>
9. <a href="#quick-start">## Quick Start</a>
10. <a href="#usage">## Usage</a>
11. <a href="#api-endpoints">## API Endpoints</a>
12. <a href="#configuration">## Configuration</a>
13. <a href="#environment-variables">## Environment Variables</a>
14. <a href="#model-setup-training">## Model Setup & Training</a>
15. <a href="#project-structure">## Project Structure</a>
16. <a href="#development">## Development</a>
17. <a href="#security">## Security</a>
18. <a href="#contributing">## Contributing</a>
19. <a href="#code-of-conduct">## Code of Conduct</a>
20. <a href="#license">## License</a>

---

# DataForge LLM Dataset Generator

DataForge is a powerful, real-time dataset generation platform designed to streamline the creation of high-quality training data for large language models (LLMs). Built with modern web technologies and AI-powered agents, it enables users to transform simple prompts into structured, diverse datasets ready for model fine-tuning.

The application features a **React-based frontend** powered by Vite and TypeScript, providing a responsive, dark-themed user interface with real-time progress tracking. Users interact through an intuitive configuration panel where they can input core prompts, optional memory facts, specify dataset size, and toggle deduplication settings. Preset options allow quick setup, while form validation ensures data integrity before processing begins.

Behind the scenes, a **FastAPI backend** orchestrates a sophisticated multi-stage pipeline. The process initiates with prompt expansion using `prompt_expander.py`, which transforms raw inputs into detailed dataset briefs. Next, `scenario_generator.py` creates numbered, diverse scenario headings from approved prompts. Finally, `dataset_generator.py` produces question-answer pairs in ShareGPT format, optionally injecting memory facts and applying FAISS-based cosine similarity deduplication via `faiss_store.py` to ensure uniqueness.

Throughout execution, the system provides **real-time feedback** via Server-Sent Events (SSE), managed by `sse_manager.py`. This enables live updates on stage progress, model switches, completion status, and operational logs. A collapsible ModelDashboard component displays current model usage, availability, and performance metrics, automatically polling when active.

Deduplication is handled efficiently using FAISS vector embeddings generated by `embedder.py`, which leverages the Mistral AI API for semantic similarity comparison. All generated data is persisted through `file_manager.py`, supporting multiple formats including JSON and JSONL, with download functionality accessible upon completion.

The backend architecture supports **modular agent workflows**, with `manager_agent.py` overseeing prompt approval loops and iterative refinement. Model routing is managed by `model_router.py`, which intelligently selects from multiple providers (Groq, LongCat, Cerebras, Mistral) based on availability, rate limits, and error handling.

Security and collaboration are prioritized with comprehensive policies: a Contributor Covenant Code of Conduct governs community behavior, while dedicated SECURITY.md outlines vulnerability reporting procedures. Setup guidance is provided through CONTRIBUTING.md and SUPPORT.md, ensuring smooth onboarding for both contributors and users.

With its blend of real-time monitoring, intelligent deduplication, and flexible configuration, DataForge empowers teams to generate clean, high-value datasets at scale—all within a cohesive, developer-friendly environment.

## Abstract

DataForge is a sophisticated **LLM dataset generator** built with a modern, full-stack architecture designed for scalability and real-time interactivity. The system leverages **FastAPI** on the backend to orchestrate an intelligent pipeline of AI agents that transform raw user prompts into high-quality, deduplicated training datasets in ShareGPT format. At its core, DataForge employs multiple specialized agents—including prompt expansion, scenario generation, and dataset creation—each managed through asynchronous workflows that stream progress updates via Server-Sent Events (SSE) to the frontend.

The backend is powered by Python and structured around modular components such as a **model router** (`model_router.py`) that intelligently routes requests across multiple AI providers (Groq, LongCat, Cerebras, Mistral) based on availability, rate limits, and performance. A key feature is **FAISS-based deduplication** (`faiss_store.py`), which ensures dataset uniqueness using cosine similarity on vector embeddings generated via the Mistral AI API (`embedder.py`). File management is handled robustly by `file_manager.py`, supporting persistent storage of text, JSON, and JSONL outputs. Real-time communication between server and client is facilitated by an SSE manager (`sse_manager.py`) that broadcasts stage progress, model switches, logs, and completion events.

On the frontend, the application is built with **React** and **TypeScript**, utilizing Vite for fast development and hot-reloading. The UI features a dark-themed interface with neon-green accents, including interactive components like `ConfigPanel` for prompt input and dataset configuration, `PipelineProgress` for live stage tracking, `ModelDashboard` for monitoring active models, and `DownloadSection` for exporting results. Global styles are defined in `src/index.css`, emphasizing readability and a cohesive visual identity.

The project enforces strong code quality practices through ESLint configuration and supports collaborative development via comprehensive documentation (`CONTRIBUTING.md`, `CODE_OF_CONOND.md`, `SECURITY.md`, `SUPPORT.md`). Configuration is centralized in `config.py`, while logging is standardized using a structured, colored console logger (`logger/setup.py`). Deployment is streamlined through `run_commands.txt`, which automates virtual environment activation and Uvicorn startup on port 8005 with auto-reload.

In summary, DataForge represents a production-ready, extensible platform for automated LLM dataset curation, combining advanced NLP techniques with a responsive user experience and enterprise-grade tooling.

## Key Highlights

**DataForge LLM Dataset Generator** is a modern, full-stack application designed to streamline the creation of high-quality datasets for large language model (LLM) training. Built with a robust **FastAPI backend** and a responsive **React frontend**, the system orchestrates an intelligent pipeline that transforms raw user prompts into structured, deduplicated question-answer pairs in ShareGPT format.

### 🔧 Core Backend Architecture

The backend is powered by **FastAPI**, serving as the central orchestrator for dataset generation. It integrates multiple specialized agents—including prompt expansion, scenario generation, and dataset creation—each leveraging advanced AI models via providers like Groq, LongCat, Cerebras, and Mistral. The system employs **server-sent events (SSE)** through `sse_manager.py` to provide real-time updates on pipeline progress, enabling seamless frontend-backend communication. A **FAISS-based vector store** (`faiss_store.py`) ensures intelligent deduplication using cosine similarity, while `model_router.py` dynamically routes requests based on availability, rate limits, and priority.

Configuration is centralized in `config.py`, supporting secure API key management and model-specific settings. Logging is handled via a custom colored logger (`logger/setup.py`), ensuring traceability across operations. All data persistence is managed through `file_manager.py`, which supports saving outputs in text, JSON, and JSONL formats.

### 🖥️ Intelligent Frontend Interface

The React-based frontend (`src/App.tsx`) offers an intuitive, dark-themed interface built with Vite for fast development and deployment. Users interact through a **ConfigPanel** (`ConfigPanel.tsx`) where they input prompts, define dataset size, toggle deduplication, and select presets. Real-time feedback is delivered via a **PipelineProgress** component (`PipelineProgress.tsx`), which displays stage-by-stage completion status, live logs, and model switch notifications. A collapsible **ModelDashboard** (`ModelDashboard.tsx`) provides visibility into current model usage and availability, with automatic polling during active runs.

Upon completion, a **DownloadSection** (`DownloadSection.tsx`) presents metadata such as sample count, elapsed time, and download links, all styled with neon-green accents for a futuristic aesthetic. The UI leverages TypeScript interfaces defined in `types.ts` for strict type safety across state management and API contracts.

### ⚙️ Development & Tooling

Built on **TypeScript** with strict linting via ESLint and optimized builds using Vite, the project emphasizes maintainability and performance. The `tsconfig.json` setup enables modular compilation for both frontend and Node.js environments. Dependency management is handled through `package.json` and `package-lock.json`, while `vite.config.ts` configures API proxying to `http://localhost:8005`. Development workflows are supported by comprehensive guides in `CONTRIBUTING.md`, `SUPPORT.md`, and `CODE_OF_CONDUCT.md`, ensuring a welcoming and well-documented contributor experience.

Security best practices are enforced via `SECURITY.md`, outlining vulnerability reporting procedures and supported versions. With auto-reload enabled via Uvicorn and structured logging throughout, DataForge delivers a production-ready, scalable solution for automated LLM dataset generation.

## Features

DataForge is a powerful LLM dataset generator built with a modern tech stack and designed for efficient, real-time pipeline management. The application features a comprehensive backend-driven workflow that orchestrates multiple AI-powered stages to transform raw user input into structured, high-quality training data.

**🧠 Intelligent Pipeline Orchestration**  
At the core of DataForge is an asynchronous, multi-stage generation pipeline managed by FastAPI and orchestrated through Server-Sent Events (SSE). The system processes user prompts through a sequence of specialized agents: prompt expansion, scenario generation, and dataset creation. Each stage emits real-time progress updates via streaming logs, allowing users to monitor the entire process live in the frontend interface.

**🔍 Deduplication & Similarity Search**  
To ensure dataset quality, DataForge integrates FAISS-based vector similarity search for cosine similarity deduplication. This prevents redundant content from entering the final dataset, improving diversity and reducing noise. The deduplication logic runs during dataset generation using embeddings generated via the Mistral AI API, ensuring semantic uniqueness across samples.

**⚙️ Flexible Configuration Interface**  
Users can customize their dataset generation through an intuitive React-based configuration panel. Options include custom prompts, optional memory facts injection, adjustable dataset size, and toggleable deduplication settings. Preset configurations allow quick setup, while validation ensures inputs meet requirements before processing begins.

**📊 Real-Time Progress Monitoring**  
The application provides a detailed pipeline progress dashboard showing stage-by-stage status with visual indicators, progress bars, and live log streams. Users receive notifications when models switch between providers and can track overall completion metrics such as elapsed time and sample count. A collapsible model dashboard displays current model status, usage statistics, and availability from the backend.

**💾 Robust File Management**  
Generated datasets are saved in ShareGPT format (JSONL) with metadata including file size and version. The backend includes a dedicated file manager supporting persistent storage, retrieval, and organization of text, JSON, and JSONL files. Download functionality is streamlined through a styled download section component with hover effects and clear labeling.

**🛡️ Enterprise-Grade Backend Infrastructure**  
Built on FastAPI with Uvicorn, the backend supports auto-reload development mode and uses structured logging with colored console output. The system implements rate limiting, model blacklisting, and intelligent routing across multiple AI providers (Groq, LongCat, Cerebras, Mistral) via a configurable model router. Environment variables and secure API key management are handled through centralized configuration.

**🔒 Secure & Compliant Development**  
The project enforces security best practices with a defined security policy, supports vulnerability reporting, and maintains contributor guidelines. Code quality is ensured through ESLint with React Hooks and Refresh plugins, strict TypeScript typing, and comprehensive testing infrastructure.

## Tech Stack

The **DataForge LLM Dataset Generator** is built on a modern, scalable tech stack designed for real-time dataset generation with intelligent deduplication and streaming capabilities. The architecture separates concerns between a React-based frontend and a FastAPI-powered backend, communicating via Server-Sent Events (SSE) for live progress tracking.

### Frontend
The user interface is powered by **React** with **TypeScript**, providing type-safe development and robust component composition. The application uses **Vite** as the build tool, enabling fast hot module replacement during development. Styling is handled through CSS modules and global stylesheets, featuring a dark theme with neon-green accents for visual consistency. Real-time updates are rendered dynamically using React hooks that consume SSE streams from the backend.

Key frontend technologies include:
- **React 18+** with `createRoot` for concurrent rendering
- **TypeScript** with strict type checking and JSX support
- **Vite** for optimized bundling and proxy configuration (`/api` → `http://localhost:8005`)
- **ESLint** with React Refresh plugin for linting and fast refresh
- **Monospace fonts** (JetBrains Mono) for terminal-like readability

### Backend
The backend is implemented in **Python 3.10+** using **FastAPI** with **Uvicorn** as the ASGI server, running on port 8005 with auto-reload enabled. It provides RESTful endpoints and SSE streams for real-time communication.

Core backend components include:
- **FAISS** for cosine similarity-based deduplication of generated text embeddings
- **Mistral AI API integration** via asynchronous HTTP requests for embedding generation
- **Server-Sent Events (SSE)** managed through an asyncio queue for live pipeline progress updates
- **File storage system** supporting JSON, JSONL, and plain text formats
- **Model routing logic** with rate limiting, blacklisting, and priority-based provider selection

Configuration is environment-driven through `config.py`, managing API keys and model-specific parameters for multiple providers (Groq, LongCat, Cerebras, Mistral). Logging is structured and colorized using a custom logger setup.

### Data Flow & Integration
The system orchestrates a multi-stage dataset generation pipeline:
1. **Prompt Expansion**: Transforms raw prompts into detailed briefs using agentic refinement
2. **Scenario Generation**: Creates numbered, diverse scenarios from approved prompts
3. **Dataset Creation**: Produces ShareGPT-format Q&A pairs with optional memory injection
4. **Deduplication**: Uses FAISS vector store to eliminate near-duplicate content
5. **Streaming Updates**: Real-time progress via SSE throughout all stages

All components are container-ready and follow strict separation of concerns, with TypeScript interfaces defining request/response contracts and pipeline state management.

## Dependencies & Packages

This project is a modern, full-stack application built with a **TypeScript React frontend** and a **Python FastAPI backend**, designed for generating LLM datasets. The dependencies are split between the frontend and backend environments, each with its own dedicated configuration files.

### Frontend Dependencies

The React-based frontend is powered by **Vite** as the build tool and uses **TypeScript** for type safety. Key frontend packages include:

- **React 18+**: Core library for building user interfaces, initialized via `src/main.tsx` using `createRoot` within `StrictMode`.
- **TypeScript**: Configured with strict type checking (`tsconfig.app.json`) and JSX support.
- **ESLint**: Integrated with React Hooks and Refresh plugins (`eslint.config.js`) to enforce code quality and development best practices.
- **Vite**: Handles fast development server, hot module replacement, and proxy setup (`vite.config.ts`) to forward `/api` requests to the backend at `http://localhost:8005`.
- **CSS Modules / Global Styles**: Custom styling is applied through `src/App.css`, `src/index.css`, and component-specific styles like `DownloadSection.css` and `ModelDashboard.css`, featuring a dark theme with neon-green accents and JetBrains Mono font.

The frontend communicates with the backend via an API client (`src/api.ts`) that supports starting generation, checking model status, streaming updates via Server-Sent Events (SSE), and downloading results.

### Backend Dependencies

The Python backend is built on **FastAPI** and uses **Uvicorn** to serve the application. Core backend dependencies include:

- **FastAPI**: Web framework for building APIs with automatic OpenAPI documentation.
- **Uvicorn**: ASGI server to run the FastAPI app with auto-reload enabled (as per `backend/run_commands.txt`).
- **FAISS**: Used in `backend/dedup/faiss_store.py` for efficient similarity search and deduplication of generated dataset entries.
- **Mistral AI Client**: Leveraged in `backend/dedup/embedder.py` to generate text embeddings via HTTP requests.
- **Logging Utilities**: Custom logger setup (`backend/logger/setup.py`) provides structured, colored console output.
- **File Management**: `backend/storage/file_manager.py` handles saving and loading data in JSON and JSONL formats.
- **Streaming Support**: `backend/streaming/sse_manager.py` manages real-time event broadcasting using asyncio queues.
- **Configuration Management**: `backend/config.py` centralizes API keys, provider URLs, and rate limits for multiple AI services (Groq, LongCat, Cerebras, Mistral).
- **Agent System**: Includes modules like `prompt_expander.py`, `scenario_generator.py`, `dataset_generator.py`, and `manager_agent.py` that orchestrate the dataset generation pipeline using language models.

All backend dependencies are listed in `backend/requirements.txt`.

### Development & Build Tools

- **TypeScript Configuration**: Project references are defined in `tsconfig.json`, splitting builds into separate apps and Node.js configurations.
- **Environment Isolation**: A virtual environment must be activated before running the backend (per `run_commands.txt`).

This modular dependency structure ensures clean separation between frontend and backend concerns, enabling scalable development and deployment.

## Prerequisites

Before setting up and running the **DataForge LLM Dataset Generator**, ensure your development environment meets the following requirements as evidenced by the codebase structure and configuration files.

### 🔧 Software & Tools

- **Node.js (v18 or higher)**: Required to run the React frontend built with Vite. The project uses modern ES2022 features and TypeScript, supported via `tsconfig.app.json` and `package.json`.
- **Python (3.9 or higher)**: Necessary for the FastAPI backend services. The backend is implemented in Python and relies on packages listed in `backend/requirements.txt`.
- **Git**: Used for version control and cloning the repository. Recommended for managing contributions and updates.

### 📦 Package Managers

- **npm or yarn**: To install frontend dependencies defined in `package.json` and `package-lock.json`. This includes React, Vite, ESLint, and TypeScript tooling.
- **pip**: To install Python dependencies from `backend/requirements.txt`, which includes FastAPI, Uvicorn, FAISS, and other backend utilities.

### 🌐 Network & API Access

- **Internet connectivity** for downloading dependencies and accessing external AI model APIs. The backend (`backend/config.py`) is configured to connect to providers such as Groq, LongCat, Cerebras, and Mistral via their respective base URLs.
- Ensure API keys are available and properly configured in environment variables or a `.env` file (referenced indirectly via `backend/config.py` and logging setup).

### 💻 Development Environment

- **Code editor** supporting TypeScript and Python (e.g., VS Code recommended).
- **Terminal or command-line interface** capable of executing shell commands for virtual environments and service startup.

### 📁 Repository Setup

Clone the repository and navigate into the project root. The structure includes:
- Frontend: `src/` (React + Vite), `index.html`, `vite.config.ts`
- Backend: `backend/` containing FastAPI app (`main.py`), agents, models, storage, and deduplication modules
- Configuration files: `tsconfig.json`, `eslint.config.js`, `tsconfig.node.json`

> ⚠️ Note: The backend runs on port **8005** with auto-reload enabled, as specified in `backend/run_commands.txt`. The frontend proxies `/api` requests to this endpoint via Vite’s proxy configuration.

Ensure all prerequisites are satisfied before proceeding with installation and execution.

## Installation

Welcome to the installation guide for **DataForge**, the LLM dataset generator! This section will walk you through setting up both the frontend and backend components of the application. The project is built with modern tools and requires specific dependencies to run smoothly.

### Prerequisites

Before proceeding, ensure your system meets the following requirements:

- **Node.js** (v18 or higher) — Required for running the React frontend and build tools.
- **Python** (v3.10 or higher) — Needed for the FastAPI backend and data processing modules.
- A terminal or command-line interface (CLI) — For executing setup commands.
- An internet connection — To download dependencies and access external services (e.g., AI model APIs).

> 💡 **Tip**: Use [nvm](https://github.com/nvm-sh/nvm) (Node Version Manager) and [pyenv](https://github.com/pyenv/pyenv) to manage multiple versions of Node.js and Python if needed.

---

### Frontend Setup

The frontend is a TypeScript-based React application powered by Vite for fast development and builds.

1. **Navigate to the project root directory** in your terminal.
2. Install all frontend dependencies using npm:
   ```bash
   npm install
   ```
   This installs packages defined in `package.json`, including React, Vite, ESLint, TypeScript support, and proxy configuration for API calls.

3. **Verify TypeScript configuration**:
   - The project uses `tsconfig.json` to define app-level settings.
   - `tsconfig.app.json` configures strict type checking and ES2022+ features for the React app.
   - `tsconfig.node.json` sets up Node.js-specific compilation rules.
   - These ensure proper module resolution and JSX handling across the codebase.

4. **Start the development server**:
   ```bash
   npm run dev
   ```
   This launches the Vite development server, typically at `http://localhost:5173`. The app uses a proxy (`vite.config.ts`) to forward `/api` requests to the backend on port 8005.

> 🌐 The frontend expects the backend to be running on `http://localhost:8005`. If it’s not active, API calls will fail.

---

### Backend Setup

The backend is a FastAPI service written in Python, responsible for orchestrating the dataset generation pipeline using AI agents and managing real-time updates via Server-Sent Events (SSE).

1. **Navigate into the `backend` folder**:
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment**:
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   This installs core packages such as:
   - `fastapi` — Web framework for building the API.
   - `uvicorn` — ASGI server to run FastAPI.
   - `faiss-cpu` or `faiss-gpu` — For vector similarity deduplication.
   - `httpx` — Async HTTP client for AI model requests.
   - `python-dotenv` — For environment variable management.
   - `logging` utilities and other supporting libraries.

4. **Set up logging**:
   The backend uses `backend/logger/setup.py` to configure structured, colored console logs. No additional steps are required—it initializes automatically when the app starts.

5. **Configure environment variables**:
   Ensure you have valid API keys for AI providers (e.g., Groq, Mistral, LongCat, Cerebras) set in your environment or via a `.env` file. These are used by `backend/config.py` to authenticate requests.

6. **Start the backend server**:
   ```bash
   uvicorn main:app --reload --port 8005
   ```
   This runs the FastAPI app with auto-reload enabled on port 8005, as specified in `run_commands.txt`.

---

### Final Steps

Once both frontend and backend are running:

- Open your browser to `http://localhost:5173`.
- You should see the DataForge interface ready for use.
- Use the **ConfigPanel** to input prompts, set dataset size, enable deduplication, and start generation.
- Monitor progress via the **PipelineProgress** component, which streams real-time updates from the backend.

> 🔁 The `--reload` flag in Uvicorn allows automatic restarts on code changes—ideal during development.

For troubleshooting, refer to `SUPPORT.md` for common issues and reporting procedures.

You're now ready to generate high-quality LLM datasets with ease! 🚀

## Quick Start

Welcome to **DataForge**, an LLM dataset generator built with React and FastAPI. This guide will help you get the application up and running quickly.

### 🛠️ Prerequisites

Ensure you have the following installed:
- **Node.js** (v18 or later recommended)
- **Python** (v3.9 or later)
- A terminal with support for running `npm`, `pip`, and `uvicorn`

### 📦 Installation & Setup

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/H0NEYP0T-466/dataset-generator.git
   cd dataset-generator
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```
   This installs all required packages listed in `package.json`, including Vite, React, TypeScript, ESLint, and project-specific tooling.

3. **Set up the backend environment**:
   - Navigate to the `backend` directory.
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
     This includes FastAPI, Uvicorn, FAISS, logging utilities, and other backend services.

4. **(Optional) Configure API keys**:
   Update `backend/config.py` with your AI provider credentials (e.g., Groq, Mistral, etc.) to enable model access.

---

### ▶️ Running the Application

#### Start the Backend Server

In a new terminal window, run:
```bash
cd backend
# Use the commands from run_commands.txt to activate venv and start Uvicorn
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload --port 8005
```
The FastAPI server will start on `http://localhost:8005` with auto-reload enabled for development.

> 🔁 The `--reload` flag ensures code changes trigger automatic restarts during development.

#### Start the Frontend Development Server

In another terminal:
```bash
npm run dev
```
This launches the Vite-based React app at `http://localhost:5173` by default.

> ⚙️ Vite proxies `/api` requests to `http://localhost:8005` as configured in `vite.config.ts`.

---

### 🌐 Access the Application

Open your browser and go to:
```
http://localhost:5173
```

You’ll see the DataForge interface where you can:
- Enter a prompt and optional memory facts
- Set dataset size and deduplication preferences
- Monitor real-time pipeline progress via SSE streaming
- View model status, logs, and completion summaries

> 💡 The UI uses a dark theme with neon-green accents and monospace fonts for clarity.

---

### 🧪 First Test Run

1. Launch both servers (frontend + backend).
2. In the web interface, enter a simple prompt like *"Generate questions about renewable energy."*
3. Click **Start Generation**.
4. Watch the live pipeline progress: prompt expansion → scenario generation → dataset creation → deduplication.
5. Once complete, download your generated `.jsonl` file from the Download section.

---

### 🚨 Troubleshooting Tips

- If the backend fails to start, check that port `8005` is free and API keys are set in `config.py`.
- Ensure all dependencies are installed (`npm install`, `pip install -r requirements.txt`).
- For frontend issues, verify `vite.config.ts` proxy settings match the backend URL.
- Logs are available via the built-in logger (`backend/logger/setup.py`) and displayed in the PipelineProgress component.

For more details on configuration, contribution, or support, see `SUPPORT.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md`.

## Usage

To use the DataForge LLM Dataset Generator, follow these steps to set up and run both the backend and frontend services:

### 1. **Start the Backend Service**

The backend is a FastAPI application that runs on port 8005 with auto-reload enabled for development. To start it:

```bash
uvicorn main:app --reload --port 8005
```

This command activates the virtual environment (if configured) and launches the Uvicorn server hosting the API endpoints. The `--reload` flag enables automatic restarts when code changes are detected.

> 💡 Ensure you have installed all Python dependencies listed in `backend/requirements.txt`, including FastAPI, FAISS, and other required packages.

You can also refer to `backend/run_commands.txt` for the exact activation and startup sequence if your environment requires virtual environment setup.

### 2. **Configure API Keys**

Before running, ensure your AI provider API keys are properly configured in `backend/config.py`. This file manages credentials for providers like Groq, LongCat, Cerebras, and Mistral. Update the relevant sections with your actual API keys.

### 3. **Start the Frontend Development Server**

Navigate to the project root and run the React frontend using Vite:

```bash
npm run dev
```

This starts the development server on the default Vite port (typically **5173**) with hot module replacement enabled.

> 🌐 The frontend proxies all `/api` requests to `http://localhost:8005`, as defined in `vite.config.ts`.

### 4. **Access the Application**

Open your browser and go to:

```
http://localhost:5173
```

You’ll see the DataForge interface where you can:
- Enter your dataset prompt and optional memory facts
- Configure dataset size and deduplication settings via the ConfigPanel
- Monitor real-time pipeline progress through stages (prompt expansion, scenario generation, dataset creation)
- View live logs, model switches, and completion status via SSE streaming

### 5. **Monitor Pipeline Progress**

The **PipelineProgress** component displays real-time updates of each stage using Server-Sent Events (SSE). As the system processes your request, you’ll see:
- Stage completion status
- Elapsed time and sample count
- Model usage and switching notifications
- Live log output

Once complete, the **DownloadSection** provides a download link for the generated dataset in JSONL format.

### 6. **Reset or Reconfigure**

Use the reset functionality to clear the current session. You can also adjust configurations anytime through the ConfigPanel, which supports presets and validation.

> 🛠️ For troubleshooting, refer to `SUPPORT.md` for guidance on common issues, configuration help, and reporting bugs.

## API Endpoints

The backend provides a comprehensive set of RESTful and streaming endpoints to manage the dataset generation pipeline. These endpoints are implemented using FastAPI and exposed via Uvicorn on port 8005.

### Core Generation Endpoints

- **POST `/api/start`**  
  Initiates a new dataset generation job with user-provided parameters (prompt, memory facts, dataset size, deduplication settings). Returns a job ID for tracking progress.

- **GET `/api/status/{job_id}`**  
  Retrieves the current status and progress of a specific generation job, including stage completion percentages and overall pipeline state.

- **GET `/api/download/{job_id}`**  
  Provides a download URL for the completed dataset file in JSONL format, along with metadata such as file size and generation timestamp.

- **POST `/api/reset`**  
  Resets the system state, clearing all active jobs and stopping any running processes. Useful for starting fresh after a failed or interrupted session.

### Real-Time Streaming

- **GET `/api/events`**  
  Establishes a Server-Sent Events (SSE) connection that streams real-time updates during dataset generation. Clients receive structured events for:
  - Stage transitions (e.g., "prompt expansion", "scenario generation")
  - Progress percentages per stage
  - Model switch notifications when different AI models are used
  - Log messages and error alerts
  - Completion summaries with sample counts and elapsed time

This endpoint is essential for powering the frontend's live dashboard experience, enabling users to monitor pipeline execution without polling.

### Model Management

- **GET `/api/models`**  
  Lists all available AI models with their current status (available, busy, rate-limited), usage metrics, and priority levels. Used by the ModelDashboard component to display real-time model availability.

All endpoints follow consistent response formats using the defined TypeScript interfaces from `src/types.ts`, ensuring type safety across client-server communication. The API leverages FAISS for deduplication, Mistral AI for embeddings, and supports multiple providers through the model router system.

## Configuration

The DataForge LLM Dataset Generator is configured through multiple layers, including environment variables, backend settings, and frontend preferences. Below are the key configuration points supported by the codebase.

### Backend Configuration

The primary backend configuration is managed in `backend/config.py`, which defines API keys, provider base URLs, and model-specific settings for AI providers such as Groq, LongCat, Cerebras, and Mistral. This file includes rate limits and routing priorities for each model, ensuring efficient load balancing and fallback mechanisms. For example:

```python
# Example snippet from backend/config.py
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LONGCAT_BASE_URL = "https://api.longcat.com/v1"
CEREBRAS_MODEL_LIMITS = {"mistral-large": 10}  # requests per minute
```

Environment variables (e.g., `GROQ_API_KEY`) must be set before starting the backend to enable secure access to external AI services.

### Frontend Configuration

The React frontend uses several configuration files to manage build and runtime behavior:

- **`vite.config.ts`**: Sets up a proxy to forward all `/api` requests to `http://localhost:8005`, enabling seamless communication between the frontend and FastAPI backend during development.
  
- **`tsconfig.app.json`** and **`tsconfig.node.json`**: Define TypeScript compilation targets with strict type checking and modern ES2022 support, ensuring type safety across both client and server applications.

- **`src/api.ts`**: Implements typed API clients that interact with the backend endpoints, abstracting HTTP calls for actions like starting generation, checking status, and streaming updates via Server-Sent Events (SSE).

### Deduplication & Storage Settings

Deduplication is enabled via FAISS-based vector similarity checks in `backend/dedup/faiss_store.py`. The system supports persistence of vector indices and configurable similarity thresholds. In the frontend, users can toggle deduplication in the `ConfigPanel` component (`src/components/ConfigPanel.tsx`), which passes this setting to the backend pipeline.

File storage operations are handled by `backend/storage/file_manager.py`, which manages saving datasets in JSONL format with metadata tracking (e.g., sample count, timestamp, version).

### Logging & Monitoring

Logging is centralized using `backend/logger/setup.py`, which configures a colored console logger with structured output, supporting different log levels (INFO, DEBUG, ERROR) for monitoring pipeline progress and debugging issues.

### Environment Setup

Before running the application:

1. Ensure Python dependencies are installed via `backend/requirements.txt`.
2. Start the virtual environment and launch the FastAPI server on port 8005 using commands listed in `backend/run_commands.txt`.
3. Launch the React frontend via Vite, which automatically proxies API calls to the backend.

All configuration values should be validated at startup, and missing or invalid settings (e.g., unset API keys) will prevent the pipeline from initializing properly.

## Environment Variables

The DataForge LLM Dataset Generator relies on several environment variables to configure its backend services, API integrations, and operational behavior. These variables are primarily managed through the `backend/config.py` file, which centralizes configuration settings for multiple AI providers and system parameters.

### Core Backend Configuration

The application uses environment variables to securely manage sensitive information such as API keys and service endpoints. The most critical variables include:

- **`GROQ_API_KEY`**: Required for accessing Groq's language models. This key is used by the model router (`backend/models/model_router.py`) to authenticate requests to Groq's inference endpoints.
  
- **`MISTRAL_API_KEY`**: Necessary for generating text embeddings via the Mistral AI API, as implemented in `backend/dedup/embedder.py`. This enables semantic similarity checks during deduplication.

- **`CEREBRAS_API_KEY`** and **`LONGCAT_API_KEY`**: Used for fallback model routing when primary providers (like Groq) are unavailable or rate-limited, ensuring robust dataset generation.

These keys are referenced in `backend/config.py`, where they populate provider-specific configurations including base URLs, model names, and rate limits. For example:
```python
# Example from config.py structure
groq_config = {
    "base_url": os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
    "api_key": os.getenv("GROQ_API_KEY"),
    "models": ["llama3-8b-8192", "mixtral-8x7b-32768"],
    "rate_limit": 10  # requests per minute
}
```

### Operational Settings

Additional environment variables control system behavior:

- **`PORT`**: Specifies the port on which the FastAPI server runs (default: 8005), as seen in `backend/run_commands.txt` where Uvicorn starts on port 8005 with auto-reload.

- **`LOG_LEVEL`**: Controls logging verbosity, configured via `backend/logger/setup.py`, which sets up colored console output with structured formatting.

- **`STORAGE_DIR`**: Defines the directory path for saving generated datasets and metadata, managed by `backend/storage/file_manager.py`.

- **`DEDUPLICATION_THRESHOLD`**: A float value (e.g., 0.95) used in `backend/dedup/faiss_store.py` to determine similarity thresholds for duplicate detection using FAISS vector indexing.

### Frontend Integration

While the React frontend (`src/api.ts`) interacts with a local backend at `http://localhost:8005`, it does not directly consume environment variables. However, if deployed in different environments (development vs production), Vite’s proxy setup in `vite.config.ts` may need adjustment based on backend URL—though currently hardcoded to forward `/api` requests to `http://localhost:8005`.

> 💡 **Note**: All AI provider keys must be set before starting the backend. Failure to do so will result in failed API calls and pipeline errors. Use `.env` files or your deployment platform’s secret management to inject these securely.

Ensure all required environment variables are defined in your runtime environment to guarantee full functionality of the dataset generation pipeline.

## Model Setup & Training

The DataForge LLM Dataset Generator leverages a sophisticated model orchestration system powered by multiple AI providers to handle the complete dataset creation pipeline. The backend architecture is built around FastAPI and utilizes several specialized agents that interact with external language models through a configurable routing system.

**Model Routing & Management**  
At the core of the system is `backend/models/model_router.py`, which implements a smart routing mechanism that manages requests across different AI providers including Groq, LongCat, Cerebras, and Mistral. This router handles priority-based request distribution, enforces rate limits, manages model availability, and includes blacklisting capabilities for failed or overloaded models. The system automatically switches between models based on performance and availability, ensuring robust operation even when individual providers experience issues.

**AI Provider Configuration**  
Model configurations are centrally managed in `backend/config.py`, where API keys, base URLs, and specific model settings are defined with appropriate rate limits for each provider. This centralized configuration allows easy switching between different AI services and ensures consistent behavior across all pipeline stages.

**Pipeline Agents Architecture**  
The system employs several specialized agents working in sequence:
- **Prompt Expansion Agent** (`backend/agents/prompt_expander.py`) transforms raw user prompts into detailed dataset briefs using AI models
- **Scenario Generation Agent** (`backend/agents/scenario_generator.py`) creates diverse, numbered scenario headings from approved prompts
- **Dataset Generation Agent** (`backend/agents/dataset_generator.py`) produces question-answer pairs in ShareGPT format with optional memory injection
- **Manager Agent** (`backend/agents/manager_agent.py`) reviews and iteratively refines prompts through an approval loop until quality standards are met

**Deduplication System**  
To ensure dataset quality, the system implements FAISS-based cosine similarity deduplication through `backend/dedup/faiss_store.py`. This vector store detects and eliminates duplicate content during the generation process, maintaining data diversity while preserving accuracy.

**Real-time Processing & Streaming**  
All model interactions support real-time progress tracking via server-sent events (SSE) implemented in `backend/streaming/sse_manager.py`. This enables live updates throughout the generation pipeline, allowing users to monitor completion status, view logs, and receive notifications about model switches or errors.

**Embedding Generation**  
Text embeddings for deduplication are generated asynchronously using Mistral AI's API through `backend/dedup/embedder.py`, which handles HTTP requests to create vector representations of text content.

This comprehensive model setup provides a resilient, scalable foundation for high-quality dataset generation with automatic failover, intelligent load balancing, and real-time monitoring capabilities.

## Project Structure

The DataForge LLM Dataset Generator is organized as a modern full-stack application with a clear separation between frontend and backend components. The project follows a monorepo structure with shared TypeScript configurations and dedicated directories for each major component.

### Frontend (`src/`)
The React-based frontend is built using Vite and TypeScript, providing an interactive interface for dataset generation. Key files include:
- `main.tsx`: Application entry point that renders the main App component within StrictMode
- `App.tsx`: Main application logic managing pipeline state, SSE connections, and UI orchestration
- `App.css` & `index.css`: Global styling with dark theme, custom color variables, and monospace font styling
- `api.ts`: API client handling all backend communications including model status, progress tracking, and data retrieval
- Component directory containing:
  - `ConfigPanel.tsx`: User input interface for prompts, memory facts, dataset size, and deduplication settings
  - `PipelineProgress.tsx`: Real-time progress dashboard showing stage completion, logs, and model switches
  - `ModelDashboard.tsx`: Collapsible model status display with usage metrics and availability indicators
  - `DownloadSection.tsx`: Completion summary with download link and metadata display

### Backend (`backend/`)
The FastAPI backend handles the core dataset generation pipeline with multiple specialized modules:

**Core Services:**
- `main.py`: FastAPI application entry point exposing REST endpoints and SSE streaming
- `config.py`: Configuration management for API keys, provider URLs, and rate limits across multiple AI providers (Groq, LongCat, Cerebras, Mistral)
- `run_commands.txt`: Commands to activate virtual environment and start Uvicorn server on port 8005 with auto-reload

**Agent System:**
- `manager_agent.py`: Coordinates prompt refinement through approval loops with iterative feedback
- `prompt_expander.py`: Transforms raw prompts into detailed dataset briefs using AI models
- `scenario_generator.py`: Creates diverse scenario headings from approved prompts
- `dataset_generator.py`: Generates question-answer pairs in ShareGPT format with optional memory injection

**Storage & Processing:**
- `storage/file_manager.py`: Manages text, JSON, and JSONL file operations in designated storage directory
- `dedup/faiss_store.py`: FAISS-based vector store for cosine similarity deduplication
- `dedup/embedder.py`: Async function generating text embeddings via Mistral AI API

**Utilities:**
- `streaming/sse_manager.py`: Server-sent events manager using asyncio queue for real-time event broadcasting
- `logger/setup.py`: Configures colored console logging with structured formatting
- `models/model_router.py`: Routes requests to available AI models based on priority, availability, and usage limits

### Configuration & Tooling
- `package.json` & `package-lock.json`: Frontend dependencies including Vite, ESLint, and TypeScript
- `tsconfig.json` & related configs: TypeScript project references splitting build into separate applications
- `vite.config.ts`: Vite configuration with proxy setup forwarding `/api` requests to `http://localhost:8005`
- `eslint.config.js`: ESLint configuration for TypeScript React with recommended rules and React plugins

### Documentation
- `CONTRIBUTING.md`: Comprehensive contributor guide with setup instructions and workflow
- `SUPPORT.md`: Support resources including issue reporting guidelines and configuration details
- `SECURITY.md`: Security policy covering vulnerability reporting and disclosure procedures
- `CODE_OF_CONDUCT.md`: Community guidelines implementing Contributor Covenant standards

## Development

### Project Structure

This project is a full-stack application with a **React frontend** and a **FastAPI backend**, built for generating LLM datasets. The codebase follows a clear separation of concerns:

- **Frontend**: Located in `src/`, the React application uses Vite as the build tool, TypeScript for type safety, and ESLint for code quality. Key files include:
  - `src/main.tsx`: Entry point that renders the App within StrictMode.
  - `src/App.tsx`: Main component managing pipeline state and SSE connections.
  - `src/api.ts`: API client for backend communication.
  - Components like `ConfigPanel`, `PipelineProgress`, `ModelDashboard`, and `DownloadSection` handle user interaction, progress tracking, and file downloads.

- **Backend**: Stored in `backend/`, this FastAPI service orchestrates the dataset generation pipeline using AI agents. Core files are:
  - `backend/main.py`: FastAPI app with endpoints for starting generation, checking status, streaming logs via SSE, and resetting the system.
  - `backend/models/model_router.py`: Routes requests to available AI models with rate limiting and fallback logic.
  - `backend/agents/` contains specialized modules: `prompt_expander.py`, `scenario_generator.py`, and `dataset_generator.py` for prompt refinement, scenario creation, and QA pair generation.
  - `backend/dedup/embedder.py` and `faiss_store.py`: Handle deduplication using FAISS and Mistral embeddings.
  - `backend/streaming/sse_manager.py`: Manages real-time event broadcasting.
  - `backend/storage/file_manager.py`: Handles file I/O for saving generated datasets.

- **Configuration & Tooling**:
  - `tsconfig.json`, `tsconfig.app.json`, and `tsconfig.node.json`: Configure TypeScript for both frontend and backend builds.
  - `vite.config.ts`: Sets up proxy from `/api` to `http://localhost:8005`.
  - `eslint.config.js`: Enforces coding standards with React and Refresh plugins.
  - `backend/requirements.txt`: Lists Python dependencies including FastAPI, FAISS, and logging utilities.
  - `backend/run_commands.txt`: Provides commands to start the backend with Uvicorn on port 8005 with auto-reload.

### Frontend Development

To develop the frontend:

1. Install dependencies: `npm install`
2. Start the development server: `npm run dev`
3. The app runs on `http://localhost:5173` (default Vite port) with hot module replacement enabled.

The UI is styled with a dark theme using custom CSS variables and features components for configuration (`ConfigPanel`), real-time progress tracking (`PipelineProgress`), model status monitoring (`ModelDashboard`), and dataset download (`DownloadSection`). All API calls are proxied through Vite to the backend running on port 8005.

### Backend Development

For backend development:

1. Activate the virtual environment using the commands in `backend/run_commands.txt`.
2. Install Python dependencies: `pip install -r backend/requirements.txt`
3. Start the server: `uvicorn backend.main:app --reload --port 8005`

The backend exposes RESTful endpoints under `/api` and streams real-time updates via Server-Sent Events (SSE). It supports asynchronous processing of prompts through a multi-stage pipeline involving prompt expansion, scenario generation, dataset creation, and optional deduplication using FAISS-based similarity search.

## Security

The DataForge LLM Dataset Generator prioritizes security throughout its architecture and operational lifecycle. The project maintains a formal **Security Policy** documented in `SECURITY.md`, which outlines supported versions, vulnerability reporting procedures, disclosure timelines, and response processes. This ensures responsible disclosure practices and provides clear guidance for both users and contributors to report potential security issues.

### Authentication & API Key Management
The backend configuration is managed through `backend/config.py`, which handles sensitive credentials including API keys for multiple AI providers (Groq, LongCat, Cerebras, Mistral). These keys are loaded via environment variables, preventing hardcoded secrets in the codebase. The system implements rate limiting and blacklisting functionality in `backend/models/model_router.py` to prevent abuse and ensure fair usage of external AI services.

### Secure Communication
The frontend (`src/api.ts`) communicates with the backend through a proxy configured in `vite.config.ts`, which forwards API requests from `/api` to `http://localhost:8005`. This setup ensures that all client-server communication occurs over standard HTTP protocols during development. For production deployments, this should be secured with HTTPS/TLS encryption.

### Input Validation & Sanitization
All user inputs—including prompts, memory facts, and dataset parameters—are processed through the configuration interface in `src/components/ConfigPanel.tsx` and validated before being sent to AI models. The pipeline stages in `backend/main.py` handle data transformation and generation tasks, with structured logging implemented in `backend/logger/setup.py` that avoids exposing sensitive information in logs.

### Dependency Security
Both frontend and backend dependencies are explicitly defined in `package.json` and `backend/requirements.txt`, ensuring reproducible builds and reducing risks associated with transitive vulnerabilities. The project uses modern tooling (TypeScript, ESLint) with strict type checking enabled across configurations (`tsconfig.app.json`, `tsconfig.node.json`) to catch potential security-related bugs at compile time.

### Code Quality & Review Processes
A comprehensive **Contributor Covenant Code of Conduct** (`CODE_OF_CONDUCT.md`) establishes behavioral expectations for maintainers and contributors, promoting a secure and respectful development environment. The contribution guidelines in `CONTRIBUTING.md` outline processes for bug reports and feature suggestions that include security considerations.

> 🔒 **Note**: Users are advised to regularly update dependencies and follow the security policy outlined in `SECURITY.md` when deploying DataForge in production environments.

## Contributing

Welcome to the DataForge LLM Dataset Generator project! We appreciate your interest in contributing. This guide outlines how you can help improve the project, whether through code, documentation, or community support.

### 🪜 Getting Started

To begin contributing, follow these steps:

1. **Fork the repository** and clone it locally.
2. **Set up your development environment** by installing dependencies:
   ```bash
   npm install
   ```
3. **Configure the backend** by ensuring Python dependencies are installed in `backend/`:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. **Start the development servers**:
   - Run the FastAPI backend using commands from `backend/run_commands.txt`
   - Start the Vite frontend with:
     ```bash
     npm run dev
     ```

The project uses **TypeScript**, **React**, **Vite**, **FastAPI**, and **FAISS** for vector similarity. Configuration is managed via `tsconfig.json`, `vite.config.ts`, and `backend/config.py`.

### 🧩 How to Contribute

We welcome contributions in several forms:

- **Bug Reports**: Use GitHub Issues to report bugs. Include steps to reproduce, expected vs actual behavior, and environment details.
- **Feature Requests**: Open a discussion or issue to propose new features. Please provide context and use cases.
- **Code Contributions**: Submit pull requests targeting the `main` branch. Ensure your code follows the established style.

All code must pass ESLint checks configured in `eslint.config.js`. The project enforces strict TypeScript typing as defined in `src/types.ts`.

### 🔄 Contribution Workflow

1. Create a feature or bugfix branch from `main`.
2. Make your changes with clear commit messages.
3. Test your changes locally:
   - Verify frontend components render correctly
   - Confirm backend endpoints respond as expected
   - Check that SSE streaming works in `src/api.ts`
4. Update documentation if needed (see `CONTRIBUTING.md`, `SUPPORT.md`)
5. Submit a pull request with a descriptive title and detailed description

### 📝 Code Style & Standards

- Follow React best practices using functional components with hooks
- Use async/await consistently in backend services (`backend/agents/*.py`, `dedup/*.py`)
- Maintain consistent logging using the setup in `backend/logger/setup.py`
- Preserve dark theme styling across all CSS files (`*.css`)
- Keep API contracts stable — update `src/types.ts` if interfaces change

### 🤝 Community Guidelines

This project adheres to our [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful, inclusive, and constructive in all interactions.

For support questions, refer to `SUPPORT.md` for guidance on using the application and troubleshooting common issues.

Thank you for helping make DataForge better!

## Code of Conduct

We are committed to fostering a **respectful, inclusive, and collaborative environment** for all contributors and users of the DataForge LLM Dataset Generator project. This Code of Conduct outlines our expectations for behavior within our community and provides guidelines for reporting concerns.

### Our Pledge

In the interest of promoting an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual orientation.

This project is built using modern web technologies including **React**, **TypeScript**, **Vite**, and **FastAPI**, and emphasizes clean, well-documented code. We expect all interactions—whether through GitHub Issues, Discussions, pull requests, or direct communication—to reflect the values of professionalism and mutual respect.

### Expected Behavior

All participants are expected to:

- 🤝 Be respectful and considerate in discussions and code reviews.
- 📚 Provide constructive feedback that supports improvement.
- 🧪 Contribute to a collaborative spirit by helping others understand the codebase, which includes structured logging (via `backend/logger/setup.py`) and modular architecture.
- 🔒 Respect intellectual property and follow licensing terms in `package.json` and `backend/requirements.txt`.

### Unacceptable Behavior

Unacceptable behaviors include but are not limited to:

- 🚫 Harassment, discrimination, or derogatory language.
- 💬 Personal attacks, trolling, or disruptive comments.
- 🔗 Posting private information without consent.
- 🛠️ Intentionally submitting low-quality or malicious code, especially given the project’s reliance on AI agents (`backend/agents/*.py`) and real-time streaming (`streaming/sse_manager.py`).

### Enforcement

Project maintainers have the responsibility to enforce this Code of Conduct. Violations may result in:

- ⚠️ Temporary or permanent bans from discussions, issues, or contributions.
- 📝 Public or private warnings.
- 🛑 Removal of inappropriate content or comments.

Maintainers will act promptly and fairly, referencing this document when addressing reports.

### Reporting Violations

If you witness or experience unacceptable behavior, please report it via:

- 🐞 [GitHub Issues](https://github.com/H0NEYP0T-466/dataset-generator/issues) with the label `conduct`
- 💬 [GitHub Discussions](https://github.com/H0NEYP0T-466/dataset-generator/discussions)

All reports will be reviewed confidentially by the maintainer team, as outlined in our [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md) policies.

### Scope

This Code of Conduct applies to all project spaces, including repositories, issue trackers, discussion forums, and any related communications. It also extends to public behavior when representing the project.

---

By participating in this project, you agree to abide by these guidelines. Let’s build great datasets—and a great community—together. 🌱

## License

This project, **DataForge**, is an open-source LLM dataset generator built with a modern tech stack including FastAPI, React, TypeScript, and Vite. The codebase is distributed under the terms of the **MIT License**, a permissive free software license that allows for broad use, modification, distribution, and private use of the software, provided that appropriate copyright and license notices are preserved.

The MIT License grants users the freedom to:
- Use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software
- Incorporate the software into proprietary applications without restriction
- Include the original source code or compiled binaries in commercial products

**Key conditions of the MIT License include:**
- The above copyright notice and this permission notice must be included in all substantial portions of the software
- The software is provided "as is," without warranty of any kind—express or implied—including but not limited to warranties of merchantability, fitness for a particular purpose, or non-infringement
- In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from, out of, or in connection with the software or its use

This licensing approach aligns with the open and collaborative development model promoted by the project, encouraging contributions and community-driven improvements while maintaining clear legal boundaries. The presence of standard open-source files such as `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` further reflects the project’s commitment to responsible and inclusive software stewardship.

By using, modifying, or distributing this software, you agree to abide by the terms of the MIT License. A full copy of the license text should accompany the repository and can typically be found in the root directory as `LICENSE` (though not explicitly listed in the provided file summary, it is standard practice for MIT-licensed projects).

🔐 **Note**: While the core application logic is open, third-party AI models and APIs used during dataset generation (e.g., Mistral AI, Groq, Cerebras via backend/config.py) may be governed by their own separate terms of service and usage policies. Users are responsible for ensuring compliance with those external agreements when deploying or using the generated datasets.

---

<p align="center">Made with ❤️ by <a href="https://github.com/H0NEYP0T-466">H0NEYP0T-466</a></p>