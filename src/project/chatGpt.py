import openai
import os
from dotenv import load_dotenv
import json


load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

def generateCityNames(numberOfCities):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
             "content": "give me a unique" + str(numberOfCities) +" city names based on a fantasy theme, output it in a json array, don't even say anything before it to expalin it or after it, just give me the json array."
            }
        ]
    )
    
    return json.loads(completion.choices[0].message.content)

