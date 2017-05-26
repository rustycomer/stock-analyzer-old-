import quandl

print("What stock would you like to research: ")
user_stock = input()

stock = Share(user_stock)
stock_price = stock.get_price()
stock_volume = stock.get_avg_daily_volume()
stock_cap = stock.get_market_cap
stock_earnings_growth = stock.get_price_earnings_growth_ratio()
stock_info = stock.get_info()
print(str(stock_price))

# get cash on hand
# accounts recievable growth vs sales growth
# get innventory growth vs revenue growth

# stock volume to be greater than 150k if not do not trade


# Calculate gross margins nothing below 20%
# Avoid commodity based businesses
# Avoid second class companies
# Avoid companies that trade less than 100k shares a day
# Avoid companies that have just made recent acquisitions
#
# Look for:
# Companies who have accelerated sales and earnings growth of top and bottom lines of 15%
# Look for insider buying
# Companies that have a solid chart, momentum trends and breaking through lines of resistance with high volume backing the move
# Companies that have products you are familiar with
# Companies with inventory growth relative to revenue growth
# Companies with cash on hand
# Companies with account receivable growth relative to their sales growth
