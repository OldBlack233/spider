# 阿伟练习
import re
#match 只匹配一次，必须从第一位开始，类似于search（"^"）
print(re.match('a','123456'))
print(re.match('[a-z]','123456'))
print(re.match('[a-z]','123x456'))
print(re.match('[a-z][a-z]','123x456'))
print(re.match('[a-z][a-z]','123ab456'))
print(re.match('[a-z][0-9]{3}[a-z]','123x456a'))

print(re.match('1[3-9][0-9]{9}','15391841384'))

print(re.match('1[3-9][0-9]{9}$','15391841384'))

