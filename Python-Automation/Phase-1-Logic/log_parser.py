# SRE Skill: File I/O and Data Aggregation
# Can error if the direectory is wrong or the file doesn't exist, so I added a try:except block to handle that gracefully.
# May also fail depending on the format of the log file, will add some basic error handling for that as well in the future.
error_counts = {}

print("--- SCANNING SYSTEM LOGS ---")

# The 'with' keyword ensures the file closes automatically, even if the script crashes 
# Added a try:execpt block to handle potential file not found errors gracefully.
try:
    with open("server_logs.txt", "r") as file:


        for line in file:
            # Step 1: Clean and Normalize
            clean_line = line.strip()
            
            # Step 2: Logic Branching (Only care about ERRORS)
            if "ERROR" in clean_line:
                print(f"⚠️  Detected: {clean_line}")
                
                # Step 3: Count the occurrences using a dictionary
                # We split the line to get the server name (e.g., 'db-01')
                parts = clean_line.split(":")
                error_message = parts[1].strip()
                
                # This logic adds 1 to the count or creates the key if it's new
                error_counts[error_message] = error_counts.get(error_message, 0) + 1
    print("\n--- ERROR SUMMARY REPORT ---")
    for msg, count in error_counts.items():
        print(f"{msg}: {count} occurrences")
# added a catch and action for file not found errors, which is a common issue when dealing with file I/O in automation scripts. This way, if the log file is missing, the script will inform the user instead of crashing.  
except FileNotFoundError as e:
    print(f"❌ ERROR: Log file not found. Details: {e}")
    
