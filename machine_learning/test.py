import requests
import json

url = 'http://127.0.0.1:8888/lr'#请求接口
data = {'city': '保定','experience': 2,'education': '硕士'}
req = requests.post(url, data)#发送post请求，第一个参数是URL，第二个参数是请求数据
print(req.text)