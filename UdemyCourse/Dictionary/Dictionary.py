import json
from difflib import get_close_matches

#Loads the JSON data from data.json
data = json.load(open("UdemyCourse\Dictionary\data.json"))

#Searches JSON file for the word and returns the definition
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    
    #Checks title-case spelling for words like 'Texas' or 'Paris'
    elif w.title() in data:
        return data[w.title()]
    
    #Checks uppercase spelling for words like 'USA' or 'NATO'
    elif w.upper() in data:
        return data[w.upper()]

    #If the user enters an invalid word, but it is close to another word, 
    #the program will ask if they meant the near-match. 
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist, please double check it."
        else:
            return "We did not understand your entry."

    #If the word is not close to any other word in the dict, it will return an error message
    else:
        return "The word doesn't exist, please double check it."


#Takes user input
word = input("Enter word: ")

#Runs the translate() method, stores the value in a variable
output = (translate(word))

#Iterates through output, prints contents line-by-line if it is a list
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

