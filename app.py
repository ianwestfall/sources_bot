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
    'Charles Lin\'s Twisted Mind', 
    'The Brettel', 
    'The Brontel', 
    'Codex Brentenstein', 
    'Paulus Hector Mair',
    'Meyer',
    'Street Sword: Practical Use of the Long Blade for Self-Defense', 
]

BULLSHIT_SOURCES = [
    'not source-based',
    'some bullshit that Shadiversity made up and called HEMA.',
    'some HEMAism that people pass around as common knowledge even though it\'s not supported by any sources.',
    'some weird play from Talhoffer that doesn\'t make any damn sense.',
    'something that people made up and said it\'s from Liechtenauer, even though it isn\'t.',
    "something Brent made up."
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
def get_response_message(trigger_message: str) -> str:
    """
    Builds a response message
    :param trigger_message: message that triggered the event
    :return: a response message
    """
    intro = random.choice(INTROS)
    if intro == INTROS[-1]:
        response = f'{intro}that\'s {random.choice(BULLSHIT_SOURCES)}'
    else:
        response = f'{intro}that\'s in {random.choice(SOURCES)}'

    if 'brent' in trigger_message.lower():
        response = f'That\'s definitely from Charles Lin\'s Twisted Mind'

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
