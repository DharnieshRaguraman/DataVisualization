import amzn
import fb
import gll
import nflx
import tsla

#import pandas as pd
import matplotlib.pyplot as plt

x = amzn.amzn()
y = fb.fb()
z = gll.gll()
a = nflx.nflx()
b = tsla.tsla()

w = [x,y,z,a,b]
print(w)

n = ["Google","Amazon","Facebook","Netflix","Tesla"]
s = [z,x,y,a,b]
c = ["orange","black","blue","red","grey"]

#dict = {"Company":n,"StockPrice":s}

#df = pd.DataFrame(dict)

#df.to_csv(r'C:\Users\HP\AppData\Local\Programs\Python\Python39\PythonProject\csv\TopStockMarket.csv', index=False)

plt.bar(n,s,width=0.4,align="center",color=c)
plt.xlabel("Company")
plt.ylabel("Stock Price")
plt.title("Top Company Stock Market")
plt.show()
