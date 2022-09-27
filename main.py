from vocal_assistant import talk, listen
from discord import get_messages, send_message

discord_channel_id = "DISCORD_PRIVATE_MSG_ID"


def start_bot():
    print("Bot: Vous pouvez commencer à parler")
    talk("Vous pouvez commencer à parler")
    while True:
        content = listen()
        talk(content)
        if "récupère les messages" in content:
            print("Bot: Message en cours de récupération...")
            get_messages(discord_channel_id)
        if "réponse au message" in content:
            print("Bot: J'écoute pour envoyer un message")
            message = content.replace("réponse au message", "")
            print(message)
            send_message(discord_channel_id, message)
        if ("stopper le robot" in content):
            print("Bot: En cours d'arrêt")
            talk("Robot en cours d'arrêt")
            return


start_bot()
