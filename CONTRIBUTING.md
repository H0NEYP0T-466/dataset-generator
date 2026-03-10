# Contributing to H0NEYP0T-466/dataset-generator

🎉 Welcome, and thank you for your interest in contributing to **DataForge — LLM Dataset Generator**!  
We're building a powerful tool that enables developers and researchers to generate high-quality, deduplicated datasets for fine-tuning large language models. Your contributions help make this project more robust, user-friendly, and accessible.

Whether you're fixing bugs, adding features, improving documentation, or reporting issues — every contribution matters!

---

## 🚀 How to Get Started

1. **Fork the repository**  
   Click the "Fork" button at the top-right of this repo to create your own copy.

2. **Clone your fork locally**
   ```bash
   git clone https://github.com/your-username/dataset-generator.git
   cd dataset-generator
   ```

3. **Set up the development environment**

   ### Backend (Python)
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

   ### Frontend (TypeScript + React + Vite)
   ```bash
   npm install
   ```

4. **Run the application**
   - In one terminal (backend):
     ```bash
     uvicorn main:app --reload --port 8005
     ```
   - In another terminal (frontend):
     ```bash
     npm run dev
     ```

   Visit [http://localhost:5173](http://localhost:5173) to see the app in action!

> 💡 Tip: Use `run_commands.txt` in the `backend/` folder for quick reference on running the server.

---

## 🐞 Reporting Bugs

Found a bug? Help us squash it faster by filing a detailed issue!

### Before submitting:
- Check existing issues to avoid duplicates.
- Ensure you're using the latest version.

### Include in your bug report:
- ✅ Steps to reproduce
- ✅ Expected vs actual behavior
- ✅ Screenshots (if applicable)
- ✅ Browser/OS info (for frontend issues)
- ✅ Backend logs (from `uvicorn` output)
- ✅ Relevant environment details:
  - Python version (`python --version`)
  - Node.js & npm versions
  - API keys / config used (redact secrets!)

👉 Use the **Bug Report** template when creating an issue.

---

## 💡 Suggesting Features or Enhancements

Have an idea to improve DataForge? We'd love to hear it!

- Open an issue with the **Feature Request** label.
- Describe:
  - What problem it solves
  - Why it’s valuable
  - Any implementation ideas (optional)

We encourage early discussion — don’t worry about getting everything perfect upfront!

---

## 🔄 Pull Request Process

We follow a clean and collaborative PR workflow:

### 1. Create a Feature Branch
```bash
git checkout -b feat/add-new-agent-type
# or
git checkout -b fix/sse-connection-leak
```

Use clear prefixes:
- `feat/` – new functionality
- `fix/` – bug fixes
- `docs/` – documentation
- `refactor/` – code improvements
- `test/` – test additions

### 2. Make Your Changes
- Follow our [code style](#code-style-and-quality-expectations).
- Write tests if applicable.
- Update documentation as needed.

### 3. Commit Messages
Keep them concise and meaningful:
```
feat(agents): add memory injection to scenario generator
fix(storage): handle missing dir creation in file_manager
```

### 4. Push & Open a PR
Push your branch:
```bash
git push origin feat/add-new-agent-type
```

Then open a Pull Request against `main`.

### 5. PR Description Template
Please include:
- Summary of changes
- Related issue(s) (e.g., `Closes #123`)
- Testing steps performed
- Screenshots (if UI changed)

Our maintainers will review within a few days.

> ⚠️ PRs without tests or clear context may take longer to merge.

---

## 🧼 Code Style and Quality Expectations

We aim for clean, maintainable, and consistent code across both frontend and backend.

### General Guidelines:
- **Readability over cleverness**: Favor clarity.
- **Consistent naming**: snake_case for Python, camelCase for TypeScript.
- **No hardcoded secrets**: Use `.env` or config files.
- **Modular design**: Keep components and modules focused.

### Backend (Python)
- Follow [PEP 8](https://pep8.org/)
- Use type hints where possible
- Async/await patterns preferred
- Log meaningful messages via `logger.setup`

### Frontend (TypeScript + React)
- Use functional components with hooks
- Leverage TypeScript strictly (`tsconfig.app.json` enforces strict mode)
- Follow React best practices (avoid unnecessary re-renders, use proper memoization)
- CSS-in-JS or scoped styles encouraged; global styles only when necessary

### Linting & Formatting
Both projects use ESLint:
- Run linter before committing:
  ```bash
  # Frontend
  npm run lint

  # Backend (add to requirements if not present)
  flake8 .
  ```

Auto-fixable issues can be resolved with:
```bash
npm run lint:fix
```

---

## ✅ Running Tests & Linting

Currently, automated tests are minimal but growing. We welcome test contributions!

### Linting
Ensure your code passes checks:
```bash
# Frontend
npm run lint

# Backend (install flake8 if needed)
pip install flake8
flake8 backend/
```

### Manual Testing Tips
- Test prompt expansion with edge cases
- Verify SSE stream integrity during long runs
- Confirm deduplication works with sample data
- Validate file downloads and metadata display

Add unit/integration tests under appropriate folders when feasible.

---

## 📜 Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).  
By participating, you agree to foster an open, inclusive, and respectful community.

Report unacceptable behavior to the maintainer team.

---

## 🙌 Recognition & Attribution

We believe in giving credit where it's due!

- Contributors will be acknowledged in release notes.
- Major contributors may be invited to join as collaborators.
- All pull requests and commits reflect the original author’s effort.

Thank you for helping shape DataForge into a better tool for the AI community!

---

Happy coding! 🤖✨