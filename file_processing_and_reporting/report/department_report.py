#!/usr/bin/env python3

# Process Employees files and report on the deparment with most employees


import csv
import os

csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

def read_employees(csv_file):
        '''
        Reads a csv fie and returns a list of dictionaries for each record
        Args:
                csv_file (valid csv file path)
        Returns:
                List of dictionaries
        '''
        employees=[]
        with open(csv_file,'r') as file:
                employee_file = csv.DictReader(file,dialect='empDialect')
                for row in employee_file:
                        employees.append(row)
        return employees


def process_data(emp_list):
        ''' 
        Args:
               emp_list (List): A list contaiing dictionaries
        Returns:
                Dictionary: containing distinct deparments (key) and counts (values)'''
        emp_dic={}
        emp_dep=[]
        # append departments into a list
        for emp in emp_list:
                emp_dep.append(emp['Department'])
        # count each instance of department and map it to the deparment name as key:value pairs
        for dep in set(emp_dep):
                emp_dic[dep]= emp_dep.count(dep)
        return emp_dic

def write_report(dep_info,newfile):
        ''' Write a report of cotaining the deparments and counts
        Args:
                def_info (dic)
                newfile (any filename/path)
        Return:
                file: writes the def_info into a new text file'''
        with open(newfile,'w+') as file:
                for dep,num in dict(sorted(dep_info.items())).items():
                        file.write(str(dep)+':' + str(num)+'\n')
                print('file written successfylly to {}'.format (file.name))

def main():
    try:
            file_path = 'employees.csv'
            if not os.path.isfile(file_path):
                    print('Invalid file: Exiting Program ...')
                    exit()
            else:
                    employee_list=read_employees(file_path)
    except FileNotFoundError:
            print('Enter a valid file name:')
    emp_dic= process_data(employee_list)
    write_report(emp_dic,'test_report.txt')
    
if __name__== '__main__':
    main()
    

