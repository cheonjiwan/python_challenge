import os
import requests
from bs4 import BeautifulSoup

#os.system("clear")


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


def main():
    country_dic = crawl()
    print("Hello! Please choose select a country by number: ")

    for i in range(len(country_dic)):
        print('# {} {}'.format(i, country_dic[i][0]))

    while (True):
        try:
            country_num = int(input("#: "))
            if country_num >= len(country_dic):
                print("Choose a number from the list.")
                continue
            else:
                break
        except:
            print("That wasn't a number.")
            continue

    print(f"You choose {country_dic[country_num][0]}")
    print(f"The currency code is {country_dic[country_num][2]}")


main()
