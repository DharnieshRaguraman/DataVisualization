def gll():
    import requests as rq
    from bs4 import BeautifulSoup as bs
    url = "https://www.google.com/finance/quote/GOOGL:NASDAQ"
    r = rq.get(url)
    soup = bs(r.content,"html.parser")
    price = soup.find("div",{"class":"YMlKec fxKbKc"})

    return price.text
