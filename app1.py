import json


with open("data.json") as fileContent:
    content = json.load(fileContent)

def translate(word):
    return content[word]

word = input("Enter a word: ")
print(translate(word))
# print(content["rain"])