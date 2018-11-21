from collections import deque

# 准备数据
graph = {}
graph["you"] = ["bob","claire","alice"]
graph["bob"] = ["anuj","peggy"]
graph["claire"] = ["thon","jonny"]
graph["alice"] = ["peggy"]
graph["anuj"] = []
graph["peggy"] = []
graph["thon"] = []
graph["jonny"] = []
graph["peggy"] = []

# 定义函数判断是否为销售商
def is_seller(name):
    return name[-1] == 'm'

# 广度优先搜索算法
def bfs(name):
    search_quene = deque()
    search_quene += graph[name]
    searched = []
    while search_quene:
        # 取出队列中的第一人
        person = search_quene.popleft()
        if person not in searched:
            # 判断是否为销售商
            if is_seller(person):
                print("%s is a seller!" % (person))
                return True
            else:
                search_quene += graph[person]
                searched.append(person)
    return False

print(bfs("you"))





