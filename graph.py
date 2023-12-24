from collections import deque
#  graph example with usage of dict datatype

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []

print(graph)
print("okay, lets realize it...")

search_queue = deque()
search_queue += graph["you"]

print(search_queue)


def person_is_seller(name):
    return name[-1] == 'm'


while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + " is a mango seller!")
    else:
        search_queue += graph[person]



