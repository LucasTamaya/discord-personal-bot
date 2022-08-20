from vocal_assistant import talk, listen
from discord import get_messages, send_message


def start_bot():
    message = listen()
    if "récupère les messages" in message:
        print("Bot: Message en cours de récupération...")
        get_messages()
    if "envoie un message" in message:
        print("Bot: J'écoute pour envoyer un message")
        talk("J'écoute pour envoyer un message")
    


while True:
    start_bot()
