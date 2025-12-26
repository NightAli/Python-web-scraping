# Auto-annotated: imports requests
import requests

url="https://uploads8.wikiart.org/images/claude-monet/view-at-rouelles-le-havre.jpg" #圖片網址
imgname=url.split("/")[5] #網址萃取出檔名
img1=requests.get(url)
f=open(f'download/{imgname}','wb') #開啟空白二進位檔案
f.write(img1.content)
f.close()
