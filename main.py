import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

api = os.getenv("Open_Ai_key")

def main():
    client = OpenAI(api_key= api)
    response = client.chat.completions.create(
    model="gpt-4o-mini", 
     messages=[
        {"role": "user", "content": "You are a helpful assistant."},       
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ] )
    print(response.choices[0].text.strip())

main()