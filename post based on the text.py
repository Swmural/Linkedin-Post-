import os
import requests

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import openai


# Steps to get the OpenAI API Key
# ...

apiKey = input("Please enter your OpenAI API Key:")

os.environ["OPENAI_API_KEY"] = apiKey

# This is where we get the input from the user
apiInput = input("Please give the Input to generate a LinkedIn post with an image: ")
imageType = input("Please choose the image type (png/gif): ")

# Large Language Model (LLM) AI is a term that refers to AI models that can generate natural language texts from large amounts of data.

# ...

llm = OpenAI(temperature=0.9)

# ...

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate a LinkedIn post about {topic}",
)

# ...

chain = LLMChain(llm=llm, prompt=prompt)

# ...

openai.api_key = os.getenv("OPENAI_API_KEY")

# DALL-E API, which takes the prompt as the input and then it generates it into random image
response = openai.Image.create(
    prompt="Random {} image of a {}".format(imageType.upper(), chain.run(apiInput)),
    n=1,
    size="256x256",
    response_format="url",
)

# Generate a LinkedIn post
# 1. We run the chain here with the input
# 2. From the response, we get the image url
# 3. And then, just combine it, so that it looks like a LinkedIn post with an image!
print(response["data"][0]["url"])
