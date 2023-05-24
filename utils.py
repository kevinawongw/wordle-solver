import re 
def check_string(string):
    pattern = r'^[a-zA-Z_*]{5}$'
    match = re.match(pattern, string)
    return bool(match)

       
def read_words(filename):
    f = open(filename, "r")
    data = f.read()
    full_list = data.split('\n')
    f.close()
    return full_list

def insist_correct(result):
    while not check_string(result):
        print("Invalid format. Please try agian.")
        result = input("Input Result:") 
    return result


    