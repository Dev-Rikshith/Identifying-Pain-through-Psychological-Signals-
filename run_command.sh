#!/bin/bash

directory="/path/to/your/project"

log_file="script_log.txt"

commands=(
   "/Users/ricky/mambaforge/bin/python Project2.py dia Project2Data"
   "/Users/ricky/mambaforge/bin/python Project2.py sys Project2Data"
   "/Users/ricky/mambaforge/bin/python Project2.py eda Project2Data"
   "/Users/ricky/mambaforge/bin/python Project2.py res Project2Data"
   "/Users/ricky/mambaforge/bin/python Project2.py all Project2Data"
)

for file in "$directory"/*.py; do
    echo "Processing file: $file" >> "$log_file"
    
    for cmd in "${commands[@]}"; do
        echo "Running command: $cmd" >> "$log_file"
        echo "" >> "$log_file" 
        eval "$cmd" >> "$log_file" 2>&1  
        echo "" >> "$log_file"  
    done

    echo "" >> "$log_file"  
done

echo "All files processed. Log saved to $log_file"
