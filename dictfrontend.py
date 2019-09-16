import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tkinter.Tk()
# Code to add widgets will go here...
import json
from difflib import get_close_matches
data = json.load(open("data.json"))
print("******************")
print("English Dictionary")
print("******************\n")
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

def function():
    word = input("Enter the word: ")
    output = meaning(word)

    if type(output) == list:
        count = 1
        for item in output:
            print(str(count)+". " + item + "\n")
            count = count + 1

    else:
        print(output)
function()
nextWord = input("Do you wish to search another word ? [y/n]: ")

while nextWord.lower() == 'y':
    function()
    nextWord = input("Do you wish to search another word ? [y/n]: ")
else:
    print("Good Bye!")
    quit()

top.mainloop()
