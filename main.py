import openai
from openai import OpenAI
# Import load_dotenv
from dotenv import load_dotenv
import requests
import os

# allows access to fields in .env folder
load_dotenv()

API_KEY = os.getenv("API_KEY")

# create an openai client
client = openai.OpenAI(api_key=API_KEY)

available_models = client.models.list()
print(available_models)

# \ load a gpt-3 model
# model = client.model("gpt-3.5-turbo-16k-0613")

#  get a response from the query
response = client.completions.create(
    engine="gpt-3",
    prompt="Who is the best Gaelic Athletic Association footballer of all time?",
    max_tokens=1000,
    temperature=0.5,
)

#  print response to console
print(response)