import os
import sys

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