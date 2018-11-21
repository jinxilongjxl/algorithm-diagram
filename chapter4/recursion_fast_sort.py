def fast_sort(list): 
    # 基准条件
    if len(list) < 2:
        return list
    # 递归条件
    pivot = list[0]
    less = [val for val in list[1:] if val < pivot]
    greater = [val for val in list[1:] if val > pivot]
    return fast_sort(less) + [pivot] + fast_sort(greater)

# 测试
print(fast_sort([10,5,2,3]))



        
