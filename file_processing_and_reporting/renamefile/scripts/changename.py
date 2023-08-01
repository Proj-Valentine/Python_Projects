#!/usr/bin/env python3

# Renaming files

import sys
import subprocess
import os

# pass the file created from the check.sh script contains old file names to be renamed-full path) as a command line argument to this python scripts
file=sys.argv[1]
with open(file,'r') as f:
        for line in f.readlines():
                old=line.strip()
                new=line.strip().replace('jane','jdoe')
                if os.path.exists(old):
                        subprocess.run(["mv",old,new])
                else:
                        print("error: file {} does not exist".format(old))