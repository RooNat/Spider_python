import requests

url="https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start=0&limit=20"

#重新封装参数
params={
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

resp=requests.get(url=url,params=params)

print(resp.request.url)
print(resp.text) #结果为空意味着被反爬了，此处尝试user-agent

#此处尝试默认User-agent
print(resp.request.headers)
#有结果可见默认user-agent为python,此时需将前面的u-a换成浏览器

header={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

resp=requests.get(url=url,params=params,headers=header)

print(resp.json())

resp.close()  #关闭response,否则会报错。