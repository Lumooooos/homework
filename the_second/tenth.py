# 85、python字典和json字符串相互转化方法


import json

# 将Python字典转换为JSON字符串
my_dict = {"name": "John", "age": 30, "city": "New York"}
json_str = json.dumps(my_dict)
print(json_str)

# 将JSON字符串转换为Python字典
json_str = '{"name": "Tom", "age": 20, "city": "Kun Ming"}'
my_dict = json.loads(json_str)
print(my_dict)
