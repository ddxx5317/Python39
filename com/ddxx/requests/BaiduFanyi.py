import requests
import json

if __name__ == "__main__":
    url = "https://fanyi.baidu.com/sug"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    keyWord = input("enter a key word:")
    data = {
        "kw": keyWord
    }
    response = requests.post(url=url, data=data, headers=headers)
    jsonObj = response.json()
    print(jsonObj)
    fileName = keyWord + ".json"
    fp = open(fileName, "w", encoding="utf-8")
    json.dump(jsonObj, fp=fp, ensure_ascii=False)
    print("OK！！！")
