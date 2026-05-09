# Contributing to Clextron

Thank you for your interest in contributing to Clextron.

## Getting Started

1. Fork the repository.
2. Clone your fork:
   
   git clone https://github.com/<your-username>/Clextron.git
   cd Clextron
3. Create a branch:
   
   git checkout -b feature/your-feature-name
4. Install dependencies:
   
   pip install -r requirements.txt
5. Run the app:
   
   uvicorn app:app --reload

## Development Guidelines

- Keep changes focused and small.
- Follow existing Python style and naming.
- Add or update tests where possible.
- Do not commit secrets (for example, `.env`).

## Commit Messages

Use clear commit messages with a prefix:

- feat: new feature
- fix: bug fix
- chore: maintenance task
- docs: documentation update

Example:

feat: add language selector to research form

## Pull Requests

Before opening a PR, make sure:

1. Code runs locally without errors.
2. API endpoints are tested.
3. README or docs are updated if needed.
4. Your PR description explains what changed and why.

## Reporting Issues

When opening an issue, include:

- A clear title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Logs or screenshots if useful

## Code of Conduct

Be respectful and constructive. We welcome contributors of all experience levels.
