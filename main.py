import google.generativeai as ai
import random
import json

API_KEY = 'AIzaSyDPbYoOP_ANE5DmJuz-Q5MURQqQCflUk8M'
ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

def pirate_translate(text):
    translations = {
        "hello": "ahoy",
        "hi": "ahoy",
        "my": "me",
        "friend": "matey",
        "friends": "me hearties",
        "is": "be",
        "am": "be",
        "are": "be",
        "yes": "aye",
        "no": "nay",
        "stop": "avast",
        "wait": "belay",
        "left": "port",
        "right": "starboard",
        "where": "whar",
        "you": "ye",
        "your": "yer",
        "you are": "ye be",
        "old": "barnacle-covered",
        "the": "th'",
        "of": "o'",
        "I": "meself",
        "I'm": "I be",
        "money": "doubloons",
        "treasure": "booty",
        "for": "fer",
        "look": "spy",
        "man": "buccaneer",
        "woman": "wench",
        "kids": "lil' scallywags",
        "cannon": "blunderbuss",
        "ship": "vessel",
        "drink": "grog",
        "rum": "rum",
        "wine": "pirate's nectar",
        "beer": "swill",
        "eat": "feast",
        "food": "grub",
        "captain": "cap'n",
        "sailor": "seadog",
        "crew": "crew",
        "head": "noggin",
        "leg": "pegleg",
        "hand": "hook",
        "eye": "spyglass",
        "sword": "cutlass",
        "battle": "scuffle",
        "fight": "brawl",
        "storm": "tempest",
        "sea": "briny deep",
        "shore": "shoreline",
        "enemy": "bilge rat",
        "victory": "plunder",
        "escape": "sail away",
        "danger": "peril",
        "goodbye": "fare thee well",
        "me": "me",
        "we": "we",
        "they": "they",
        "them": "them",
        "us": "us",
        "him": "him",
        "her": "her",
        "it": "it",
        "this": "this",
        "that": "that",
        "these": "these",
        "those": "those",
        "Hello": "Ahoy",
        "Hi": "Ahoy",
        "My": "Me",
        "Friend": "Matey",
        "Friends": "Me Hearties",
        "Is": "Be",
        "Am": "Be",
        "Are": "Be",
        "Yes": "Aye",
        "No": "Nay",
        "Stop": "Avast",
        "Wait": "Belay",
        "Left": "Port",
        "Right": "Starboard",
        "Where": "Whar",
        "You": "Ye",
        "Your": "Yer",
        "You Are": "Ye Be",
        "Old": "Barnacle-covered",
        "The": "Th'",
        "Of": "O'",
        "Money": "Doubloons",
        "Treasure": "Booty",
        "For": "Fer",
        "Look": "Spy",
        "Man": "Buccaneer",
        "Woman": "Wench",
        "Kids": "Lil' Scallywags",
        "Cannon": "Blunderbuss",
        "Ship": "Vessel",
        "Drink": "Grog",
        "Rum": "Rum",
        "Wine": "Pirate's Nectar",
        "Beer": "Swill",
        "Eat": "Feast",
        "Food": "Grub",
        "Captain": "Cap'n",
        "Sailor": "Seadog",
        "Crew": "Crew",
        "Head": "Noggin",
        "Leg": "Pegleg",
        "Hand": "Hook",
        "Eye": "Spyglass",
        "Sword": "Cutlass",
        "Battle": "Scuffle",
        "Fight": "Brawl",
        "Storm": "Tempest",
        "Sea": "Briny Deep",
        "Shore": "Shoreline",
        "Enemy": "Bilge Rat",
        "Victory": "Plunder",
        "Escape": "Sail Away",
        "Danger": "Peril",
        "Goodbye": "Fare Thee Well",
        "Me": "Me",
        "We": "We",
        "They": "They",
        "Them": "Them",
        "Us": "Us",
        "Him": "Him",
        "Her": "Her",
        "It": "It",
        "This": "This",
        "That": "That",
        "These": "These",
        "Those": "Those"
    }

    for word, pirate_word in translations.items():
        text = text.replace(word, pirate_word)

    return text

def is_monkey_island_question(text):
    with open('Monkey_Island.json', 'r') as file:
        keywords = json.load(file)['keywords']
    return any(keyword in text.lower() for keyword in keywords)

def is_greeting(text):
    greetings = ["ahoy", "hello", "hi", "greetings", "hey"]
    return any(greeting in text.lower() for greeting in greetings)

def random_greeting_response():
    responses = [
        "Ahoy! I be at yer service to answer questions about Monkey Island!",
        "Ahoy there! Ye've found the right pirate for Monkey Island queries!",
        "Greetings, matey! Ask me anythin' about Monkey Island, and I'll be glad to help!",
        "Hey ho! I'm ready to answer all yer Monkey Island questions, arr!",
        "Ahoy, matey! What Monkey Island mysteries can I help ye solve today?"
    ]
    return random.choice(responses)

while True:
    message = input('Ye: ')
    if message.lower() == 'bye':
        print('Chatbot: Fare thee well!')
        break
    if is_greeting(message):
        print('Chatbot:', random_greeting_response())
    elif is_monkey_island_question(message):
        response = chat.send_message(message)
        pirate_response = pirate_translate(response.text)
        print('Chatbot:', pirate_response)
    else:
        print("Chatbot: Arrr, I only be answerin' questions about Monkey Island, matey!")
