# 阿伟练习
import re
obj = re.finditer('[a-z]',"abcdefg")
for i in obj:
    print(i)

obj2 = re.findall('[a-z]',"abcdefg")
print(obj2)
