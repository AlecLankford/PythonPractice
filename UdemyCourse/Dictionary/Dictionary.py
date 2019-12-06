import json

#Loads the JSON function
data = json.load(open("UdemyCourse\Dictionary\data.json"))

#Searches JSON file for the word and returns the definition
#If the word does not exist it will return an error message
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist, please double check it."
    

#Takes user input
word = input("Enter word: ")

#Returns definition of user input
print(translate(word))

