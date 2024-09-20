# 阿伟练习
import re

#re.M对于^$的影响
#\A和\Z和^ $ 一样的，只有在re.M时有区别
myStr = "abcd\nabcd"
print(re.findall('^a',myStr))
print(re.findall('\Aa',myStr))

print(re.findall('^a',myStr,re.M))
print(re.findall('\Aa',myStr,re.M))
