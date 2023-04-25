import os

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import openai


from flask import Flask, Response, request, json

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/text_linkedIn_generator', methods=['GET'])
def text_to_image_converter():
  data = request.json
  
  if data is None or data == {}:
    return Response(response=json.dumps({"Error": "Please provide post information"}),
                        status=400,
                        mimetype='application/json')
  OpenAI.api_key = os.getenv('OPENAI_API_KEY')
  
  api_input = data['text']
  image_size = data['size']

  response = {}
  
  llm = OpenAI(temperature=0.1)

  prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a LinkedIn post about {topic} with an image of size 512 x 512",
    )
  
  chain = LLMChain(llm=llm, prompt=prompt)

  
  llm_output = chain.run(api_input)
  
  response = openai.Image.create(
    prompt= llm_output,
    n=1,
    size= image_size,
  )
  
  response.data[0]['content'] = llm_output
  
  return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
