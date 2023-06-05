# 83、正则匹配以163.com结尾的邮箱


import re

email = "abc@163.com"
pattern = r"\w+@163\.com$"
result = re.match(pattern, email)
if result:
    print("匹配成功")
else:
    print("匹配失败")
