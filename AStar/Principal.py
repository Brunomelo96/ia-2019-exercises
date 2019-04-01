from collections import deque

'''
    This code was writenn by Bruno Melo Moreira
'''

'''
    The heuristic is based on the straight-line distance to bucharest.
'''

class City:
    name = None
    childs = None
    depth = None
    distance = None
    heuristic = None

    def __init__(self, name, childs, distance, heuristic):
        self.name = name
        self.childs = childs
        self.distance = distance
        self.heuristic = heuristic


eforie = City("Eforie", None, 86, 161)
neamt = City("Neamt", None, 87, 234)
hirsova = City("Hiraova", [eforie], 98, 151)
iasi = City("Iasi", [neamt], 92, 226)
vaslui = City("Vaslui", [iasi], 142, 199)
urziceni = City("Urziceni", [vaslui, hirsova], 85, 80)
giurgiu = City("Giurgiu", None, 90, 77)

bucharest = City("Craiova", [giurgiu, urziceni], 101, 0)
pitesti = City("Pitesti", [bucharest], 138, 98)
craiova = City("Craiova", [pitesti], 146, 160)
bucharest = City("Bucharest", [giurgiu, urziceni], 101, 0)
pitesti = City("Pitesti", [bucharest], 97, 98)
rimnicuVilcea = City("Rimnicu Vilcea", [craiova, pitesti], 80, 193)
bucharest = City("Bucharest", [giurgiu, urziceni], 211, 0)
fagaras = City("Fagaras", [bucharest], 99, 176)
sibiu = City("Sibiu", [rimnicuVilcea, fagaras], 151, 253)
oradea = City("Oradea", [sibiu], 71, 380)
zerind = City("Zerind", [oradea], 75, 374)



bucharest = City("Bucharest", [giurgiu, urziceni], 101, 0)
pitesti = City("Pitesti", [bucharest], 138, 98)
craiova = City("Craiova", [pitesti], 146, 160)
bucharest = City("Bucharest", [giurgiu, urziceni], 101, 0)
pitesti = City("Pitesti", [bucharest], 97, 98)
rimnicuVilcea = City("Rimnicu Vilcea", [craiova, pitesti], 80, 193)
bucharest = City("Bucharest", [giurgiu, urziceni], 211, 0)
fagaras = City("Fagaras", [bucharest], 99, 176)
sibiu = City("Sibiu", [rimnicuVilcea, fagaras], 140, 253)


bucharest = City("Bucharest", [giurgiu, urziceni], 101, 0)
pitesti = City("Pitesti", [bucharest], 138, 98)
rimnicuVilcea  = City("Pitesti", [pitesti], 146, 193)
bucharest = City("Bucharest", [giurgiu, urziceni], 101, 0)
pitesti = City("Pitesti", [bucharest], 138, 98)
craiova = City("Craiova", [pitesti, rimnicuVilcea ], 120, 160)
dobreta = City("Dobreta", [craiova], 75, 242)
mehadia = City("Mehadia", [dobreta], 70, 241)
lugoj = City("Lugoj", [mehadia], 111, 244)
timisoara = City("Timisoara", [lugoj], 118, 329)
arad = City("Arad", [timisoara, sibiu, zerind], 0, 366)

def getNextCity(city):
    minChild = city.childs[0]
    for child in city.childs:
        nextDestination = child.distance + child.heuristic
        minDestination = minChild.distance + minChild.heuristic
        if(nextDestination < minDestination):
            minChild = child
    return minChild

def aStar(firstCity, destination):
    queue = deque([firstCity])
    path = []
    while (True):
        city = queue.popleft()
        path.append(city.name)
        if (city.name == destination):
            print(path)
            break
        else:
            queue.append(getNextCity(city))

aStar(arad, "Bucharest")