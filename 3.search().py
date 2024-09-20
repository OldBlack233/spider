# 阿伟练习
import re #导入re正则模块
#search只匹配一次
print(re.search('a','123456'))
print(re.search('[a-z]','123456'))
print(re.search('[a-z]','123x456'))
print(re.search('[a-z][a-z]','123x456'))
print(re.search('[a-z][a-z]','123ab456'))
print(re.search('[a-z][0-9]{3}[a-z]','123x456a'))

print(re.search('1[3-9][0-9]{9}','15391841384'))
print(re.search('1[3-9][0-9]{9}','15391841384a'))
print(re.search('1[3-9][0-9]{9}','x15391841384a'))
print(re.search('^1[3-9][0-9]{9}','x15391841384a'))
print(re.search('^1[3-9][0-9]{9}$','15391841384a'))
print(re.search('^1[3-9][0-9]{9}$','15391841384'))
print(re.search('^1[3-9][0-9]{9}$','1539184138'))

#获取匹配的内容
print(re.search('^1[3-9][0-9]{9}$','15391841384').group())



