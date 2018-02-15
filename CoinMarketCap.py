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

    for i in [coin["percent_change_1h"],coin["percent_change_24h"],coin["percent_change_7d"]]:
        if i!=None:
            print("Change (1h) : "+i+" %")
        else:
            print("Change (1h) : N/A")
    print("=======================")

    #return coin
