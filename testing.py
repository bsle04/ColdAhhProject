import os
from openai import OpenAI

client = OpenAI(
  api_key = os.getenv("OPENAI_API_KEY") #get api key from openai page and set as environment variable otherwise this wont work
)

content = input("Ask something: ")
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": content,
        }
    ]
)

print(completion.model_dump()['choices'][0]['message']['content'])
