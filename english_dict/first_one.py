import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)):
        ur = input('Did you mean %s instead? Enter Y if yes, or N if No: ' % get_close_matches(w, data.keys())[0])
        if ur.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return 'Well, then I suppose this word has some mistakes. Please, try again.'
    else:
        return 'I suppose this word has some mistakes. Please, try again.'

word = input('Enter your word, please:')

print(translate(word))