import requests
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    params = {
        "type": 7,
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 10
    }
    response = requests.get(url=url, params=params, headers=headers)
    jsonObj = response.json()
    print(jsonObj)
    fileName = "douban.json"
    fp = open(fileName, "w", encoding="utf-8")
    json.dump(jsonObj, fp=fp, ensure_ascii=False)
    print("OK！！！")
