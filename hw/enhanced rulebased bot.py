import re
import random
from colorama import Fore, init

init(autoreset=True)

international_trips = {
    "europe": ["Paris", "Rome", "Barcelona"],
    "asia": ["Tokyo", "Bali", "Singapore"],
    "africa": ["Marrakech", "Cape Town", "Nairobi"],
    "america": ["New York", "Rio de Janeiro", "Toronto"],
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travellers always feel warm? Because of all their hot spots!",
]

faq = {
    "what is your name": "I'm TravelBot, your travel guide!",
    "where can i go": "You can ask me for internations trips of different states.",
    "best time to visit": "It depends on the place, but spring and autumn are often great seasons.",
    "do i need a visa": "Visa rules depend on your nationality and destination.",
    "how much money should i carry": "Bring a mix of cash and cards, and check local costs.",
    "weather": "I can help you plan for the weather, but you should also check the local forecast.",
}


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def recommend():
    print(Fore.CYAN + "TravelBot: Where can I go visit? Choose Europe, Asia, Africa, or America.")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in international_trips:
        suggestion = random.choice(international_trips[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = normalize_input(input(Fore.YELLOW + "You: "))

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy your trip to {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another one.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I will suggest something else.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that international trip option.")


def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")


def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest international travel spots (say 'recommendation' or 'recommend')")
    print(Fore.GREEN + "- Tell a joke (say 'joke' or 'funny')")
    print(Fore.GREEN + "- Answer travel questions like visa, budget, or weather")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")


def answer_question(user_input):
    for key, value in faq.items():
        if key in user_input:
            print(Fore.BLUE + f"TravelBot: {value}")
            return True
    return False


def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "What is your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif answer_question(user_input):
            pass
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Adios!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase that?")


if __name__ == "__main__":
    chat()
