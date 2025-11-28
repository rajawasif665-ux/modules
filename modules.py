import numpy as np
import pandas as pd
import json
# CREATE CLASSS
class Stock:
    def __init__(self,name,shares,buy_price,current_price):
        self.name=name
        self.shares=shares
        self.buy_price=buy_price
        self.current_price=current_price
    def value(self):
        return self.shares*self.current_price
    def profit (self):
        return(self.current_price - self.buy_price)*self.shares
# CREATE SECOND CLASS
class Portfolio:
    def __init__(self):
        self.stock=[]
    def add_stock(self,stock):
        self.stock.append(stock)
        print(f"{stock.name} added!")
    def get_table(self):
         data = {
            "Name": [s.name for s in self.stock],
            "Shares": [s.shares for s in self.stock],
            "Buy Price": [s.buy_price for s in self.stock],
            "Current Price": [s.current_price for s in self.stock],
            "Value": [s.value() for s in self.stock],
            "Profit": [s.profit() for s in self.stock],
        }
         return pd.DataFrame(data)
    def total_value(self):
        return np.sum([s.value()for s in self.stock])
    def total_profit(self):
        return np.sum([s.profit()for s in self.stock])
    def save(self,filename="portfolio.json"):
        data = [
            {
                "name": s.name,
                "shares": s.shares,
                "buy_price": s.buy_price,
                "current_price": s.current_price
            }
            for s in self.stock
        ]
        with open(filename,"w")as f:
            json.dump(data,f,indent=4)
        print("Portfolio saved!")
    def load(self,filename="portfolio.json"):
        try:
            with open(filename,"r")as f:
                data=json.load(f)
                self.stock=[Stock(**item)for item in data]
            print("Portfolio loaded !")
        except:
            print("Error file not found!")
# ewifhjdsf         
if __name__ == "__main__":
    portfolio = Portfolio()
# add stock
    portfolio.add_stock(Stock("Apple", 10, 150, 170))
    portfolio.add_stock(Stock("Tesla", 5, 200, 250))
    portfolio.add_stock(Stock("Microsoft", 8, 100, 140))

    print("\n=== Portfolio Table ===")
    print(portfolio.get_table())

    print("\nTotal Portfolio Value:", portfolio.total_value())
    print("Total Profit:", portfolio.total_profit())
# save portfolio
portfolio.save()
#load
new_portfolio = Portfolio()
new_portfolio.load()

print("\n=== Loaded Portfolio ===")
print(new_portfolio.get_table())


