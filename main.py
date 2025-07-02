

# Title
import streamlit as st
from newspaper import Article
from data_extractor import summarize_article

def main():
    st.title("📰 Web Article Summarizer")
    st.write("Paste a news article URL and get a concise summary with key takeaways.")

    # Input field
    url = st.text_input("Enter URL here:")

    # Buttons
    col1, col2 = st.columns([1, 1])
    submit_clicked = col1.button("Summarize")
    
   

    # Handle Submit
    if submit_clicked and url:
        with st.spinner("Extracting article..."):
            try:
                article = Article(url)
                article.download()
                article.parse()
                article_text = article.text
                if len(article_text) < 100:
                    st.warning("Article text too short or could not be extracted properly.")
                    return
            except Exception as e:
                st.error(f"Error extracting article: {e}")
                return

        with st.spinner("Generating summary..."):
            summary = summarize_article(article_text)

        st.subheader("Summary")
        st.write(summary)

if __name__ == "__main__":
    main()

