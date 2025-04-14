from dotenv import load_dotenv
import os

load_dotenv()  # يحمل ملف .env تلقائيًا

print("GEMINI_KEY:", os.getenv("GEMINI_API_KEY"))
print("GEMINI_SECRET:", os.getenv("GEMINI_API_SECRET"))
