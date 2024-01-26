states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az", "ny", "cb", "ar", "tx"])
stations = {}
stations["kone"] = set(["id", "nv", "ut", "tx", "ca", "az", "cb"])
stations["ktwo"] = set(["wa", "id", "mt", "tx", "ar", "or", "ny", "nv"])
stations["kthree"] = set(["or", "nv", "ut", "tx", "ca", "az", "ny", "mt", "id"])
stations["kfour"] = set(["az", "nv", "ut", "cb", "ny", "id"])
stations["kfive"] = set(["ca", "nv", "ut", "tx", "ny", "or", "wa", "az"])

final_stations = set()
best_station = None
states_covered = set()
for station, states_for_station in stations.items():
    covered = states_needed & states_for_station
    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered

states_needed -= states_covered
final_stations.add(best_station)
print(final_stations)


