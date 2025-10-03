import os
from openai import OpenAI
client = OpenAI(
    api_key="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"
)

response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

#etc etc for chatbot with gemini