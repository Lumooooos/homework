# 82、s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong'] |表示或，根据冒号或者空格切分


import re

s = "info:xiaoZhang 33 shandong"
result = re.split(r':|\s', s)
print(result)
