
# stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# pe ratio = price / earnings per-share
# price to book ratio = price / book value

with open("stocks.csv","r") as f ,open("output.csv","w") as output:
    output.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
        credit=line.split(",")
        stock=credit[0]
        price=float(credit[1])
        earning=float(credit[2])
        book_value=float(credit[3])
        pe_ratio=float(price/earning)
        ptbr=float(price/book_value)
        output.write(f"{stock},{pe_ratio},{ptbr}\n")


