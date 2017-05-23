from yahoo_finance import Share

user_stock = input("What stock would you like to research: ")

stock = Share(user_stock)
stock_price = stock.get_price()
stock_volume = stock.get_avg_daily_volume()
# get earnings growth
# get marketcap
# get cash on hand
# accounts recievable growth vs sales growth
# get innventory growth vs revenue growth

# stock volume to be greater than 150k if not do not trade


'''Calculate gross margins nothing below 20%
Avoid commodity based businesses
Avoid second class companies
Avoid companies that trade less than 100k shares a day
Avoid companies that have just made recent acquisitions

Look for:
Companies who have accelerated sales and earnings growth of top and bottom lines of 15%
Look for insider buying
Companies that have a solid chart, momentum trends and breaking through lines of resistance with high volume backing the move
Companies that have products you are familiar with
Companies with inventory growth relative to revenue growth
Companies with cash on hand
Companies with account receivable growth relative to their sales growth'''
