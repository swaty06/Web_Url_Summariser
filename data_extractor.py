from langchain_groq import ChatGroq
from newspaper import Article
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile")


# Mock function to extract financial data (replace with actual function)
def summarize_article(article_text):
    prompt = '''
Summarize the following news article in 3-4 concise sentences.  
Provide key takeaways as bullet points.

Article
=======
{article}
    '''
    pt = PromptTemplate.from_template(prompt)
    chain = LLMChain(llm=llm, prompt=pt)

    try:
        response = chain.run(article=article_text)
        return response.strip()
    except OutputParserException as e:
        return f"Error during summarization: {str(e)}"
