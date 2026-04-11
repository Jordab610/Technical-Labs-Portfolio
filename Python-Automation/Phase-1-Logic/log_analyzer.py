import datetime

def analyze_log():
    stats = {}
    
    try:
        with open("network_monitor.log", "r") as f:
            for line in f:
                parts = line.split(" | ")
                name = parts[1].strip()
                ping_status = "UP" if "UP" in parts[2] else "DOWN"
                response_ms = int(parts[4].strip().replace("ms", ""))
                
                # Your job — if name isn't in stats yet, add it
                # Then update the counts and response times
                if name not in stats:
                    stats[name] = {
                        "total": 0,
                        "up": 0,
                        "down": 0,
                        "total_ms": 0
                 }
                    
                stats[name]["total"] += 1
                stats[name]["total_ms"] += response_ms
            
                if "UP" in ping_status:
                    stats[name]["up"] += 1
                else:
                    stats[name]["down"] += 1    
                
            print(f"=== Network Monitor — Summary Report ===\n")
            for name in stats:
                uptime_pct = round((stats[name]["up"] / stats[name]["total"]) * 100)
                avg_ms = round(stats[name]["total_ms"] / stats[name]["total"])
                print(f"{name:<12}      — Checks: {stats[name]["total"] } | UP: {stats[name]["up"]} | DOWN: {stats[name]["down"]} | Avg Response: {avg_ms}| Uptime: {uptime_pct}%\n")
    
            
                
            
            
            
                            
    except FileNotFoundError:
        print("No log file found. Run network_monitor.py first.")
        return

if __name__ == "__main__":
    analyze_log()