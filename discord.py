import requests
import json
from decouple import config

from vocal_assistant import talk, listen

AUTHORIZATION = config('AUTHORIZATION')
headers = {
    'authorization': AUTHORIZATION
}


# envoit un message sur discord
def send_message(channel_id, message):

    payload = {
        'content': message
    }
    r = requests.post(
        f'https://discord.com/api/v9/channels/{channel_id}/messages', data=payload, headers=headers)

# récupère des messages sur discord
def get_messages(channel_id):  
    r = requests.get(
        f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    data = json.loads(r.text,)
    contents = []
    for value in data:
        # récupère uniquement les messages du destinataire dans un tableau
        if ("Lucas T" in value["author"]["username"]):
            pass
        else:
            contents.append(value["content"])
    # lecture du dernier message
    talk(contents[0])

    # enregistrement de ma réponse
    message = listen()

    # envoit du message
    send_message(channel_id, message)
