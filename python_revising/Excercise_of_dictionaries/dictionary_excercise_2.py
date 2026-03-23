# You are given following list of stocks and their prices in last 3 days,
#
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# a) print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# b) add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc.) then it will append the price to the list. Otherwise, it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

stock_prices={
    "info": [600,630,620],
    "ril": [1430,1490,1567],
    "mtl": [234,180,160]
}
def print_stocks(stocks):
    for tickers,p in stock_prices.items():
        avg=float(sum(stock_prices[tickers])/len(stock_prices[tickers]))
        print(tickers,"==>",p,"avg:",avg)

def add_stocks(stocks):
    ticker=input("Enter the ticker: ")
    price=float(input("Enter the price: "))
    if ticker in stocks:
        stocks[ticker].append(price)
        print_stocks(stocks)
    else:
        stocks[ticker]=[price]
        print_stocks(stocks)

def choices(choic):
    if choic=="print":
        print_stocks(stock_prices)
    elif choic=="add":
        add_stocks(stock_prices)
    else:
        print("Invalid choice")


if __name__ == '__main__':
    x="1"
    while x != "ok":
        choice = input("Enter the operation you wanna perform ,print,add on a given dataset ")
        choice = choice.lower()
        choices(choice)
        if choice == "ok":
            x="ok"
            print("program terminated")

