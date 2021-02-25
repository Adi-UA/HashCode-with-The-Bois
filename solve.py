filename = "a.txt"

with open(filename, "r") as file:
    D, I, S, V, F = [int(x) for x in file.readline().split()]
    nodeDict = {n:[] for n in range(I)}
    carDict = {}
    for _ in range(S):
        inp = file.readline().split()
        b, e = int(inp[0]), int(inp[1])
        sName = inp[2]
        sTime = int(inp[3])
        # each node has a list of tuples, each tuple has a street name, ending node and time to cross
        nodeDict[b].append((e, sName, sTime))

    for i in range(V):
        inp = file.readline().split()
        p = int(inp[0])
        carStreets = inp[1:]
        carDict[i] = carStreets

# algo here

# tester
print(D, I, S, V, F)
print(nodeDict)
print(carDict)
