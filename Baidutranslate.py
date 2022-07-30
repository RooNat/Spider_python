import requests #导入requests包

url="https://fanyi.baidu.com/"

s=input("请输入需要进行翻译的单词")

dat={
    "kw":s
}

resp=requests.post(url,data=dat)
print(resp.text)
