import json
from difflib import get_close_matches


with open("data.json") as fileContent:
    content = json.load(fileContent)


def translate(word):
    lowerCasedWord = word.lower()
    if lowerCasedWord in content:
        return content[lowerCasedWord]
    elif len(get_close_matches(word, content.keys())) > 0:
        suggestedWord = get_close_matches(word, content.keys())[0]
        confirmation = input(f"Unfortunately we could not find {word}! Did you mean {suggestedWord}? (Y/N) ")
        if confirmation.lower() == "y":
            return translate(suggestedWord)

    return "The word does not exist! Please double check"

word = input("Enter a word: ")
print(translate(word))
