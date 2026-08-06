import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try: df = pd.read_csv("Lesson6//imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file imdb_top_1000.csv was not found."); raise SystemExit

genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p):
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    d= df
    if genre:
        d = d[d['Genre'].str.contains(genre, case= False, na = False)]
    if rating is not None:
        d = d[d['IMDB_Rating']>= rating]
    if d.empty:
        return "No suitable recommendations found"
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop = True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("overview")
        if pd.isna(ov):
            continue
        pol = TextBlob(ov).sentiment.polarity
        if(not need_nonneg) or pol >=0:
            out.append((r["Series_Title"], pol))
            if len(out) == n:
                break
    return out if out else "No suitable recommendations found"
def show(recs, name):
    print(Fore.YELLOW + f"\n AI- analyzing Movie recommendations for {name}: ")
    for i, (title, polarity) in enumerate(recs, start=1):
        print(f"{Fore.CYAN}{i}. {title} - polarity: {polarity:.2f}, {senti(polarity)}")

def get_genre():
    print(Fore.GREEN + "Available genres: ", end = "")
    for i, g in enumerate(genres, 1): print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x = input(Fore.YELLOW + "Enter the genre number or name: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres):
            return genres[int(x) - 1]
        x = x.title()
        if x in genres:
            return x
        print(Fore.RED + "Invalid input, try again pls. \n")

def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6 - 9.3) or 'skip'").strip()
        if x.lower() == 'skip':
            return None
        try: 
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
        except ValueError:
            print(Fore.RED + "Invalid input, try again pls. \n")

print(Fore.BLUE + "Welcome to your personal movie recommendation assisstant! \n")
name = input(Fore.YELLOW + "What is your name?").strip()
print(f"\n {Fore.GREEN} Great to see you {name}!")
print(Fore.BLUE + "\n Lets find out the perfect movie for you! \n")

genre = get_genre()
mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()
print(Fore.BLUE + "\n Analyzing your mood", end ="", flush = True)
dots()
mp = TextBlob(mood).sentiment.polarity
md = "Positive" if mp>0 else "negative" if mp < 0  else "neutral"
print(f"\n {Fore.GREEN} your mood is {md} (Polarity: {mp:.2f}). \n")

rating = get_rating()
print(f"{Fore.BLUE} \n finding new movies {name} might like", end = "", flush = True);
dots()
recs = recommend(genre = genre, mood = mood, rating = rating, n = 5)
print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)

while True:
    a = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
    if a =="no":
        print(Fore.BLUE + f"\n enjoy your movie picks {name}! \n")
        break
    if a == "yes":
        recs = recommend(genre = genre, mood= mood, rating = rating, n =5)
        print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print(Fore.RED + "Invalid inpot, pls try again. \n")