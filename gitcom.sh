#! /bin/bash

# Chek fuel prices
python3 bot_fuel_tr.py

# Waits 30 seconds.
sleep 15

# Add to git repository
git add .
git commit -m "`date +%Y-%m-%d` Fuel Update"
git push origin main
