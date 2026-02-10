# Asset inventory
server_inventory = {
    "web-01": "192.168.1.10",
    "db-01": "192.168.1.20",
    "auth-01": "192.168.1.30"
}

# CHALLENGE: Add a 4th server below this line
server_inventory["backup-01"] = "192.168.1.40"

print(f"total server tracked: {len(server_inventory)}")

# Look up specific IP using the name (Key)

target = "db-01"
print(f"The IP address for {target} is {server_inventory[target]}")