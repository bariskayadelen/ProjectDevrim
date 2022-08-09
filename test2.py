import get_currency_tr as cur

# Get all data
print(cur.price('USD'))

# Get bank currency code
print(cur.price('USD')[0])

# Get bank buy rate
print(cur.price('USD')[1])

# Get bank sell rate
print(cur.price('USD')[2])

# Example: 1600 USD to TRY
x = float(cur.price('USD')[2])
print(round((x * 1600), 2))