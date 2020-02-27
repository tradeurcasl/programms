import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)):
        ur = input('Did you mean %s instead? Enter Y if yes, or N if No: ' % get_close_matches(w, data.keys())[0])
        if ur.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif ur.upper() == 'N':
            return 'Well, then I suppose this word has some mistakes. Please, try again.'
        else:
            return 'I do not understand you. Please, use Y,N-language in query'
    else:
        return 'I suppose this word has some mistakes. Please, try again.'

word = input("Enter your word, please: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)