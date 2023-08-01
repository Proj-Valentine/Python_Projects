#!/usr/bin/env python3

# Program description: process log files to identify lines with specific errors and write them to a new file

# STEPS
    # change file mode:
        # - sudo chmod +x find_error.py
    # run file from command line
        # - ./find_error.py ~/directory/logfilename
    # sample error input
        # - CRON ERROR Failed to start

import sys
import os
import re

def error_search(log_file):
    ''' this returns lines in log files that contains error patterns we are looking for'''
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                # returning lines in logfiles that contains the error pattern
                returned_errors.append(log)
    return returned_errors
  
def file_output(returned_errors):
    ''' This function writes the found error lines into a new file. 
    the expanduser function returns the home directory of your system instance'''    
    with open(os.path.expanduser('~') + '/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
    print('File successfully written to {}'.format(file.name))
        
if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)