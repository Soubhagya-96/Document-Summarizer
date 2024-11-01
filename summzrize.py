import sys

from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (HumanMessage, SystemMessage)

load_dotenv()

try:
    # make sure the pdf is a text pdf
    filename = sys.argv[1]
    pdfreader = PdfReader(filename)
    text = ''

    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            text += content

    chat_messages=[
        SystemMessage(content='You are an expert assistant with expertize in summarizing text'),
        HumanMessage(content=f'Please provide a short and concise summary of the following text:\n TEXT: {text}')
    ]

    # you can use any other Open-AI model if you have the access to it
    llm=ChatOpenAI(model_name='gpt-3.5-turbo')
    summary = llm(chat_messages).content
    print("\nSummary:\n\n")
    print(summary)

except Exception as e:
    print("Error occured:\n", str(e))
