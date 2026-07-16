print("Hello! I am an AI bot! what is your name?")
name = input()
print("Nice to meet you, " + name + "!")
print("How are you feeling today? (good/bad):")

mood = input().lower()

if mood == "good":
    print("That great to hear!")
elif mood == "bad":
    print("I am sorry to hear that. Hope your day gets better eventually!")
else:
    print("I am not sure what you mean by that, but i hope you have a good day!")

print("It was nice chatting with you!" + name + ". Have a great day!")