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


def generateMeJournalStory(events):
    message = "write me a short joural about AIAgent going to a joural to a city where he starts from the city \'" + events["start"] +"\'" + " and has to travel to city of \'"+ events['end'] +"\'"
    message += "as he travel and began his journey he travel to various of the cities, he travel to "

    for journey in events["journey"]:
        message += "\'"+journey["To"] + "\' from \'" + journey["From"] + "\'"

        if journey['Event'] != None:
            message += "where he got in a " + journey['Event']['type'] + ' and ';
            if (journey['Event']['won']):
                message += "won "
            else:
                message += "lost "
            message += "gaining " + str(journey['Event']['gained']) + " coins "

        message += ". Then, ";

    message += "write it like a joural with dear and first person."

    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": message
                }
            ]
    )
    return completion.choices[0].message.content;

events = {
    "start":"New york", 
    "end":"Pittsbugh", 
    "journey": [
        {
            "From": "New york",
            "To": "Washington",
            "Event": None
        },
        {
            "From": "Washington",
            "To": "Breadford",
            "Event": {
                "type": "Battle",
                "won": True,
                "gained": 2
            }
        },
        {
            "From": "Breadford",
            "To": "Pittsbugh",
            "Event": None
        },
    ]
}

print(generateMeJournalStory(events))