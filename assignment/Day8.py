import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("cls")
alba_url = "http://www.alba.co.kr"

# 슈퍼브랜드 항목 가져오기
def extract_brand(html):
    company_link = html.find("a")["href"]
    title = html.find("span",{"class":"company"}).string
    return [title,company_link]

def get_super_brand():
    super_brand_list = []
    result = requests.get(alba_url)
    soup = BeautifulSoup(result.text,"html.parser")
    superbrand = soup.find("div",{"id":"MainSuperBrand"})
    goodsboxs = superbrand.find("ul",{"class":"goodsBox"})
    goodsboxs_li = goodsboxs.find_all("li")

    for goodsbox in goodsboxs_li:
        brand_list = extract_brand(goodsbox)
        super_brand_list.append(brand_list)
    
    return super_brand_list
            

# def get_last_pages(url):
#     print(url)
#     result = requests.get(url)
#     soup = BeautifulSoup(result.text, "html.parser")
#     normarInfo = soup.find("div", {"class":"paging"})
#     print(normarInfo)
#     #pages = normarInfo.find("div",{"class":"paging"})

#     #print(pages)
#     #pages = soup.find("div", {"class":"paging"}).find("span",{"class":"page"})

#     #print(pages)
    
#     #return pages
#     return


def get_jobs(url):
  job_list = []
  #brand_list = brandlist
  if url == "http://www.alba.co.kr/job/brand/elandfashion/job/brand":
    return
  else:
    print(url)
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    table = soup.find("div",{"id":"NormalInfo"}).find("table")
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")
    
    for i in range(0,len(trs),2):
        html = trs[i]
        check = html.find("td").get_text()
        if check != "해당 조건/분류에 일치하는 채용정보가 없습니다.":
            place = check.replace('\xa0'," ")
            if html.find("span",{"class":"company"}) is not None:
                title = html.find("span",{"class":"company"}).get_text()
            data = html.find("td",{"class":"data"}).get_text()
            pay1,pay2 = html.find("td",{"class":"pay"}).find_all("span")
            pay1 = pay1.get_text()
            pay2 = pay2.get_text()
            pay = pay1 + pay2
            regDate = html.find("td",{"class":"regDate last"}).get_text()
            mylist = {
                'place' : place,
                'title' : title,
                'data' : data,
                'pay' : pay,
                'regDate' : regDate
            }
            job_list.append(mylist)
        else:
            mylist = {}
            job_list.append(mylist)
    return job_list

    
def main():
    brand_list = get_super_brand()
    job_list = []

    for item in brand_list:
        url = item[1]+"job/brand"
        job_list = get_jobs(url)
        file = open(item[0]+".csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["place", "title", "time", "pay","date"])
        # 파일 쓰기
        if job_list is not None:
            for job in job_list:
                writer.writerow(list(job.values()))
    

main()