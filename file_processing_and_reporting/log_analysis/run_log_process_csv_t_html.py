#!/usr/bin/env python3

    
import subprocess

if __name__ == "__main__":
    # run the log_process scripts
    subprocess.run(["python", "log_process.py", "syslog.log", "errorstry.csv", "user_list_try.csv"])
    
    # run the csv_to_html.py to convert csv files generated from the log_process script to html files (tables)
    subprocess.run(["python", "csv_to_html.py","errorstry.csv", "errors_count.html"])
    subprocess.run(["python", "csv_to_html.py","user_list_try.csv", "user_activity.html"])

