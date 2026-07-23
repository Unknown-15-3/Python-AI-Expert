import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ['Bali', 'Maldives', 'Phuket'],
    "mountains": ['Swiss Alps', 'Rocky Mountains', 'Himalayas'],
    "cities": ['Tokyo', 'Paris', 'New york'],
}

jokes = [
    "Why don't programmers like nature? Too many bugs"
    "Why did the computer go to the doctor? Because it had a virus!"
    "Why do travellors always feel warm? Because of all of there hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())
def recommend():
    print(Fore.CYAN + "Travel.Bot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You:")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: how about {suggestion}")
        print(Fore.CYAN + "TravelBot: do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! enjoy{suggestion}!")
        elif answer== "no":
            print(Fore.RED + "TravelBot: lets try another")
            recommend()
        else:
            print(Fore.RED + "TravelBot: i will suggest something else")
            recommend()
    else:
        print(Fore.RED + "Travel:Bot sorry, i don't have that type of destination.")

def packing_tips():
    print(Fore.CYAN + "TravelBot: where to?")
    location = normalize_input(input(Fore.YELLOW + "You:"))
    print(Fore.CYAN + "TravelBot: how many days")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: packing tips for {days} in {location}:")
    print(Fore.GREEN + "-Pack Vesatille clothes")
    print(Fore.GREEN + "-Bring Charger/Adaptters")
    print(Fore.GREEN + "-check wheather forecast")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\n I can:")
    print(Fore.GREEN + "-Suggest Travel spot(say 'recommendations')")
    print(Fore.GREEN + "-offer packing tips(say 'paching')")
    print(Fore.GREEN + "-Tell a joke(say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'Bye' to end \n ")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "your name?")
    print(Fore.GREEN + f"nice to meet you{name}")
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}:")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! adios!")
            break
        else:
            print(Fore.RED + "TravelBot: could you rephrase?")

if __name__ == "__main__":
    chat()