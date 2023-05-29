# 52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]


def sort_list(lst):
    if not lst:
        return []
    else:
        min_value = min(lst) 
        lst.remove(min_value)
        return [min_value] + sort_list(lst)

lst = [2, 3, 5, 4, 9, 6]
sorted_lst = sort_list(lst)
print(sorted_lst)
