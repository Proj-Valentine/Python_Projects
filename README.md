# Python_Projects
## Description

This repository contains a collection of Python projects focused on `automating file processing` and `generating reports`. These scripts are designed to work with various file formats, including CSV, log, and text files, and produce output in CSV, text, and HTML formats.

## Directories

### 1. File processing_and_reporting

This directory houses Python scripts that automate file processing tasks. The scripts can read from CSV, log, and text files, and generate reports in CSV, text, and HTML formats.

### log_analysis:
  - **Description**: This script processes logs from a service called `ticky`, an internal ticketing system. It filters the log data and stores error-related information, including error types and frequencies, and user usage data based on encountered errors and their information. The final processed data is stored in separate CSV files, converted to an html file to report the data in tables on a webserver.
  - To run the program, run the `run_log_process_csv_t_html.py` file which uses the `subprocess module` to run both `log_process.py` and `csv_to_html.py` including their command line arguments which have been `supplied` for now.
  - However, you can run `log_process.p` and `csv_to_html.py` separately: first run `log_process.py` to generate the csv files and run `csv_to_html.py` to generate the corresponding html files. open the html file in any webserver to view reports.

### replace_emailDomain

This directory contains a script that uses regular expressions to find users with an old email domain (abc.edu) in a large list. The script replaces the old domain with a new one (xyz.edu) and saves all domains, including the updated ones, to a new file.

### process_logs

This directory contains a script that uses regular expressions to search and extract specific errors from a program log file. The extracted errors are then saved into a separate file for further analysis, assisting colleagues in troubleshooting program issues.

### unit_test

This directory houses a script for improving the `process_emails.py` script. It includes test cases for identifying and fixing bugs, error handling using try/except, and verifying the accuracy of email lookups, enhancing the script's reliability and functionality.

### rename_file

This directory contains scripts to change a coworker's username from "jane" to "jdoe," aligning with the company's naming policy. It includes both bash and Python scripts to handle renaming operations efficiently, such as using `cat`, `grep`, and `cut` commands for file operations, redirecting I/O streams with `>` and `>>` commands, and replacing substrings using Python. The updated files are then organized accordingly. The directory simulate a directory with `data` sub directory containing data files to be renamed and a `script` directory containing the `bash` and `python` scripts.


### 2. scripts

## reorganize_dir
 The scripts directory contains some scripts to automate directory organization using `recursions` and `non recursive` techniques. These scripts organize files in folders based on their file extensions

- `pass_w_generator` is a script that generates random passwords based on user supplied lenght. it takes an interger value n and generates a password of lenght n.


## Usage

Each directory contains specific Python scripts related to the described tasks. Before running any script, ensure you have Python installed on your system and meet any additional dependencies mentioned within each script.

Feel free to explore and utilize these Python projects for your file processing and reporting needs. Contributions and feedback are welcome, and we hope these scripts will prove helpful in streamlining your tasks!

`file path(names)` should / be modified approriately to match your system

**Note**: Please refer to the individual directories for more detailed instructions on running each script, `parameters` , `*Args` and `return values`.

