from nltk.corpus import wordnet as wn
import pytumblr
import random

ls = list(wn.all_synsets(pos=wn.ADJ))
while(True):
    adj = random.choice(random.choice(ls).lemmas())
    if adj.antonyms():
        break
ant = adj.antonyms()
wisdom = f"Everything in reality is either {adj.name()} or {ant[0].name()}."
print(wisdom)

# OAuth is stored in a seperate file because thats not something you post publicly on github
oauth = open("oauth.txt", "r+")
oauth = oauth.read()

# Authenticate via OAuth
# OAuth comes in four parts
client = pytumblr.TumblrRestClient(
    oauth[1:51],
    oauth[55:105],
    oauth[109:159],
    oauth[163:213]
)

client.create_text('dichotomy-of-the-day.tumblr.com', state="queue", body=wisdom)
#client.create_text('dichotomy-of-the-day.tumblr.com', body=wisdom)