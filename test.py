# from dotenv import load_dotenv
# import os
# from pydantic import BaseModel
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import PydanticOutputParser
# from langchain_core.tools import tool
# import google.generativeai as genai
# import json

# # Load environment variables
# load_dotenv()

# # Define a simple Gemini LLM wrapper
# class GeminiLLM:
#     def __init__(self, model_name="gemini-1.5-pro"):
#         self.model_name = model_name
#         api_key = os.getenv("GEMINI_API_KEY")
#         if not api_key:
#             raise ValueError("GEMINI_API_KEY not found in environment variables")
#         genai.configure(api_key=api_key)
#         self.model = genai.GenerativeModel(self.model_name)

#     def call(self, messages):
#         try:
#             contents = []
#             for msg in messages:
#                 if msg["role"] == "user":
#                     contents.append({"role": "user", "parts": [{"text": msg["content"]}]})
#                 elif msg["role"] == "assistant":
#                     contents.append({"role": "model", "parts": [{"text": msg["content"]}]})
#                 else:
#                     raise ValueError(f"Unsupported role: {msg['role']}")

#             response = self.model.generate_content(
#                 contents=contents,
#                 generation_config={
#                     "temperature": 0.7,
#                     "top_p": 0.9,
#                     "max_output_tokens": 1000
#                 }
#             )

#             return {"role": "assistant", "content": response.text}

#         except Exception as e:
#             print(f"Error in GeminiLLM call: {e}")
#             return {"role": "assistant", "content": f"Error: {str(e)}"}

# # Example usage
# if __name__ == "__main__":
#     llm = GeminiLLM(model_name="gemini-1.5-pro")
#     messages = [
#         {"role": "user", "content": "Hello, how can you help me today?"}
#     ]
#     response = llm.call(messages)
#     print("Response:", response)

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Gemini API wrapper
class GeminiLLM:
    def __init__(self, model_name="gemini-1.5-pro"):
        self.model_name = model_name
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(self.model_name)

    def ask(self, user_input):
        try:
            response = self.model.generate_content(
                contents=[{"role": "user", "parts": [{"text": user_input}]}],
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "max_output_tokens": 1000
                }
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

# Main loop
if __name__ == "__main__":
    llm = GeminiLLM()
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit", "q"]:
            print("Exiting...")
            break
        answer = llm.ask(question)
        print("Gemini:", answer)
