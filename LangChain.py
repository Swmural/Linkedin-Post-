import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import requests

os.environ["OPENAI_API_KEY"] = "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"
apiInput = input("Please give the Input to generate a LinkedIn post with image? ")

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate a LinkedIn post about {topic}",
)

chain = LLMChain(llm=llm, prompt=prompt)

# Generate the image using OpenAI's DALL-E API
response = requests.post(
    "https://api.openai.com/v1/images/generations",
    headers={"Authorization": "Bearer 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"},
        json={
        "model": "image-alpha-001",
        "prompt": "Random picture of a" + apiInput,
        "num_images": 1,
        "size": "512x512",
        "response_format": "url"
    }
)

# Generate a LinkedIn post
print(chain.run(apiInput) + "\n" + response.json()["data"][0]["url"])
