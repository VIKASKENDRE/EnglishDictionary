import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean %s instead? Enter 'y'for yes and 'n' for no. [y/n]: " % get_close_matches(word, data.keys())[0])

        if answer.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif answer.lower() == 'n':
            word = input("Please enter the word again: ")
            return (meaning(word))
        else:
            print("We did not understand the input.\n")
            word = input("Please enter the word again: ")
            return (meaning(word))

    else:
        return "This word does not exist in the dictionary, please double check it"


word = input("Enter the word: ")
output = meaning(word)

if type(output) == list:
    count = 1
    for item in output:
        print(str(count)+". " + item + "\n")
        count = count + 1

else:
    print(output)
