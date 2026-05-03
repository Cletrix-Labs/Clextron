<div align="center">

# 🤖 Clextron

### Autonomous AI Agents for Students Worldwide

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.2+-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Gemini API](https://img.shields.io/badge/Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-❤️-red?style=for-the-badge)]()

**Clextron** is an open-source platform of autonomous AI agents built for students across the globe.  
Research smarter. Study faster. Grow further - in your own language.

[🚀 Live Demo](#) · [📖 Documentation](#) · [🐛 Report Bug](https://github.com/Cletrix-Labs/Clextron/issues) · [💡 Request Feature](https://github.com/Cletrix-Labs/Clextron/issues)

---

</div>

---

## 🌟 What is Clextron?

Most AI tools make students **ask the same questions again and again.**  
Clextron is different.

Clextron runs **autonomous AI agents** that act on your behalf - researching topics, summarizing papers, building study plans, and preparing you for your career - **without you having to prompt every single step.**

> Think of it as having a team of expert AI assistants working **for you, 24/7, in your own language.**

---

## ✨ Features

| Agent | What it does |
|---|---|
|  **Research Agent** | Searches, reads, and summarizes academic topics automatically |
|  **Language Agent** | Explains any concept in 50+ languages |
|  **Study Planner Agent** | Builds a personalized study schedule based on your goals |
|  **Career Agent** *(coming soon)* | Resume review, job search, and interview prep |
|  **Quiz Agent** *(coming soon)* | Generates smart questions from your notes |

---

## 🎯 Who is this for?

-  **Engineering & CS students** who need to research fast
-  **Non-English speaking students** who want AI in their language
-  **Any student** who wants to study smarter, not harder
-  **Developers** who want to contribute to open-source AI

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Cletrix-Labs/Clextron.git
cd Clextron
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the root folder:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

>  Get your **free** Gemini API key at [aistudio.google.com](https://aistudio.google.com)

### 4. Run the app

```bash
uvicorn app:app --reload
```

Open your browser at `http://localhost:8000` - Clextron is running! 🎉

---

## 🗂️ Project Structure

```
Clextron/
│
├── agents/                  # AI agent logic
│   ├── research_agent.py    # Research & summarization agent
│   ├── language_agent.py    # Multilingual explanation agent
│   └── planner_agent.py     # Study planner agent
│
├── templates/               # HTML frontend pages
├── static/                  # CSS and JavaScript
├── modules/                 # Helper utilities
│
├── app.py                   # FastAPI main application
├── requirements.txt         # Python dependencies
├── .env                     # API keys (never commit this!)
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **FastAPI** | Backend API framework |
| **LangChain** | AI agent framework |
| **Google Gemini API** | Free AI language model |
| **python-dotenv** | Environment variable management |
| **HTML / CSS / JS** | Frontend interface |

---

## 🌍 Multilingual Support

Clextron is built for **global students**. Currently supported languages include:

`English` `Hindi` `Tamil` `Telugu` `Spanish` `French` `Portuguese` `Arabic` `Chinese` `Japanese` `Korean` `German` `Italian` `Russian` + more coming soon

---

## 🤝 Contributing

We welcome contributors of all skill levels! 

### How to contribute

1. **Fork** the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and **commit**: `git commit -m "feat: add your feature"`
4. **Push** to your branch: `git push origin feature/your-feature-name`
5. Open a **Pull Request**

### Good first issues

Look for issues tagged [`good-first-issue`](https://github.com/Cletrix-Labs/Clextron/issues?q=label%3Agood-first-issue) - perfect for beginners!

Please read our [Contributing Guide](CONTRIBUTING.md) before submitting.

---

## 📋 Roadmap

- [x] Project setup and structure
- [x] Research Agent (v1)
- [ ] Multilingual language support
- [ ] Study Planner Agent
- [ ] Career Agent
- [ ] Quiz Generator Agent
- [ ] Web UI (HTML/CSS frontend)
- [ ] Deploy to Render.com
- [ ] Mobile-friendly interface
- [ ] Agent memory (remembers your progress)

---

## 📸 Screenshots

>  Screenshots coming soon as the UI is built!

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com) - for the amazing agent framework
- [Google Gemini](https://aistudio.google.com) - for the free AI API
- [FastAPI](https://fastapi.tiangolo.com) - for the blazing fast backend
- Every student who inspired this project 💙

---

<div align="center">

**Built with ❤️ by [Cletrix Labs](https://github.com/Cletrix-Labs)**

⭐ If you find this useful, **star the repo** - it helps more students find it!

[![GitHub stars](https://img.shields.io/github/stars/Cletrix-Labs/Clextron?style=social)](https://github.com/Cletrix-Labs/Clextron/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Cletrix-Labs/Clextron?style=social)](https://github.com/Cletrix-Labs/Clextron/network/members)

</div>