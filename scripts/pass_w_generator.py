# Generate random passwords from strings characters
import random
import string

# Param: len = length of the password, type integer

def generate_pw(len):
    #generate and concatenate string characters to form a population 
    total = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    total_string = list(total)
    # shuffles the total string
    random.shuffle(total_string)
    # sample len (password length from the populatio of shiffled strings (total string) and join each output with an empty string)
    password = "".join(random.sample(total_string, len))
    return password

generate_pw(10)