import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.types import HttpOptions

load_dotenv()
api_key: str = os.getenv("GOOGLE_API_KEY")

client = genai.Client(
    http_options=HttpOptions(api_version="v1")
)

model="gemini-2.5-flash"

response = client.models.generate_content(
    model=model,
    contents=input("Ask Gemini: "),
)

print(response.text, end="")