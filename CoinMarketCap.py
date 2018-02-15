# -*- coding: utf-8 -*-

from coinmarketcap import Market
coinmarketcap = Market()

def get(name):
    coin = coinmarketcap.ticker(currency=name,convert="EUR")[0]

    print("\n=======================")
    print("Name : "+coin["name"])
    print("Symbol : "+coin["symbol"])
    print("Rank : "+coin["rank"])
    print("Price : "+coin["price_btc"]+" Ƀ")
    print("Price : "+coin["price_usd"]+" $")
    print("Price : "+coin["price_eur"]+" €")

    for i in ["1h","24h","7d"]:

        v = [coin["percent_change_1h"],coin["percent_change_24h"],coin["percent_change_7d"]]

        if i=="1h":
            k=v[0]
        if i=="24h":
            k=v[1]
        if i=="4d":
            k=v[2]

        if k!=None:
            print("Change ("+i+") : "+k+" %")
        else:
            print("Change ("+i+") : N/A")
    print("=======================")

    #return coin
