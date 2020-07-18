import requests
import os

a = "http://"
flag = False

while flag == False:
    str = input("Please write a URL or URLs you want to check. (seperated by comma)\n")
    str = str.replace(" ", "")
    urls = str.split(",")
    for url in urls:
        url = url.lower()
        # print(url)
        if "." not in url:
            print(f"{url} is not a valid URL")
        else:
            if a not in url:
                url = a + url

            try:
                url_result = requests.get(url)
                if url_result.status_code == requests.codes.ok:
                    print(f"{url} is up!")
                else:
                    print(f"{url} is down!")
            except:
                print(f"{url} is down!")

    while True:
        question = input("Do you want to start over? y/n ")
        if question == 'y' or question == 'Y':
            os.system('cls')
            flag = False
            break
        elif question == 'n' or question == 'N':
            print("k, bye!")
            flag = True
            break
        else:
            print("That's not a valid answer.")
            continue


