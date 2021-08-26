import os
import random
from functools import lru_cache

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise Exception('Missing required env var DISCORD_TOKEN')

INTROS = [
    'Oh yea, ',
    'I think ',
    'Definitely, ',
    'Yes actually, ',
    'As I recall, ',
    'No, ',
]

SOURCES = [
    'Liechtenauer',
    'Fiore dei Liberi',
    'Peter von Danzig',
    'Jude Lew',
    'I.33',
    'The Zettel',
    'Codex Wallerstein',
    'Norwood\'s TTRPG',
    'Paulus Hector Mair',
    'Meyer',
    'Street Sword: Practical Use of the Long Blade for Self-Defense', 
]

TRIGGER_WORDS = [
    'sources',
    'source-based',
    'source based',
]

client = discord.Client()


def do_i_care(message: str) -> bool:
    """
    Checks if the received message should trigger a bot response
    :param message:
    :return: True if the bot cares about the message, False otherwise
    """
    for trigger in TRIGGER_WORDS:
        if trigger in message.lower():
            return True
    return False


@lru_cache(maxsize=1024)
def get_response_message(_: str) -> str:
    """
    Builds a response message
    :param _: cache key, otherwise unused
    :return: a response message
    """
    intro = random.choice(INTROS)
    if intro == INTROS[-1]:
        response = f'{intro}that isn\'t source-based'
    else:
        response = f'{intro}that\'s in {random.choice(SOURCES)}'
    return response


@client.event
async def on_ready():
    """
    Fired when the bot connects to Discord
    """
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    """
    Fired when a message is posted where the bot can see it
    """
    if message.author == client.user:
        return

    if do_i_care(message.content):
        await message.channel.send(get_response_message(message.content))


client.run(TOKEN)
