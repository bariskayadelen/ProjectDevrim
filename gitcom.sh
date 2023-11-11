#! /bin/bash

# Check fuel prices
# cd /root/ProjectDevrim/
cd /Users/baris/Library/Mobile\ Documents/com~apple~CloudDocs/GitHub/ProjectDevrim/
python3 bot_fuel_tr.py

# Waits 7 seconds.
sleep 7

# Add to git repository
git add .
git commit -m "`date +%Y-%m-%d` Fuel Update"
git push origin main
