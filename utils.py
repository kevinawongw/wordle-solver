"""
    Helper funcs and other utils.
"""
import re

def check_string(string):
    """
        Checks for correct formatting.
    """
    pattern = r'^[a-zA-Z_*]{5}$'
    match = re.match(pattern, string)

    return bool(match)

def read_words(filename):
    """
        Reads list of 5 letter words.
    """
    file = open(filename, "r", encoding="utf-8")
    data = file.read()
    full_list = data.split('\n')
    file.close()
    return full_list

def insist_correct(result):
    """
        Asks until correct formatting.
    """
    while not check_string(result):
        print("Invalid format. Please try agian.")
        result = input("Input Result:")
    return result
    