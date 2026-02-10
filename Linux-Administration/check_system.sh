#!/bin/zsh

echo "--- SYSTEM HEALTH CHECK ---"

echo "1. DISK SPACE USAGE:"
df -h | head -n 5

echo ""
echo "2. TOP 3 MEMORY CONSUMERS:"
ps aux | sort -rnk 4 | head -n 3

echo ""
echo "3. SEARCHING LOGS FOR ERRORS:"
# We store the result of the grep in a temporary variable
ERRORS=$(tail -n 20 /var/log/system.log | grep -i "error")

if [ -z "$ERRORS" ]; then
	echo "✅ No errors found. Your M1 is running smooth!"
else 
	echo "⚠️ Potential issues found:"
	echo "$ERRORS"
fi

echo""
echo "--- CHECK COMPLETE ---"
