#用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容


from urllib.request import urlopen

url="http://www.baidu.com"
resp=urlopen(url)  #打开网址得到的响应

resp.read()

print(resp.read().decode("utf-8"))




