def binary_search(list, target_number):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high)//2
        if list[mid] == target_number:
            return mid
        if list[mid] > target_number:
            high = mid - 1
        else:
            low = mid + 1
    return None

# 测试
list = [1,3,5,7,9]
print(binary_search(list, 5))
print(binary_search(list,2))
    
