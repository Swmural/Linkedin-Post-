import os

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import openai


# The OpenAI API can be applied to virtually any task that involves understanding or generating natural language, code, or images

# Steps to get the OpenAI API Key

# 1. Go to the OpenAI website and sign up for an account if you haven't already.
# 2. Navigate to the "API Keys" tab in your OpenAI dashboard.
# 3. Click on the "Generate New Key" button.
# 4. Give your API key a name and choose the permissions you want to grant.
# 5. Click on the "Generate API Key" button.
# 6. Your new API key will be displayed on the screen. Make sure to copy it and store it
# 7. Update your card details, only then your API KEY will work
apiKey = input("Please enter your OpenAI API Key:")

os.environ["OPENAI_API_KEY"] = apiKey

# This is where we get the input from the user
apiInput = input("Please give the Input to generate a LinkedIn post with image? ")

# Large Language Model (LLM) AI is a term that refers to AI models that can generate natural language texts from large amounts of data.

# we are sending temperature as 0.1, as a parameter to the OpenAI AI class. 
# This parameter controls how "creative" the model's responses are.
# eg :0.1 is less creative and 0.9 is more creative
# It wont be exceeding 1.0
llm = OpenAI(temperature=0.1)


# i got the input from the user and then i am calling the 
#llm chain,which takes the prompt as the input and then it generates it into random Text

# I am just creating the prompt template, which is a way to create a natural language prompt with placeholders for variables.
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate a LinkedIn post about {topic}",
)

# The LLMChain is a simple chain that takes in a prompt template, formats it with the user input and returns the response from an LLM
chain = LLMChain(llm=llm, prompt=prompt)

# The DALL-E API is a generative AI model developed by Open AI that can generate images and art from a text prompt
# Calling OpenAI's DALL-E API with required input parameters to get the image url
openai.api_key = os.getenv("OPENAI_API_KEY")

# Dall-E API, which takes the prompt as the input and then it generates it into random image

response = openai.Image.create(
    prompt="Random picture of a" + apiInput,
    n=1,
    size="500x500",
)


# Generate a LinkedIn post
# 1. We run the chain here with the input
# 2. From the response, we get the image url
# 3. And then, just combined it, so that it looks like a linkedIn post!

print(chain.run(apiInput) + "\n" + response["data"][0]["url"])





