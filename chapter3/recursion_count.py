def count_element(list):
    # 基线条件
    if list == []:
        return 0
    # 递归条件
    else:
        return 1 + count_element(list[1:]) 

# 测试
print(count_element([1,2,3]))
print(count_element([1,2,3,4]))
    
