# # import os
# # import requests

# # from langchain.prompts import PromptTemplate
# # from langchain.llms import OpenAI
# # from langchain.chains import LLMChain
# # import openai


# # # Steps to get the OpenAI API Key
# # # ...

# # apiKey = input("Please enter your OpenAI API Key:")

# # os.environ["OPENAI_API_KEY"] = apiKey

# # # This is where we get the input from the user
# # apiInput = input("Please give the Input to generate a LinkedIn post with an image: ")
# # imageType = input("Please choose the image type (png/gif): ")
# # postText = input("Please enter the text for the LinkedIn post: ")

# # # Large Language Model (LLM) AI is a term that refers to AI models that can generate natural language texts from large amounts of data.

# # # ...

# # llm = OpenAI(temperature=0.9)

# # # ...

# # prompt = PromptTemplate(
# #     input_variables=["topic"],
# #     template="Generate a LinkedIn post about {topic}",
# # )

# # # ...

# # chain = LLMChain(llm=llm, prompt=prompt)

# # # ...

# # openai.api_key = os.getenv("OPENAI_API_KEY")

# # # DALL-E API, which takes the prompt as the input and then it generates it into random image
# # response = openai.Image.create(
# #     prompt="Random {} image of a {}".format(imageType.upper(), chain.run(apiInput)),
# #     n=1,
# #     size="256x256",
# #     response_format="url",
# # )

# # # Display the post text and image URL
# # print(postText)
# # print("Image URL:", response["data"][0]["url"])





# import os
# import requests

# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# import openai


# # Steps to get the OpenAI API Key
# # ...

# apiKey = input("Please enter your OpenAI API Key:")

# os.environ["OPENAI_API_KEY"] = apiKey

# # This is where we get the input from the user
# apiInput = input("Please give the Input to generate a LinkedIn post with an image: ")
# imageType = input("Please choose the image type (png/gif): ")
# postText = input("Please enter the text for the LinkedIn post: ")

# # Large Language Model (LLM) AI is a term that refers to AI models that can generate natural language texts from large amounts of data.

# # ...

# llm = OpenAI(temperature=0.9)

# # ...

# prompt = PromptTemplate(
#     input_variables=["topic", "text"],
#     template="{text} Generate a LinkedIn post about {topic}",
# )

# # ...

# chain = LLMChain(llm=llm, prompt=prompt)

# # ...

# openai.api_key = os.getenv("OPENAI_API_KEY")

# # DALL-E API, which takes the prompt as the input and then it generates it into random image
# response = openai.Image.create(
#     prompt="Random {} image of a {}".format(imageType.upper(), chain.run(topic=apiInput, text=postText)),
#     n=1,
#     size="256x256",
#     response_format="url",
# )

# # Display the generated text and image URL
# print(chain.run(topic=apiInput, text=postText))
# print("Image URL:", response["data"][0]["url"])
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
apiInput = input("Please give the Input to generate a LinkedIn post based on your request: ")
imageType = input("Please choose the image type example (png/gif): ")
postText = input("Please enter the input text based on what text you want : ")

# Large Language Model (LLM) AI is a term that refers to AI models that can generate natural language texts from large amounts of data.

llm = OpenAI(temperature=0.9)


prompt = PromptTemplate(
    input_variables=["topic", "text"],
    template="{text} Generate a LinkedIn post about {topic}",
)


chain = LLMChain(llm=llm, prompt=prompt)


openai.api_key = os.getenv("OPENAI_API_KEY")

# DALL-E API, which takes the prompt as the input and then it generates it into random image
response = openai.Image.create(
    prompt="Random {} image of a {}".format(imageType.upper(), chain.run(topic=apiInput, text=postText)),
    n=1,
    size="1024x1024",  # Increase the image size
    response_format="url",
)

# Display the generated text and image URL
generated_text = chain.run(topic=apiInput, text=postText)
image_url = response["data"][0]["url"]

print("Image URL:", generated_text)
print("Image URL:", image_url)

# Display the image in a new web page
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated LinkedIn Post</title>
</head>
<body>
    <h2>Generated LinkedIn Post:</h2>
    <p>{generated_text}</p>
    <img src="{image_url}" alt="Generated Image">
</body>
</html>
"""

with open("generated_post.html", "w") as file:
    file.write(html_content)

# Open the HTML file in the default web browser
import webbrowser
webbrowser.open("generated_post.html")
