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
    'No, ',
    'No, ',
    'No, ',
    'No, ',
]

SOURCES = [
    'Liechtenauer',
    'Fiore dei Liberi',
    'Peter von Danzig',
    'Jude Lew and his beautiful ass art',
    'Ringeck',
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
    'George Silver, unfortunately',
    'Michael Hundt',
    'Hutton',
    'Roworth',
    'Capo Ferro',
    'Giganti',
    'Fabris',
    'Thibault',
    'Le Jeu de la Hache',
    'Hans Medel',
    'Paurnfeyndt',
    '3227a',
    '3227a, but specifically the part with all the magic spells',
    'A recently-discovered, anonymous Liechtenauer gloss where the schaitelhau actually works',
    'Vadi',
    'Kendo',
    'Foil',
    'Epee',
    'The Ledall Roll, but that\'s a terrible source so it barely counts',
    'a book I once found in a cardboard box full of porn in the forest'
]

BULLSHIT_SOURCES = [
    'not source-based.',
    'some bullshit that Shadiversity made up and called HEMA.',
    'some HEMAism that people pass around as common knowledge even though it\'s not supported by any sources.',
    'some weird play from Talhoffer that doesn\'t make any damn sense. That\'s right, Talhoffer is not a real source.',
    'something that people made up and said it\'s from Liechtenauer, even though it isn\'t.',
    'something that Brent made up as a joke.',
    'on the same level of HEMA as Polish saber or Viking combat, which is to say that it\'s not HEMA.',
    'the equivalent of people claiming to do \"Byzantine longsword\" or \"Dane axe combat\" or something like that, aka a bunch of bullshit that they made up.',
    'the delusional ramblings of LindyBeige using \"logic\" and \"reason\" to invent some completely ahistorical combat system using whatever works for him, with no academic rigor or actual historical sources involved whatsoever.',
    'some whack-a-doodle martial fantasy nonsense made up by someone who unironically thinks too much about what they would do in a Real Sword Fight.',
    'not HEMA. That\'s an Ash of War from Elden Ring.',
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
    if intro == 'No, ':
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
