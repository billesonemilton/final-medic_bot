from flask import Flask, render_template, request
import os
import sys
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

app = Flask(__name__)

@app.route('/index3')
def index():
    return render_template('index3.html')

@app.route('/chat', methods=['POST'])
def chat():
    question = request.form['question']

    loader = TextLoader('training_data.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    answer = index.query(question, llm=ChatOpenAI())

    return render_template('index3.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
