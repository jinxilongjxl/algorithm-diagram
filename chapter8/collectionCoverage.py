# 集合覆盖问题
# 数据准备

# 需要覆盖的州
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])

# 广播台
stations = {}
stations["kone"]   = set(["id","nv","ut"])
stations["ktwo"]   = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"]  = set(["nv","ut"])
stations["kfive"]  = set(["ca","az"])

# 该集合用来存储最终选取的广播台
final_set = set()

while states_needed:
    # 覆盖了最多未覆盖州的电视台
    best_station = None
    # 该集合用来存储已经覆盖的州
    state_covered = set()

    for station,states_for_station in stations.items():
        covered = states_needed & states_for_station # covered = states_needed & state_covered
        if len(covered) > len(state_covered):
            best_station = station
            state_covered = covered
            final_set.add(best_station)
        states_needed -= state_covered

print(final_set)

