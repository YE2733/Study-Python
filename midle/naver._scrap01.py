#네이버 웹페이지 긁어오기
from urllib.request import Request, urlopen

req = Request('http://www.naver.com/')
res = urlopen(req)
print(res.status)

