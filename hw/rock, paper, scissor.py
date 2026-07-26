from colorama import init, Fore, Style
import random

init(autoreset=True)

OPTIONS = ["rock", "paper", "scissor"]

def bot_reply(user_choice, bot_choice, result):
    # simple chatbot-like replies
    if result == "win":
        replies = [
            "Nice move! I didn't see that coming.",
            "You're good at this!",
            "Well played. I'll get you next time."
        ]
    elif result == "lose":
        replies = [
            "Ha! I win this round.",
            "Lucky shot. Try again!",
            "I had that one planned."
        ]
    else:
        replies = [
            "It's a tie. So close!",
            "We think alike.",
            "Draw. Rematch?"
        ]
    prefix = f"You: {user_choice} | Bot: {bot_choice} -> "
    return prefix + random.choice(replies)

def decide(user, bot):
    if user == bot:
        return "draw"
    wins = {"rock": "scissor", "scissor": "paper", "paper": "rock"}
    if wins[user] == bot:
        return "win"
    return "lose"

def color_text(text, result):
    if result == "win":
        return Fore.GREEN + text + Style.RESET_ALL
    if result == "lose":
        return Fore.RED + text + Style.RESET_ALL
    return Fore.YELLOW + text + Style.RESET_ALL

def main():
    print(Fore.CYAN + "Welcome to Rock, Paper, Scissor! :D.")
    print("Type 'quit' to exit. Type 'help' for options.")
    score_user = 0
    score_bot = 0

    while True:
        user = input(Fore.WHITE + "Your move (rock/paper/scissor): ").strip().lower()
        if not user:
            continue
        if user == "quit":
            print(Fore.CYAN + "Goodbye!")
            break
        if user == "help":
            print("Options:", ", ".join(OPTIONS))
            continue
        if user not in OPTIONS:
            print(Fore.MAGENTA + "Invalid choice. Try rock, paper, or scissor.")
            continue

        print(Fore.BLUE + "Bot is thinking...")

        bot = random.choice(OPTIONS)
        result = decide(user, bot)

        if result == "win":
            score_user += 1
        elif result == "lose":
            score_bot += 1

        reply = bot_reply(user, bot, result)
        print(color_text(reply, result))
        print(Fore.CYAN + f"Score => You: {score_user} | Bot: {score_bot}")
        print()

if __name__ == "__main__":
    main()
