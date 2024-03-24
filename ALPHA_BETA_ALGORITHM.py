# Initial values of Alpha and Beta
MAX, MIN = 1000000, -1000000
#Recursion Algorithm For ALPHABETAPRUNING
def MiniMax_AlphaBetaPruning(curDepth, nodeIndex, maxTurn,
            terminal_nodes, alpha, beta):
    if curDepth == 3:
        return terminal_nodes[nodeIndex]
    #base case and termination condition in the leaf-terminal nodes
    if maxTurn:
        best = MIN
        #Recursion for the right and left child nodes where we are in the max player
        for i in range(0, 2):

            val = MiniMax_AlphaBetaPruning(curDepth + 1, nodeIndex * 2 + i,
                          False, terminal_nodes, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX
        #Recursion for the right and left child nodes where we are in the min player
        for i in range(0, 2):

            val = MiniMax_AlphaBetaPruning(curDepth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    # Driver Code


if __name__ == "__main__":
    values = [15, 7, -7, 31, -65, 28, 0, -1]
    print("The optimal value is :", MiniMax_AlphaBetaPruning(0, 0, True, values, MIN, MAX))