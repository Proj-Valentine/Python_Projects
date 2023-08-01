#!/usr/bin/env python3

# This program process logs for a service (ticky) a ticketing services and stores error data based on error types and frequencies 
# and users of the service and split their usage based on erros encountered and their info
# The final data is stored in to separate csv files and processed for reporting

# How to run the program from command line: ./log_process.py syslog.log error_m.csv user_l.csv

import re
import csv
import operator
import sys

def extract_user_error_info(filelog):
    ''' logfile = sys.argv[1]
    processing log files to track online ticketing service denoted by 'ticky' in the log files'''
    # initialized to store lines containing ERROR
    error_messages = {}
    #initialzed to store users where line contians ERRORS or INFO
    per_users = {}
    with open (filelog, 'r') as f:
        # defining regex patter to match lines containing ERROR and usernames
        error_pattern = r'ticky: ERROR ([\w ]*) \(([\w.]*)\)'
        # defining regex patter to match lines containing INFO and usernames
        info_pattern = r'ticky: INFO ([\w ]*) \[#(\d+)\] \(([\w.]*)\)' 
        for line in f.readlines():
            line.strip() # remove newline characters
            # define variables to store the match objects
            errors = re.search(error_pattern,line)
            info = re.search(info_pattern,line)
            
            # if a match is found for INFO and ERROR
            if info:
                # slice third group \(([\w.]*)\) which is the username
                users=info.group(3).strip()
                # using the setdefault method to set default values if key is not present and increase counter
                per_users.setdefault(users, {'INFO': 0, 'ERROR': 0})
                per_users[users]['INFO'] +=1
                    
            elif errors:
                # slice the first group: error message
                error_type = errors[1].strip()
                users = errors[2].strip()
                # if no key exist default the value to 0 and increment by 1 for every match
                error_messages[error_type] = error_messages.get(error_type, 0) + 1
                per_users.setdefault(users, {'INFO': 0, 'ERROR': 0})
                # adding counts for users and errors
                per_users[users]['ERROR'] += 1 
        return error_messages, per_users

# sort returned dictionaries items
def sort_dic(error_messages,per_users):
    sorted_errors = sorted(error_messages.items(), key = operator.itemgetter(1), reverse=True)
    sorted_errors.insert(0,("Error", "Count"))
    sorted_users = sorted(per_users.items(), key = operator.itemgetter(0))
    sorted_users.insert(0,("Username", "INFO", "ERROR"))
    return sorted_errors , sorted_users

# create errors csv files
def create_error_csv(sorted_errors,error_csv_file):
    with open(error_csv_file, 'w', newline='') as file:
        writer= csv.writer(file)
        writer.writerows(sorted_errors)
        print ('file written successfully to {}'.format(file.name))

# create users stattistic csv files   
def create_users_csv(sorted_users,user_csv_file):
    with open(user_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(sorted_users[0])
        for user in sorted_users[1:]:
            #flatten the user dictionary
            user_info = list(user[1].values())
            writer.writerow([user[0]] + user_info)    
        print ('file written successfully to {}'.format(file.name))
        

def main():
    # Check that command-line arguments are included
    if len(sys.argv) < 4:
        print("ERROR: Missing command-line argument, 'enter logfile' !")
        print("Exiting program...")
        sys.exit(1)
        
    # command line arguments    
    # pass the logfile name    
    logfile = sys.argv[1]
    # pass a name/path for csv file to store error data
    error_csv_file =sys.argv[2]
    # pass a name/path for csv file to store user data
    user_csv_file = sys.argv[3]
    
    if ".log" not in logfile:
        print('Missing ".log" file extension from first command-line argument!')
        print("Exiting program...")
        sys.exit(1)     
    
    if ".csv" not in error_csv_file:
        print('Missing ".csv" file extension from second command-line argument!')
        print("Exiting program...")
        sys.exit(1) 

    if ".csv" not in user_csv_file:
        print('Missing ".csv" file extension from third command-line argument!')
        print("Exiting program...")
        sys.exit(1) 
    # function calls       
    error_messages, per_users = extract_user_error_info(logfile)
    sorted_errors, sorted_users = sort_dic(error_messages,per_users)
    create_error_csv(sorted_errors,error_csv_file)
    create_users_csv(sorted_users,user_csv_file)
    

if __name__ == "__main__":
    main()
    sys.exit(0)
    

     
     
