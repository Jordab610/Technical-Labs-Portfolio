import subprocess
import requests
import datetime

ENDPOINTS = [
    
    {"name": "Google", "host": "google.com", "url": "https://google.com"},
    {"name": "GitHub", "host": "github.com", "url": "https://github.com"},
    {"name": "YouTube", "host": "youtube.com", "url": "https://youtube.com"},
    {"name": "MangaDex", "host": "mangadex.org", "url": "https://mangadex.org"}
]

def ping_host(host):
    import platform
    if platform == "Windows":
        command = ["ping", "-n", "2","-w","2000", host]
        success_text = "Lost = 0"
    else:
        command = ["ping", "-c", "2", "-W", "2", host]
        success_text = "0% packet loss"
        
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,  
    )
    if success_text in result.stdout:
        return True
    else:
        return False
    
def check_http(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        response_ms = round(response.elapsed.total_seconds() * 1000)
        return status_code, response_ms
    except requests.exceptions.ConnectionError:
        return None, None
    except requests.exceptions.Timeout:
        return None, None
    except Exception as e:
        return None, None
    
def log_result(name, ping_status, status_code, response_ms):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
    entry = f"{timestamp} | {name} | PING : {ping_status} | HTTPS : {status_code} | {response_ms}ms\n"
    with open("network_monitor.log", "a") as f:
        f.write(entry)

def get_previous_status():
    previous = {}
    try:
        with open("network_monitor.log", "r") as f:
            for line in f:
                parts = line.split(" | ")
                name = parts[1].strip()
                if "UP" in parts[2]:
                   previous[name] = "UP"
                else:   
                   previous[name] = "DOWN"
    except FileNotFoundError: 
        pass
    return previous
            


def run_checks():
    
    previous = get_previous_status()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"=== Network Monitor - {timestamp} ===")
    
    for server in ENDPOINTS:
        
        print(f"\n{server["name"]} ({server["host"]})")
        ping_result = ping_host(server["host"])    
        ping_status = "UP" if ping_result else "DOWN"
        
        previous_status = previous.get(server["name"])
        if previous_status is None:
            # First time seeing this endpoint
            print(f"  Status: First check - none previous data")
        elif previous_status != ping_status:
            # Something CHANGED - prints alert
            print(f"  *** ALERT: {server["name"]} changed from {previous_status} to {ping_status} ***")
        else:
            # Same as before, nothing add
            print(f" Status: No change")
            
        print(f"  Ping   (Layer 3): {ping_status}")
        
        status_code, response_ms = check_http(server["url"])
        if status_code:
            print(f"   HTTPS   (Layer 7): {status_code} - {response_ms}ms")
        else:
            print(f"  HTTPS   (Layer 7): UNREACHABLE") 
        log_result(server["name"], ping_status, status_code, response_ms)
        
       
            
        
    
if __name__ == "__main__":
    run_checks()