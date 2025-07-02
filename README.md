
# 📰 Web Article Summarizer

This Streamlit app allows you to paste a **any article URL** and get a **concise summary** with **key takeaways** using LLMs powered by [Groq](https://groq.com/).

---

## 🔍 Features

- ✅ Extract article content from any valid news URL
- ✨ Summarize articles using LLaMA 3 (via Groq API)
- 🚀 Clean and interactive Streamlit UI
- 🔄 Clear/refresh button to restart the app

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/web-article-summarizer.git
cd web-article-summarizer
```

## 📁 Project Structure

├── main.py                 # Streamlit UI code
├── data_extractor.py       # LLM summarization logic
├── requirements.txt        # Python dependencies
├── .env                    # (Excluded from GitHub) Your Groq API key
└── README.md               # Project documentation

## 🧠 Model & Tools Used

- **LLaMA 3 via Groq API** – Used for fast and accurate article summarization.
- **LangChain** – Utilized for prompt chaining and managing LLM interactions.
- **newspaper3k** – For extracting clean text content from web article URLs.
- **Streamlit** – To build an interactive and user-friendly web interface.

## 🙌 Acknowledgments

Thanks to **[Groq](https://groq.com/)**, **[LangChain](https://www.langchain.com/)**, and the amazing **open-source community** for their powerful tools and libraries that made this project possible.



