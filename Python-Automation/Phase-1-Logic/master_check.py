# 1. Our Inventory (The 'Source of Truth')
server_inventory = {
    "web-01": "192.168.1.10",
    "db-01": "192.168.1.20",
    "auth-01": "192.168.1.30",
    "backup-01": "192.168.1.40"
}

# 2. Manual status override (simulating a real network scan)
# True = Up, False = Down

status_check = {
    "web-01": True,
    "db-01": False,
    "auth-01": True,
    "backup-01": False,
    
}

print(f"--- ADVANCED SRE HEALTH CHECK ---")

for server, ip in server_inventory.items():
    # Look up the status in our status_check dictionary
    is_up = status_check[server]
    
    if is_up:
        print(f"[OK] {server} {ip} is responding.")
    else:
        print(f"[ERROR] {server} {ip} is UNREACHABLE!")
        
print("--- END OF REPORT ---")