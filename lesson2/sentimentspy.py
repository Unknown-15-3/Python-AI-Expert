import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} welcome to sentiment spy! {Style.RESET_ALL}")

user_name = input(f"{Fore.YELLOW} Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "mystery agent"
conversation_hystory = []

print(f"\n {Fore.CYAN} hello agent {user_name}!")

print(f"type a sentence and i will analyze your sentence with textblob and show you sentiment.")
print(f"type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, {Fore.YELLOW}exit{Fore.CYAN} to quit. {Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED} please enter some text or valid command. {Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"{Fore.CYAN} Exciting sentiment, goodbye agent {user_name}! {Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_hystory.clear()
        print(f"{Fore.CYAN} Conversation hystory is cleared. {Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_hystory:
            print(f"{Fore.YELLOW} No conversation hystory found. {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation Hystory: {Style.RESET_ALL}")
            for i, (text, polarity, sentiment_type) in enumerate(conversation_hystory, start =1):
                if sentiment_type == "positive":
                    color= Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😭"

                print(f"{i}.{color}{emoji}{text}" f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "positive"                    
        color= Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "neutral"
        color = Fore.YELLOW
        emoji = "😭"

    conversation_hystory.append((user_input, polarity, sentiment_type))

    print(f"{color}{emoji}{sentiment_type} sentiment detected" f"polarity: {polarity:.2f}")