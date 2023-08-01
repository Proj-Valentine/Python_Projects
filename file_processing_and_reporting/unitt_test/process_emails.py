#!/usr/bin/env python3

#Description: Find and print a users email given their full name as command line arguments 
    # example ./process_email.py valentine ampah
    
# Param filename: csv file path
# param argv :  command arguments

import csv
import sys

# Create functions

def populate_dictionary(filename):
    """
    Populate a dictionary with name/email pairs for easy lookup.
    Args:
        filename (file/path.csv): csv file.
    Returns:
        dictionary: a dictionary with name/email pairs
    """
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for row in lines:
            name = str(row[0].lower())
            email_dict[name] = row[1]
    return email_dict

def find_email(argv):
    """ Return an email address based on the username given.
    Args:
        argv (list): command arguments e.g [firstname, lastname]
    Returns:
        string: email address
    """
    # Create the username based on the command line input.
    try:
        fullname = str(argv[1] + " " + argv[2])
        # Preprocess the data
        email_dict = populate_dictionary('user_emails.csv')
            # If email exists, print it else retunr a default hard coded value
        if email_dict.get(fullname.lower()):
            return email_dict.get(fullname.lower())
        else:
            return "No email address found"
    except IndexError:
        return "Missing parameters"

def main():
    print(find_email(sys.argv))
    
if __name__ == "__main__":
    main()
