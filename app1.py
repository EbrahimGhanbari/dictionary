import json


with open("data.json") as fileContent:
    content = json.load(fileContent)

def translate(word):
    lowerCasedWord = word.lower()
    if lowerCasedWord in content:
        return content[lowerCasedWord]
    else:
        return "The word does not exist! Please double check"

word = input("Enter a word: ")
print(translate(word))
