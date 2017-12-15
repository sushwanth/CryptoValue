from lxml import html
import requests
import datetime
import time
from termcolor import colored


list_ = ['tron',
         'ripple',
         'bitcoin',
         'litecoin',
         'ethereum',
         'cardano']


print("|".join([str(datetime.datetime.now()).ljust(35) ]+[_.center(15) for _ in list_]))
dict_ = {}
while(1):
    values_ = []
    dict_['change'] = False
    for currency in list_:
        page = requests.get('https://coinmarketcap.com/currencies/'+currency+'/')
        tree = html.fromstring(page.content)
        value = (tree.xpath('//*[@id="quote_price"]/span[1]/text()'))[0]
        if currency in dict_.keys():
            if dict_[currency] > value:
                values_.append((colored(value.center(15), 'red')))
                dict_['change'] = True
            elif dict_[currency] < value:
                values_.append((colored(value.center(15),'green')))
                dict_['change'] = True
            else:
                values_.append(value)
        dict_[currency] = value

    if dict_['change'] :
        print("|".join([str(datetime.datetime.now()).ljust(35)]+[_.center(15) for _ in values_]))
    time.sleep(5)