# Our list of infrastructure
all_servers = ["web-01", "db-01", "api-01", "mail-01"]
down_servers = [] # This is our empty bucket

# Let's pretend only these two are broken 
broken_status = ["db-01", "mail-01"]

# Loop through all our servers and check their status
for server in all_servers:
    if server in broken_status:
        down_servers.append(server)
        print(f"Checking {server}... [FAILED]")
    else:
        print(f"Checking {server}... [OK]")

# Final Report for the SRE Team
print("\n--- INCIDENT REPORT ---")
print(f"Server requiring immediate attention: {", " .join(down_servers)}")