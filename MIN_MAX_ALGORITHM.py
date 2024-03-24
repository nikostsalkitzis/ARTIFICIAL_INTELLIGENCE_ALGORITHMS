import math

#curDepth: Current Depth of the Node we examine
#maxTurn: It declares if the player Max is now playing
#scores:The terminal leaf nodes where the game starts
#targetDepth: How many levels of the tree we want to look for in order to get the decision
#nodeIndex:It represents the position of each node in the tree
def MinMax(curDepth, nodeIndex,
            maxTurn, terminal_nodes,
            targetDepth):
    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return terminal_nodes[nodeIndex]

    if (maxTurn):
        return max(MinMax(curDepth + 1, nodeIndex * 2,
                           False, terminal_nodes, targetDepth),
                   MinMax(curDepth + 1, nodeIndex * 2 + 1,
                           False, terminal_nodes, targetDepth))

    else:
        return min(MinMax(curDepth + 1, nodeIndex * 2,
                           True, terminal_nodes, targetDepth),
                   MinMax(curDepth + 1, nodeIndex * 2 + 1,
                           True, terminal_nodes, targetDepth))


# Driver code
terminal_nodes = [2, 7, -6, 32, 5, -9, 3, 45]
treeDepth = math.log(len(terminal_nodes), 2)
print(treeDepth)
print("The optimal value is : ", end="")
print(MinMax(0, 0, True, terminal_nodes, treeDepth))
