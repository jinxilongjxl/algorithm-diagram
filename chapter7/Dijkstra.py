# 准备数据
# 存储节点信息的散列表
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# print(graph["start"].keys()) # dict_keys(['a', 'b'])

graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["end"] = 5
graph["b"]["a"] = 3

graph["end"] = {}

# 存储COSTS的散列表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

# 存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None
# 存储已经处理过的节点
processed = []

# 处理前
print("=" * 50)
print("处理前parents")
print(parents)
print("=" * 50)
print("处理前costs")
print(costs)
print("=" * 50)
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 遍历costs字典的key,a,b,end
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def entry(costs):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

entry(costs)

# 处理后
print("处理后parents")
print(parents)
print("=" * 50)
print("处理后costs")
print(costs)
print("=" * 50)


