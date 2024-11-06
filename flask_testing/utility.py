import requests
import os
from openai import OpenAI

class Wrapper:
    def __init__(self):
        self.client = OpenAI(
            api_key = os.getenv("KEY") #get api key from openai page and set as environment variable otherwise this wont work
        )

    def ask_chat(self, content):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": content,
                }
            ]
        )
        return completion.model_dump()['choices'][0]['message']['content']