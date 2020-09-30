import urllib.request
from bs4 import BeautifulSoup
import re

html=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_937811.html').read()
soup = BeautifulSoup(html, "html.parser")

tags=soup('span')
sum=0
for tag in tags:
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print(tag.contents)
    num=tag.contents[0]
    num=int(num)
    # print('Attrs:', tag.attrs)
    sum=sum+num
print(sum)


# sum=0
# for line in fhandle:
#     line=line.rstrip()
#     line=line.decode()
#     y=re.findall('[0-9]+',line)
#     for num in y:
#         num=int(num)
#         sum=sum+num
#         print
# print(sum)

