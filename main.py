#用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容


from urllib.request import urlopen

url="http://www.baidu.com"
resp=urlopen(url)  #打开网址得到的响应

# print(resp.read().decode("utf-8"))

#字节转换成中文
trans=resp.read().decode("utf-8")

#将内容写到文件中
with open("mybaidu.html", mode="w") as f:
    f.write(trans)

print("over!")

#-------------------------------------------------------------------------------------
import requests
query=input("输入一个你感兴趣的名字")

url=f'https://www.sogou.com/web?query={query}'
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp=requests.get(url, headers=headers)  #处理一个小小的反爬，模拟浏览器访问数据

print(resp)

print(resp.text) #拿到页面源代码

resp.close()




