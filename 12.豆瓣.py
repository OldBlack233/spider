# 阿伟练习
import re
f = open('豆瓣电影排行榜.html','rb')
data = f.read().decode('UTF-8')
f.close()

pattern = re.compile('<img src="\./豆瓣电影排行榜_files/p\d+\.webp" width="\d+" alt="\w+" class="">')
# print(pattern.findall(data))
with open('./img.html','w') as f:
    f.writelines(pattern.findall(data))