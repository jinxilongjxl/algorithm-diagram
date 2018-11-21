def sum(list):
    # 基线条件
    if len(list) == 0:
        return 0
    # 递归条件
    else:
        return list[0] + sum(list[1:])

# 测试
print(sum([1,2,3])) # 6

# 分析
#    s1 sum([1,2,3])
#    s2 1 + sum([2,3])
#    s3 1 + 2 + sum([3])
#    s4 1 + 2 + 3 + sum([])
#    s5 1 + 2 + 3 + 0
#    s6 1 + 2 + 3
#    s7 1 + 5
#    s6 6
