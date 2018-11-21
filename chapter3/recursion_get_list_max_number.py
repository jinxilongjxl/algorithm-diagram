def get_max_number(list):
    if len(list) == 1:
        return list[0]
    if len(list) >= 2:
        # 基线条件
        if len(list) == 2:
            return list[0] if list[0] > list[1] else list[1]
        # 递归条件
        return list[0] if list[0] > get_max_number(list[1:]) else get_max_number(list[1:])

# 测试
print(get_max_number([1,2,17,3]))
print(get_max_number([1,2,108,3,4]))
print(get_max_number([2]))
    
