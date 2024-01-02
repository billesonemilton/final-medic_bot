import os

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain.document_loaders import TextLoader 
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "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"

if __name__ == "__main__":
    while True:
        question = input("Enter a question: ")

        loader = TextLoader('training_data.txt')
        index = VectorstoreIndexCreator().from_loaders([loader])
        answer = index.query(question, llm = ChatOpenAI())

        print("Assistant: ", answer)
        
        with open('training_data.txt', "a") as ans_file:
            ans_file.write(f"\n{answer}\n")
            ans_file.write("\n")
        ans_file.close()