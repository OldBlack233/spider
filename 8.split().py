# 阿伟练习
#作用，切割字符串
import re
myStr = 'abc1\rde\t2\ndd3fg'
# 按照数字进行拆分
print(re.split("[0-9]",myStr))
print(re.split("[0-9]",myStr,maxsplit=2))
print(re.findall('\s',myStr))
print(re.findall('\S',myStr))

#按空白符拆分
print(re.split('\s',myStr))

