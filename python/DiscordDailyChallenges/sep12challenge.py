# get distance between pts if on same vert/horizontal line, else return 0
def sameLineDistance(p1,p2):
    if p1 == p2: return 0
    if p1[0] == p2[0]: return abs(p1[1] - p2[1])
    if p1[1] == p2[1]: return abs(p1[0] - p2[0])
    return 0

# check that each point has exactly two "neighbours", points that are equidistant and on the same lines
list = [[8,6],[6,6],[6,8],[8,8]]
for p1 in list:
    distance = 0
    validNeighbours = 0
    for p2 in list:
        x = sameLineDistance(p1,p2)
        if x == 0: continue
        if distance == 0: distance = x
        if x == distance: validNeighbours += 1
    if validNeighbours != 2:
        print("false")
        quit()
print("true")
