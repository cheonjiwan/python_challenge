import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("cls")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

def transferwise_crawl(transferurl):
    url = transferurl
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    
    div1 = soup.find("span",{"class":"text-success"}).string
    

    rate = float(div1)
   # print(converted)
    return rate


def crawl():
    url = "https://www.iban.com/currency-codes"
    
    iban_result = requests.get(url)
    iban_soup = BeautifulSoup(iban_result.text, "html.parser")

    table = iban_soup.find("table", {"class": "table table-bordered downloads tablesorter"})

    tbody = table.find("tbody")
    tds = tbody.find_all("td")

    information = {}
    length = len(tds)
    key = 0
    country = []
    for i in range(0, length, 4):
        if tds[i + 1].string == "No universal currency":
            continue
        else:
            country.append(tds[i].string.capitalize())
            country.append(tds[i + 1].string.capitalize())
            country.append(tds[i + 2].string)
            country.append(tds[i + 3].string)
            information[key] = country
            key = key + 1
            country = []

    return information

def caculator(money, value):
    return money * value
    
def main():
    country_dic = crawl()
    print("Welcome to CurrencyConvert PRO 2000: \n")

    for i in range(len(country_dic)):
        print('# {} {}'.format(i, country_dic[i][0]))

    print("Where are you from? Choose a country by number.\n")
    from_num = int(input("#: "))
    print(f"{country_dic[from_num][0]}\n")

    print("Now choose another country.\n")
    another_country_num = int(input("#: "))
    print(f"{country_dic[another_country_num][0]}\n")

    while (True):
        try:
            print(f"How many {country_dic[from_num][2]} do you want to convert to {country_dic[another_country_num][2]}")
            money = int(input())
            break
        except:
            print("That wasn't a number.\n")
            continue


    transfer_url = "https://transferwise.com/gb/currency-converter/"+ str(country_dic[from_num][2].lower())+"-to-"+str(country_dic[another_country_num][2].lower())+"-rate"+"?amount="+str(money)+"#rate-alerts"
    value = transferwise_crawl(transfer_url)
    result = caculator(money, value)

    print(format_currency(money,country_dic[from_num][2],locale="ko_KR")+" is ",end='')
    print(format_currency(result,country_dic[another_country_num][2],locale="ko_KR"))

main()