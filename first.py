# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]


# 输出：[1, 4, 9, 16, 25]
lst = [1,2,3,4,5]
squared_lst = list(map(lambda x: x**2, lst))
print(squared_lst)


# 输出：[16, 25]
lst = [1,2,3,4,5]
squared_lst = [x**2 for x in lst if x**2 > 10]
print(squared_lst)
