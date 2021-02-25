import math

filename = "f"

with open(filename+".txt", "r") as file:
    D, I, S, V, F = [int(x) for x in file.readline().split()]
    nodeDict = {n: [[], []] for n in range(I)}  # incoming streets, outgoing streets
    carDict = {}
    streetNames = []
    for _ in range(S):
        inp = file.readline().split()
        b, e = int(inp[0]), int(inp[1])
        sName = inp[2]
        sTime = int(inp[3])
        # each node has a list of tuples, each tuple has a street name, ending node and time to cross
        nodeDict[e][0].append((b, sName, sTime))
        nodeDict[b][1].append((e, sName, sTime))
        streetNames.append(sName)

    for i in range(V):
        inp = file.readline().split()
        p = int(inp[0])
        carStreets = inp[1:]
        carDict[i] = carStreets

# algo here
# weightage is heuristic for how important it is to open a street, higher = longer
weightages = {n: 0 for n in streetNames}
for i in range(V):
    for street in carDict[i]:
        weightages[street] += 1

timeSlice = min(int(math.sqrt(D)), D//10 + 10)  # time for each loop of lights

outputStringList = []
with open(filename+"_result.txt", "w+") as file:
    outputStringList.append(str(I)+"\n")
    for i in range(I):
        outputStringList.append(str(i)+"\n")
        weights = {tup[1]: weightages[tup[1]] for tup in nodeDict[i][0]}
        intersectionSum = sum([n for n in weights.values()])
        if intersectionSum == 0:  # intersection is never visited, leave one light on by default
            outputStringList.append("1\n" + nodeDict[i][0][0][1] + " 1\n")
            continue
        times = {n: timeSlice * math.ceil(weights[n]/intersectionSum) for n in weights if weights[n] > 0}
        outputStringList.append(str(len(times))+"\n")
        for name in times:
            outputStringList.append(name + " " + str(times[name]) + "\n")

    file.writelines(outputStringList)

print("Finished output for", filename+".txt")
# tester
# print(D, I, S, V, F)
# print(nodeDict)
# print(carDict)
