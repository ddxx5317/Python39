import requests

if __name__ == "__main__":
    url = "https://www.sogou.com/web"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    keyWord = input("enter a key word:")
    param = {
        "query": keyWord
    }
    response = requests.get(url=url, params=param, headers = headers)
    pageText = response.text
    # print(pageText)
    fileName = keyWord + ".html"
    with open(fileName, "w", encoding="utf-8") as fp:
        fp.write(pageText)
    print("爬取数据结束！！！")
