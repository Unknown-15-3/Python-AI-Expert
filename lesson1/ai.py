import webbrowser

print("Hello! I am an AI bot! what is your name?")
name = input().strip()
print(f"nice to meet you, {name}!")
print("which website would you likes to visit?")

site_name = input().strip().lower()

url = f"https://www.{site_name}.com"
print(f"opening {url} now.....")
webbrowser.open(url)
print(f"it was nice chatting with you, {name}. have a great day!")