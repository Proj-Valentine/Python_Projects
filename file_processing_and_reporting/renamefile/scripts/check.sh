
#!/bin/bash
# create a file and search through the data directory and use grep to match patterns
> oldFiles.txt
# scroll through a file that containes names of list of files
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

for i in $files; do
        # test if file exist in the desired directory (test -e "..$i")
        if [ -e "..$i" ]; then
                # append the files to the new file created
                echo "home/Python_Projects/file_processing_and_reporting/renamefile$i" >> oldFiles.txt
        fi
done