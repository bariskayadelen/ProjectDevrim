#! /bin/bash

# Chek fuel prices
cd /root/ProjectDevrim/
python3 bot_fuel_tr.py

# Waits 10 seconds.
sleep 10

# Add to git repository
git add .
git commit -m "`date +%Y-%m-%d` Fuel Update"
git push origin main
