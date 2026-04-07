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
    result = subprocess.run(
        ["ping", "-c", "2", "-W", "2", host],
        capture_output=True,
        text=True,  
    )
    if "0% packet loss" in result.stdout:
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
def run_checks():
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"=== Network Monitor - {timestamp} ===")
    for server in ENDPOINTS:
        print(f"\n{server["name"]} ({server["host"]})")
        ping_result = ping_host(server["host"])
        
        ping_status = "UP" if ping_result else "DOWN"
        print(f"  Ping   (Layer 3): {ping_status}")
        
        status_code, response_ms = check_http(server["url"])
        if status_code:
            print(f"   HTTPS   (Layer 7): {status_code} - {response_ms}ms")
        else:
            print(f"  HTTPS   (Layer 7): UNREACHABLE")
    
if __name__ == "__main__":
    run_checks()