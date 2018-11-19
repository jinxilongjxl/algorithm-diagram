# 选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # 找到数组中最小值，并返回其下表
        minIndex = findSmallest(arr)
        newArr.append(arr.pop(minIndex))
    return newArr

# 找出数组中的最小值
def findSmallest(arr):
    minIndex = 0
    minElement = arr[0]
    for i,val in enumerate(arr):
        if val < minElement:
            minIndex = i
            minElement = val
    return minIndex

# 测试
print(selectionSort([5,3,6,2,10]))
