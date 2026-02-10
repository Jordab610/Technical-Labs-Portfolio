#!/bin/bash

# Setting the directory as our home for safety

TARGET_DIR="."
LOG_FILE="cleanup_history.log"

# 1 Log the date of the operation
echo "--- Cleanup Run: $(date) ---" >> "$LOG_FILE"

# 2 This finds the old files and writes their names into our log file for accountability

find "$TARGET_DIR" \( -name "*.tmp" -o -name "*_temp" \) -mtime +1 >> "$LOG_FILE"

# 3 The "Destroy" step 

find "$TARGET_DIR" \( -name "*.tmp" -o -name "*_temp" \) -mtime +1 -exec rm {} +

echo "Cleanup complete. Check $LOG_FILE for the record of destroyed files."


