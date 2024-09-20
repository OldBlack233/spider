# 阿伟练习
import re
pattern = re.compile('^1[3-9][0-9]{9}$',re.I)
print(re.search(pattern,'15391841384'))
print(re.search(pattern,'15391841384').group())
