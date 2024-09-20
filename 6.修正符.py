# 阿伟练习
'''三.re模块中的常用函数
re.I 是匹配对大小写不敏感
re.M 多行匹配，影响到^和$
re.S 是.匹配包含换行符的所有字符'''

import re

myStr ='''
<a href="http://www.baidu.com">百度</a>
<A href="http://www.baidu.com">百度</A>
<a href="http://www.baidu.com">百度</a>
<a href='http://www.tengxun.com]'>腾
讯</a>
'''

#匹配所有的正常a链接
#print(re.findall("<a href=\"http://www.baidu.com\">百度</a>",))
print(re.findall('<a href="(.*?)">(.*?)</a>',myStr))

#修正符号
#匹配大小写
print(re.findall('(<a href="(.*?)">(.*?)</a>)',myStr,re.I))

#匹配大小写，多行匹配 可以匹配换行符
print(re.findall('(<a href=[\'"](.*?)[\'"]>(.*?)</a>)',myStr,re.I|re.M|re.S))

