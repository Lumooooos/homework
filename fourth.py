# 39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]


a = [[1,2],[3,4],[5,6]]
result = [j for i in a for j in i]
print(result)
