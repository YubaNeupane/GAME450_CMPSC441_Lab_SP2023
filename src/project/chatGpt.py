import openai
import os
from dotenv import load_dotenv
import json
import pyttsx3

load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

# object creation
# engine.setProperty('rate', 180)     # setting up new voice rate


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

        for event in journey['Event']:
            message += "where he got in a " + event["type"] + ' and ';
            if (event['won']):
                message += "won "
            else:
                message += "lost "
            message += "gaining " + str(event['gained']) + " coins. "

        message += ". Then, ";

    message += "write it like a joural with dear and first person. Also make it 250 words only"


    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": message
                }
            ]
    )

    print(completion.choices[0].message.content)
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


# engine.startLoop(False)


# def stopEngine():
#     engine.endLoop()

# def talkJournal(journal):
#     engine.say(journal)

# def stopTalkingJournal(journal):
#     engine.stop()

# if __name__ == '__main__':
#     talkJournal('Dear Journal,I am AI Agent and I have officially started my journey from the city of New York. My mission is to travel to the city of Pittsburgh and face any challenges that come in my way.As I left New York, I made my way towards the city of Washington. It was a long journey but my advanced programming allowed me to travel efficiently and quickly.')
#     stopEngine()