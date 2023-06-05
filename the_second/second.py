# 22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"


s = "ajldjlajfdljfddd"
s_set = set(s)  
s_list = list(s_set)  
s_list.sort()  
result = ''.join(s_list) 
print(result)
