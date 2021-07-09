import requests

if __name__ == "__main__":
    url = "https://www.sogou.com"
    response = requests.get(url=url)
    pageText = response.text
    print(pageText)
    with open("datas/data.html", "w", encoding="utf-8") as fp:
        fp.write(pageText)
    print("爬取数据结束！！！")
