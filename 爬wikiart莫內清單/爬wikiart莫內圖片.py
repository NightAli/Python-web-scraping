# 註解（自動）：匯入 requests
import requests

src="https://uploads2.wikiart.org/images/claude-monet/the-japanis-bridge-footbridge-over-the-water-lily-pond.jpg!Large.jpg"
src=src.split("!")[0] #選擇高解析圖片網址
print(src)
imgname=src.split("/")[5] #選擇作品名稱


img1=requests.get(src)  #使用requests.get取得圖片資訊
f=open(f'download/{imgname}','wb') #將圖片開啟成為二進位格式
f.write(img1.content)
f.close()
