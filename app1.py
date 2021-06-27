import json
from difflib import get_close_matches

# Load the english dictionary definitions in JSON format
data = json.load(open('data.json'))


def translate(word):
    """
    Function to take the user input word and search the dictionary keys to return the associated value.
    Uses difflib to perform fuzzy match on similar words if the user spells a word incorrectly.
    """

    # Converts the input word to lower case to match with the dictionary keys.
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        """
        This extra clause covers place names like Delhi or Paris etc. that shouldn't be converted by lower() method
        """
        return data[word.title()]
    elif word.upper() in data:
        """
        This extra clause covers acronyms such as NATO and USA etc. that shouldn't be converted by lower() method.
        """
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        """
        get_close_matches creates a list object. Index 0 is the closest match of the returned words.
        Asks for confirmation from user if the similar word is correct and returns the definition if yes.
        """
        response =  input("Did you mean %s instead? Enter Y for Yes or N for No: " % get_close_matches(word, data.keys())[0])
        if response.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif response.lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, we didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."

# User input request - enter a word to look up
user_input = input("Enter word: ")

# Fuction call with the user input as an argument
output = translate(user_input)

"""
Present the output list items as strings using the indexes as item numbers.
Else return the error message strings instead.
"""
if type(output) == list:
    for idx, item in enumerate(output):
        print("The following definition(s) were found:")
        print(f'{idx + 1}: {item}')
else:
    print(output)
