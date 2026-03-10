# DataForge

## Abstract 🚀

The **H0NEYP0T-466/dataset-generator** repository implements **DataForge**, a sophisticated web-based platform designed to automate the generation of high-quality fine-tuning datasets for Large Language Models (LLMs). Built as a full-stack application, DataForge leverages modern AI agents and real-time streaming technologies to transform raw user prompts into structured, diverse, and deduplicated question-answer pairs in ShareGPT format. The system is engineered for scalability, observability, and user control, making it ideal for researchers and developers seeking to rapidly prototype or enhance LLM behavior.

At its core, the backend is powered by **FastAPI** and orchestrated through a multi-stage pipeline managed by intelligent agents. These include a `manager_agent` that iteratively refines prompts via an approval loop, a `prompt_expander` that constructs detailed personas and tasks, and a `scenario_generator` that produces numbered scenario headings from approved inputs. For dataset creation, the `dataset_generator` agent synthesizes QA pairs with optional memory injection and employs **FAISS**-based vector similarity search to eliminate duplicates efficiently. All operations are tracked in real time using **Server-Sent Events (SSE)**, enabling seamless frontend monitoring of progress, logs, and model switches.

The frontend is a responsive React application built with **Vite** and styled with a dark theme using monospace fonts for clarity. It features interactive components such as a collapsible **Model Dashboard** displaying real-time model status and usage metrics, a dynamic **Pipeline Progress** tracker with stage-wise completion percentages and live logs, and a configurable **ConfigPanel** allowing users to input prompts, set dataset sizes, toggle deduplication, and select presets. A dedicated **DownloadSection** summarizes completion statistics—including sample count, elapsed time, and scenario count—and provides direct access to generated data files.

Technically, the stack integrates robust logging via `colorlog`, asynchronous embedding generation using the Mistral AI API, and modular file management for persistent storage. Configuration is centralized in `config.py`, supporting multiple providers like Groq, LongCat, Cerebras, and Mistral with rate limiting and fallback logic handled by a custom `model_router`. Development practices emphasize code quality through ESLint and TypeScript strict typing across both client (`tsconfig.app.json`) and server (`tsconfig.node.json`) environments.

In summary, DataForge represents a production-ready, extensible framework for LLM dataset engineering—combining agentic workflows, real-time feedback, and developer-friendly tooling to streamline the creation of training data at scale.

## Key Highlights

🚀 **Modern Full-Stack Architecture**  
This project is a sophisticated full-stack application built with **React 18 + TypeScript** on the frontend and **FastAPI + Python** on the backend, orchestrated by **Vite** for rapid development. The architecture supports real-time communication via Server-Sent Events (SSE), enabling live updates during data generation workflows.

🧠 **Advanced LLM-Powered Dataset Generation Pipeline**  
At its core, DataForge leverages multiple AI agents to transform raw user prompts into high-quality, structured datasets suitable for fine-tuning large language models. The system employs a multi-stage pipeline involving prompt expansion, scenario generation, and question-answer pair creation—all powered by OpenAI-compatible models from providers like Groq, LongCat, Cerebras, and Mistral.

🔁 **Intelligent Deduplication & Embedding Layer**  
To ensure dataset uniqueness, the backend integrates **FAISS** for efficient vector similarity search using cosine distance metrics. Text embeddings are generated asynchronously via the Mistral API, enabling scalable deduplication across thousands of generated samples.

📊 **Real-Time Progress Monitoring & Logging**  
Users interact with a responsive React dashboard that displays live pipeline progress through visual stage cards, completion percentages, and detailed logs. The system tracks model switches, usage metrics, and error states in real time, providing transparency throughout the generation process.

💾 **Robust File Management & Output Handling**  
Generated datasets are saved in standardized formats (JSON/JSONL) with metadata tracking. A dedicated download section allows users to retrieve completed datasets immediately after pipeline execution, complete with summary statistics like sample count and elapsed time.

⚙️ **Flexible Configuration & Preset Support**  
The configuration panel enables fine-grained control over dataset parameters including size, memory injection, and deduplication toggles. Preset options streamline common use cases while maintaining flexibility for custom requirements.

🛡️ **Enterprise-Grade Development Practices**  
The codebase enforces strict type safety with comprehensive TypeScript interfaces, follows ESLint best practices, uses structured logging with colorized output, and maintains reproducible builds through locked dependencies and virtual environment management.

🌐 **Production-Ready Deployment Setup**  
The project includes complete deployment scaffolding: Uvicorn server configuration on port 8005 with auto-reload, proxy settings for seamless frontend-backend communication, and clear startup commands for isolated development environments.

## Features

**DataForge — LLM Dataset Generator** is a powerful, real-time web application built with React and FastAPI that automates the creation of high-quality fine-tuning datasets for large language models. The system employs a sophisticated multi-stage pipeline managed by specialized AI agents, providing full transparency and control through an intuitive dashboard.

### 🤖 Intelligent Multi-Agent Pipeline
The core of DataForge is its agent-based architecture featuring four specialized components:
- **Prompt Expander Agent**: Transforms raw user prompts into detailed persona descriptions and task specifications using advanced language models
- **Manager Agent**: Implements an approval loop that reviews and iteratively refines dataset prompts based on AI feedback to ensure quality before finalization
- **Scenario Generator Agent**: Creates diverse, numbered scenario headings from approved prompts with fallback handling and progress tracking
- **Dataset Generator Agent**: Produces question-answer pairs in ShareGPT format with optional memory injection and deduplication capabilities

### 📊 Real-Time Progress Monitoring
Experience live updates through comprehensive monitoring features:
- **Pipeline Progress Dashboard**: Visual stage-by-stage progress with status indicators, completion percentages, and model switch notifications
- **Server-Sent Events (SSE)**: Real-time event streaming for instant status updates without polling overhead
- **Model Status Tracking**: Live display of model availability, usage metrics, and current operational status
- **Comprehensive Logging**: Detailed log display with color-coded status states and smooth animations

### 🔍 Advanced Deduplication System
Ensure dataset uniqueness with state-of-the-art similarity detection:
- **FAISS Vector Store**: Efficient cosine similarity-based deduplication using FAISS library
- **Embedding Generation**: Asynchronous text embedding creation via Mistral AI API integration
- **Configurable Thresholds**: Adjustable similarity parameters for precision control

### 💾 Robust Storage & Download Management
Seamless data handling throughout the generation process:
- **Multi-format Support**: Save and load text, JSON, and JSONL files with automatic directory management
- **Download Section**: Completion summary with sample count, elapsed time, scenario count, and direct download links
- **File Organization**: Structured storage system with logging and error recovery

### ⚙️ Flexible Configuration Interface
Complete control over your dataset generation workflow:
- **Interactive Config Panel**: Input fields for custom prompts, memory facts, and dataset size selection
- **Preset Templates**: Quick-start options for common use cases
- **Deduplication Toggle**: Enable/disable similarity filtering as needed
- **Error Handling**: Comprehensive validation and user-friendly error messages

### 🛠️ Modern Development Stack
Built with cutting-edge technologies for optimal performance:
- **React + TypeScript**: Type-safe frontend with modern component architecture
- **FastAPI Backend**: High-performance Python API with async support
- **Vite Build Tool**: Lightning-fast development and production builds
- **ESLint Integration**: Strict code quality enforcement with recommended presets
- **Colorful Logging**: Structured, colored output for better debugging experience

The system supports multiple AI providers including Groq, LongCat, Cerebras, and Mistral through a unified model router with rate limiting and priority-based selection, ensuring reliable operation across different infrastructure configurations.

## Architecture

The DataForge — LLM Dataset Generator is built as a modern, full-stack application with a clear separation between frontend and backend responsibilities. The system follows a **React + TypeScript** frontend architecture powered by **Vite**, communicating with a **FastAPI** Python backend via REST and Server-Sent Events (SSE).

### Frontend Layer
The React-based client (`src/App.tsx`) orchestrates the user experience, managing state for pipeline execution, real-time progress tracking, and configuration inputs. It leverages custom components such as `ConfigPanel` for user input, `PipelineProgress` for live status visualization, `ModelDashboard` for model monitoring, and `DownloadSection` for output delivery. All components use a dark theme styled with CSS-in-JS principles and monospace typography. Communication with the backend occurs through an API abstraction layer (`src/api.ts`) that handles HTTP requests, SSE connections, and error handling.

### Backend Layer
The FastAPI server (`backend/main.py`) serves as the core orchestrator, exposing endpoints to initiate dataset generation pipelines, stream progress updates via SSE, and manage system resets. It integrates multiple specialized agents:
- **Prompt Expander**: Transforms raw prompts into structured persona/task descriptions.
- **Scenario Generator**: Creates numbered scenario headings from approved prompts.
- **Dataset Generator**: Produces ShareGPT-formatted QA pairs with optional memory injection.
- **Manager Agent**: Implements an approval loop to refine prompts iteratively before final generation.

Deduplication is handled via FAISS (`backend/dedup/faiss_store.py`) using cosine similarity on embeddings generated by Mistral AI (`backend/dedup/embedder.py`). File persistence is managed through a dedicated file manager (`backend/storage/file_manager.py`), supporting JSON and JSONL formats.

Model routing (`backend/models/model_router.py`) selects among OpenAI-compatible providers (Groq, LongCat, Cerebras, Mistral) based on availability and rate limits, with in-memory usage tracking. Real-time event broadcasting is facilitated by an asynchronous SSE manager (`backend/streaming/sse_manager.py`).

Configuration is centralized in `backend/config.py`, defining API keys, provider URLs, and model-specific rate limits. Logging uses a structured, colorized setup (`backend/logger/setup.py`) for enhanced observability during development.

This modular design enables scalable, observable, and maintainable dataset generation with real-time feedback and robust deduplication capabilities.

## Tech Stack

This project is a sophisticated **LLM Dataset Generator** built with a modern, full-stack architecture designed for real-time data pipeline monitoring and management. The tech stack leverages cutting-edge tools and frameworks to deliver a responsive, scalable, and developer-friendly experience.

### 🔧 Core Technologies

The application is powered by a robust combination of frontend and backend technologies:

<p>
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
</p>

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Uvicorn-2980B9?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Uvicorn">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

### 📦 Key Dependencies & Libraries

The project integrates several essential libraries for functionality, performance, and development:

#### Frontend
- **React**: For building the interactive user interface with component-based architecture.
- **TypeScript**: Provides static typing for enhanced code quality and maintainability.
- **Vite**: Lightning-fast build tool and development server with hot module replacement.
- **ESLint**: Ensures code consistency and catches potential errors early in development.

#### Backend
- **FastAPI**: High-performance web framework for building APIs with automatic OpenAPI documentation.
- **Uvicorn**: ASGI server for running FastAPI applications with async support.
- **FAISS**: Efficient similarity search library for deduplication using vector embeddings.
- **colorlog**: Adds color-coded logging output for better debugging and monitoring.
- **aiohttp**: Asynchronous HTTP client used for making API calls to external services like Mistral AI.

### 🛠️ Development & Configuration

The project uses modern development practices and configuration systems:

- **TypeScript Configuration**: Separate configurations for app (`tsconfig.app.json`) and Node.js environments (`tsconfig.node.json`), both enforcing strict type checking.
- **Virtual Environment Management**: Python dependencies are managed via `requirements.txt` with isolated environment setup.
- **Real-time Communication**: Server-Sent Events (SSE) via custom `sse_manager.py` for live progress updates.
- **File Storage**: Custom `file_manager.py` handles persistent storage of generated datasets in various formats (JSON, JSONL).
- **Model Abstraction**: `model_router.py` provides unified access to multiple LLM providers including OpenAI-compatible models from Groq, LongCat, Cerebras, and Mistral.

This comprehensive tech stack enables the generation of high-quality, deduplicated datasets through an agent-based pipeline while providing real-time visibility into the process through a polished React frontend.

## Dependencies & Packages

This project is a full-stack application built with modern web technologies and designed for efficient dataset generation using large language models. The codebase clearly defines its dependencies through standard configuration files, ensuring reproducibility and proper environment setup.

### Frontend Stack
The frontend is powered by **React** with **TypeScript**, managed via **Vite** as the build tool. The project uses `package.json` to define all JavaScript/TypeScript dependencies, including development tools like ESLint for code quality and TypeScript support. Vite’s configuration in `vite.config.ts` enables fast development server startup and proxying of API requests to the backend. The React application is structured with components such as `ConfigPanel`, `PipelineProgress`, and `DownloadSection`, all styled using CSS-in-JS patterns and global styles defined in `src/index.css`. The UI follows a dark theme with monospace typography, emphasizing clarity and developer-friendly aesthetics.

### Backend Stack
The backend is implemented in **Python 3**, utilizing **FastAPI** as the web framework and **Uvicorn** as the ASGI server for serving the application on port 8005. Dependencies are listed in `backend/requirements.txt`, which includes essential libraries such as:
- `fastapi`: For building the RESTful API endpoints.
- `uvicorn`: To run the FastAPI app with auto-reload capabilities.
- `faiss-cpu` or `faiss-gpu`: For efficient similarity search during deduplication.
- `colorlog`: Used in `backend/logger/setup.py` to provide colored, structured logging output.
- Standard utilities like `python-dotenv` for environment management and logging.

Additionally, the backend leverages several custom modules:
- **Model Router** (`models/model_router.py`) manages AI model selection and rate limiting.
- **Deduplication Engine** (`dedup/faiss_store.py`) uses FAISS for cosine similarity-based embedding comparison.
- **Agent System**: Includes `prompt_expander.py`, `scenario_generator.py`, `manager_agent.py`, and `dataset_generator.py`, orchestrating the multi-stage pipeline for prompt refinement, scenario creation, and QA pair generation.
- **Streaming Support**: `streaming/sse_manager.py` handles real-time event broadcasting via Server-Sent Events (SSE), enabling live progress updates from the frontend.

### Development & Build Configuration
TypeScript compilation is configured via `tsconfig.json`, which references separate configurations for the frontend (`tsconfig.app.json`) and Node.js-related tooling (`tsconfig.node.json`). These enforce strict type checking and modern ES2022+ features. ESLint (`eslint.config.js`) ensures code consistency across both frontend and backend tooling environments.

All dependencies are version-locked in `package-lock.json` to ensure consistent builds across development and deployment environments.

## Prerequisites

Before setting up and running the **DataForge — LLM Dataset Generator**, ensure your development environment meets the following requirements as evidenced by the codebase structure and dependencies:

### 🔧 Core Technologies & Runtimes

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
</p>

The project is a full-stack application built with **Python** for the backend and **TypeScript/React** for the frontend. You must have both Python (3.8+) and Node.js (16+) installed on your system.

### ⚙️ Backend Dependencies

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/FAISS-FF6F00?style=for-the-badge&logo=faiss&logoColor=white" alt="FAISS">
  <img src="https://img.shields.io/badge/Uvicorn-F7DF1E?style=for-the-badge&logo=uvicorn&logoColor=black" alt="Uvicorn">
</p>

The backend relies on **FastAPI** as the web framework, served via **Uvicorn** with auto-reload support on port `8005`. It uses **FAISS** for vector-based deduplication of embeddings. Install backend dependencies using:

```bash
pip install -r backend/requirements.txt
```

Ensure you have access to AI model providers such as OpenAI, Groq, LongCat, Cerebras, or Mistral, as configured in `backend/config.py`.

### 🖥️ Frontend Stack

<p>
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/ESLint-4B32C3?style=for-the-badge&logo=eslint&logoColor=white" alt="ESLint">
</p>

The frontend is built with **React** using **Vite** as the build tool. It includes **TypeScript** strict typing and **ESLint** for code quality. Install frontend dependencies via:

```bash
npm install
```

This will resolve all React, Vite, TypeScript, and ESLint-related packages defined in `package.json` and `package-lock.json`.

### 🌐 Development Tools

- **Server-Sent Events (SSE)**: Used for real-time progress updates (`backend/streaming/sse_manager.py`).
- **Logging**: Structured, colored logging via `colorlog` in `backend/logger/setup.py`.
- **File Management**: Persistent storage handled by `backend/storage/file_manager.py`.
- **Embedding Generation**: Asynchronous text embedding via Mistral AI API (`backend/dedup/embedder.py`).

> 💡 **Note**: The application uses a proxy configuration (`vite.config.ts`) to forward API requests from the frontend (`localhost:5173`) to the backend (`localhost:8005`). Ensure no port conflicts exist.

All components are designed to run locally with proper environment variable setup (e.g., API keys) as referenced in `backend/config.py`.

## Installation

This project requires both a Python backend and a React frontend. Follow these steps to set up the complete application.

### Prerequisites

- **Python 3.8+** (for backend services)
- **Node.js 16+** with npm (for frontend development)
- **Git** (to clone the repository)

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   This installs FastAPI, FAISS for similarity search, and other required packages including logging utilities and environment management tools.

4. **Configure API keys and settings:**
   Edit `backend/config.py` to add your AI model API keys and configure provider endpoints as needed.

5. **Start the backend server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8005 --reload
   ```
   The `--reload` flag enables auto-reload during development. Refer to `run_commands.txt` for additional command options.

### Frontend Setup

1. **Return to the project root and install frontend dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173` by default (Vite's default port). The Vite configuration in `vite.config.ts` sets up a proxy so that API requests from the frontend are automatically forwarded to the backend running on port 8005.

### Configuration Files

Ensure you have the following configuration files properly set up:

- `tsconfig.json`, `tsconfig.app.json`, and `tsconfig.node.json` define TypeScript compilation settings for both the React app and Node.js backend code.
- `eslint.config.js` enforces code quality standards across the project.
- Global styles are defined in `src/index.css` with dark theme theming and monospace typography.

### Running the Application

Once both servers are running:
- Access the web interface at `http://localhost:5173`
- The backend API will be available at `http://localhost:8005`

The system uses Server-Sent Events (SSE) for real-time progress updates, allowing the frontend components like `PipelineProgress` and `ModelDashboard` to display live status information during dataset generation.

> **Note:** Make sure the backend is running before starting the frontend, as the React components expect the API to be available at localhost:8005.

## Quick Start

Welcome to **DataForge — LLM Dataset Generator**! This tool enables you to generate high-quality, deduplicated datasets for fine-tuning large language models using a multi-agent pipeline. The system supports real-time progress tracking, model switching, and structured output in ShareGPT format.

### Prerequisites

Ensure you have the following installed:
- **Python 3.9+**
- **Node.js 16+** and **npm**
- A valid API key for at least one supported AI provider (e.g., Mistral, Groq, OpenAI)

### Backend Setup

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your API keys by setting environment variables or updating `config.py`. Supported providers include Mistral, Groq, LongCat, and Cerebras.

5. Start the FastAPI server with auto-reload:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8005 --reload
   ```
   The backend will run on `http://localhost:8005`.

### Frontend Setup

1. In a new terminal, navigate to the project root and install frontend dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```
   The React app will be available at `http://localhost:5173`.

### Using the Application

1. Open your browser and go to `http://localhost:5173`.

2. In the **ConfigPanel**, enter your desired prompt and optional memory facts.

3. Select dataset size and enable/disable deduplication as needed.

4. Click **Start Generation** to begin the pipeline.

5. Monitor real-time progress via the **PipelineProgress** component, which shows stage status, completion percentage, logs, and model switches.

6. Once complete, use the **DownloadSection** to retrieve your generated dataset in JSONL format.

The system uses Server-Sent Events (SSE) to stream updates, ensuring smooth interaction even during long-running tasks. If errors occur, they’ll appear in the log panel for troubleshooting.

> 💡 **Tip**: The backend includes FAISS-based deduplication and supports multiple AI models. You can switch models dynamically during execution based on availability and usage limits.

Your generated datasets are saved locally and ready for use in fine-tuning workflows.

## Usage

The DataForge dataset generator is a full-stack application that enables users to create high-quality LLM training datasets through an interactive web interface and robust backend pipeline. To get started, ensure you have Python 3.9+ and Node.js installed on your system.

### Prerequisites

Before running the application, you'll need to set up API keys for your preferred AI providers. The backend supports multiple providers including OpenAI-compatible services, Groq, LongCat, Cerebras, and Mistral. Configure these in the backend by setting environment variables or updating the `backend/config.py` file with your actual API keys and provider URLs.

### Backend Setup

1. Navigate to the `backend` directory
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8005 --reload
   ```

The backend will be available at `http://localhost:8005` and provides RESTful APIs for dataset generation, model management, and real-time progress streaming via Server-Sent Events (SSE).

### Frontend Setup

1. Install frontend dependencies:
   ```bash
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```

The React application will be available at `http://localhost:5173` (default Vite port) with automatic proxying of API requests to the backend.

### Using the Application

1. **Configure Your Dataset**: Use the configuration panel to enter your base prompt, add memory facts, and set dataset parameters including size and deduplication preferences.

2. **Monitor Progress**: The pipeline dashboard displays real-time progress through each stage:
   - Prompt expansion and refinement
   - Scenario generation with numbered headings
   - Question-answer pair creation in ShareGPT format
   - Optional deduplication using FAISS-based vector similarity search

3. **Track Model Usage**: The collapsible model dashboard shows which AI models are currently active, their usage statistics, and availability status with automatic polling during execution.

4. **Download Results**: Once completed, the download section provides a summary with sample count, elapsed time, scenario count, and a direct link to download your generated dataset as JSONL files.

### Key Features

- **Real-time Updates**: All stages show live progress with color-coded status indicators and completion percentages
- **Model Switching**: Automatic fallback between different AI providers when rate limits are reached
- **Deduplication**: Optional cosine similarity-based duplicate removal using FAISS vector store
- **Structured Output**: Generated datasets follow ShareGPT format suitable for fine-tuning
- **Error Handling**: Comprehensive logging and error recovery throughout the pipeline

The system uses TypeScript for type safety, ESLint for code quality, and Vite for fast development builds. All components feature a dark theme with neon green accents optimized for extended development sessions.

## API Endpoints

The backend FastAPI application exposes a set of RESTful and streaming endpoints to control the dataset generation pipeline, monitor progress, and manage system state. These endpoints are documented and implemented in `backend/main.py` and integrated into the frontend via the `src/api.ts` client interface.

### 🚀 Pipeline Control

- **`POST /start`**  
  Initiates a new dataset generation run. Accepts JSON payload containing the user prompt, memory facts, dataset size, deduplication settings, and other configuration parameters. Returns a unique run ID for tracking progress.

- **`GET /status/{run_id}`**  
  Retrieves the current status of a specific run, including overall progress percentage, active stage, error states, and completion time.

- **`POST /reset`**  
  Resets the system state, clearing all running processes, SSE queues, and cached data to prepare for a fresh pipeline execution.

### 📊 Real-Time Progress Streaming

- **`GET /events/{run_id}`** (Server-Sent Events)  
  Provides real-time updates on pipeline stages, model switches, log messages, and errors. The endpoint streams events using Server-Sent Events (SSE), allowing the frontend to display live progress via the `PipelineProgress` component. Implemented in `backend/streaming/sse_manager.py`.

### 🖥️ Model Management

- **`GET /models/status`**  
  Returns a list of available language models with their current status (available, busy, rate-limited), provider source, and usage metrics. Used by the `ModelDashboard` component to display real-time model availability.

- **`GET /models/usage`**  
  Provides detailed usage statistics per model, including token counts, request rates, and latency metrics for monitoring and load balancing.

### 💾 Data Retrieval

- **`GET /download/{run_id}`**  
  Generates a downloadable link (typically a presigned URL or file path) for the completed dataset in JSONL format. The response includes metadata such as sample count, scenario count, and generation duration, displayed in the `DownloadSection` component.

All endpoints are served under the `/api` prefix due to Vite proxy configuration (`vite.config.ts`) routing requests to `localhost:8005`. The API supports CORS and uses structured logging via `backend/logger/setup.py` for operational visibility.

## Configuration

### Environment Setup
The application requires a Python backend environment with FastAPI and its dependencies. To set up the backend, ensure you have Python installed and create a virtual environment. The required packages are listed in `backend/requirements.txt`, which includes:
- **FastAPI**: Web framework for building the API server
- **FAISS**: Library for efficient similarity search and clustering of dense vectors (used for deduplication)
- **Logging utilities** and **environment management tools**

Activate your virtual environment and install dependencies using:
```bash
pip install -r backend/requirements.txt
```

### Backend Configuration
The backend configuration is managed through `backend/config.py`, which defines critical settings including:
- **API keys** for various AI providers (Groq, LongCat, Cerebras, Mistral)
- **Provider base URLs** for OpenAI-compatible endpoints
- **Model configurations** with specific rate limits for each language model
- **Rate limiting parameters** to manage API usage across different providers

These configurations allow the system to route requests intelligently based on availability, usage quotas, and priority settings.

### Frontend Configuration
The frontend uses Vite as the build tool, configured in `vite.config.ts`. Key configuration points include:
- **React plugin integration** for modern React development
- **Proxy setup** that redirects API requests from `/api` to `http://localhost:8005` (matching the backend port)
- **TypeScript support** with proper module resolution

The project uses TypeScript with two separate configurations:
- `tsconfig.app.json`: Optimized for the React application with strict compilation options
- `tsconfig.node.json`: Configured for Node.js-related code with ESNext module support

### Development Scripts
The project includes several npm scripts defined in `package.json`:
- `dev`: Starts the Vite development server with hot reloading
- `build`: Creates a production build using Vite
- `preview`: Serves the built application locally
- `lint`: Runs ESLint with the configured rules for TypeScript and React

### Logging Configuration
The backend logging system is configured in `backend/logger/setup.py`, which sets up:
- **Colored log output** using the `colorlog` library for better readability
- **Structured logging format** with predefined log levels
- **Consistent formatting** across all backend components

### System Requirements
For optimal operation, ensure the following:
- **Port 8005** must be available for the FastAPI server
- **SSE (Server-Sent Events)** support is required for real-time progress updates
- **File storage directory** will be automatically created by the file manager component
- **Internet connectivity** is necessary for accessing external AI model APIs

The system is designed to run the backend server on port 8005 while serving the frontend through Vite's development server, with proper proxy configuration for seamless API communication.

## Environment Variables

The DataForge dataset generator relies on several environment variables to configure its behavior, particularly for AI model access and backend operation. These variables are essential for proper functionality and must be set before running the application.

### Required API Keys and Model Configuration

The backend requires OpenAI-compatible API keys to function with various AI providers. Based on the configuration file (`backend/config.py`), the following environment variables are critical:

- `GROQ_API_KEY`: Required for accessing Groq's language models (e.g., Llama3-8b-8192)
- `MISTRAL_API_KEY`: Needed for Mistral AI embeddings via the deduplication module
- `CEREBRAS_API_KEY`: Required for Cerebras model access
- `OPENAI_API_KEY`: Used as fallback when other providers aren't available

These keys enable the model router (`backend/models/model_router.py`) to select appropriate AI models based on availability, usage limits, and priority settings defined in the configuration.

### Backend Server Configuration

The FastAPI server runs on port 8005 by default, as specified in the run commands (`backend/run_commands.txt`). While this could potentially be configured via environment variables, the current implementation appears to use hardcoded values. However, for production deployment, it's recommended to set:

- `PORT`: To override the default port (currently 8005)
- `HOST`: To specify binding address (defaults to localhost)

### Logging and Debugging

The colored logger setup (`backend/logger/setup.py`) uses standard Python logging configuration. For enhanced debugging:

- `LOG_LEVEL`: Set to "DEBUG" for detailed logs during development
- `LOG_FILE`: Optional path to write logs to a file instead of console output

### Deduplication Configuration

The FAISS-based deduplication system (`backend/dedup/faiss_store.py`) may require:

- `DEDUP_THRESHOLD`: Similarity threshold for duplicate detection (default typically 0.8)
- `EMBEDDING_MODEL`: Override for embedding model selection (currently defaults to Mistral)

### Frontend Considerations

While the React frontend (`src/api.ts`) communicates with the backend at `localhost:8005`, no environment variables are currently exposed in the client-side code. In production deployments, you might want to set:

- `VITE_API_URL`: To point the frontend to a different backend endpoint

All environment variables should be set before starting the backend server. The application will fail to start if required API keys are missing, ensuring early detection of configuration issues.

## Project Structure

The repository follows a **monorepo** structure with a clear separation between frontend and backend components, organized to support a modern full-stack data generation platform.

### Frontend (React + Vite)
The client-side application is built using **React** with **TypeScript**, powered by **Vite** for fast development and optimized builds. The main entry point is `src/main.tsx`, which initializes the React app within `StrictMode` using the modern `createRoot` API. Global styles are defined in `src/index.css`, featuring a dark theme with custom color variables and monospace typography. The primary UI logic resides in `src/App.tsx`, orchestrating real-time pipeline monitoring and user interactions.

Key frontend components include:
- **ConfigPanel** (`src/components/ConfigPanel.tsx`) — Handles user input for prompts, memory facts, dataset size, and deduplication settings.
- **PipelineProgress** (`src/components/PipelineProgress.tsx`) — Displays real-time stage-by-stage progress, logs, and error states during data generation.
- **ModelDashboard** (`src/components/ModelDashboard.tsx`) — Shows live model status, usage metrics, and availability via polling.
- **DownloadSection** (`src/components/DownloadSection.tsx`) — Provides completion summary and download functionality once generation finishes.

These components are styled using dedicated CSS files (e.g., `ConfigPanel.css`, `PipelineProgress.css`) that implement a consistent dark UI with neon green accents and responsive layouts. The project uses ESLint for code quality (`eslint.config.js`) and TypeScript configurations split into `tsconfig.app.json` (for React) and `tsconfig.node.json` (for Node.js tools), managed under a root `tsconfig.json`.

### Backend (FastAPI + Python)
The server layer is implemented in **Python** using **FastAPI**, designed to run on **Uvicorn** at port 8005 with auto-reload enabled (as per `backend/run_commands.txt`). Dependencies are listed in `backend/requirements.txt`, including FastAPI, FAISS for similarity search, logging utilities, and environment management.

Core backend modules include:
- **main.py**: Entry point for the FastAPI app, managing the multi-stage generation pipeline and SSE streaming.
- **models/model_router.py**: Routes requests to available LLM providers (OpenAI-compatible), handling rate limits and model selection.
- **agents/**: Contains specialized agents:
  - `prompt_expander.py`: Converts raw prompts into detailed persona/task descriptions.
  - `scenario_generator.py`: Creates numbered scenario headings from approved prompts.
  - `manager_agent.py`: Oversees prompt refinement through an approval loop.
  - `dataset_generator.py`: Produces Q&A pairs in ShareGPT format with optional deduplication.
- **dedup/**: Deduplication logic powered by embeddings (`embedder.py`) and FAISS-based similarity search (`faiss_store.py`).
- **streaming/sse_manager.py**: Manages real-time event broadcasting to the frontend via Server-Sent Events.
- **storage/file_manager.py**: Handles saving/loading text, JSON, and JSONL files.
- **logger/setup.py**: Configures structured, colored logging output.

Configuration is centralized in `backend/config.py`, defining API keys, provider URLs, and model-specific rate limits. The backend communicates with the frontend via REST endpoints and SSE streams, proxied through Vite’s dev server (`vite.config.ts`).

## License

This project is licensed under the **MIT License** — a permissive open-source software license that allows you to freely use, modify, distribute, and sublicense the code, subject to the following conditions:

### Permissions
- ✅ **Commercial Use**: You are permitted to use this software in commercial applications.
- ✅ **Modification**: You may modify the source code for your own needs or contribute improvements back to the project.
- ✅ **Distribution**: You can redistribute copies of the original or modified software, including as part of larger works.
- ✅ **Private Use**: There are no restrictions on private usage.

### Limitations
- ⚠️ **Liability**: The software is provided "as is," without warranty of any kind. The authors or copyright holders shall not be held liable for damages arising from the use of this software.
- ⚠️ **Trademark Use**: This license does not grant permission to use the names, logos, or trademarks of the project or its contributors for promotional purposes without explicit written consent.

### Conditions
- 📄 **License & Copyright Notice**: All redistributions of substantial portions of the source code must retain the original copyright notice, list of conditions, and disclaimer found in the `LICENSE` file (if present) or distributed with this software.
- 📄 **State Changes**: If you modify the files, you must indicate changes made to them so that recipients know they differ from the original version.



<p align="center">Made with ❤️ by <a href="https://github.com/H0NEYP0T-466">H0NEYP0T-466</a></p>
