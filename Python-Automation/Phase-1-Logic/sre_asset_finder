# SRE Database simulation: A dictionary of critical infrastructure
infrastructure = {
    "prod-db-01": "Primary Database - MySQL",
    "web-cache-01": "Redis Cache Layer",
    "auth-service": "Identity Management"
}

print("=== SRE ASSET FINDER (PROD) ===")

# Adding .strip & .lower to catch for user input variance
asset_id = input("Enter Asset ID:").strip().lower()

try:
    # Attempt to locate the asset
    asset_info = infrastructure[asset_id]
    print(f"✅ STATUS: {asset_id} is {asset_info}")
except KeyError:
    # SRE philosophy: Log the error, don't let the tool crash
    print(f"❌ ALERT: Asset ID '{asset_id}' not found in production inventory.")
    print("Action Required: Check inventory database integrity.")

print("==============================")



