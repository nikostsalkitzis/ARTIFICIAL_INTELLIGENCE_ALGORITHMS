A* is the most up-to-date algorithm in modern era on artificial intelligence.
The algorithm is based on branch and bound applied in DFS or BFS(mainly in the first case).
Furthermore, we keep track for paths from root to the goal state-node and we try to minimize the sum
of the heuristic and real distance of the node to the goal. Simply, the heuristic is a prediction for the distance between the current node to the goal node.
Until we found all paths to goal states and return success, we select the node,simultaneously exapnding the path, with the samllest sum of real time and predictive distance.
If the heuristic is admissible, meaning that it always underpredict the distance the A* always fins the best solution to the path.
As a heuristic in this simple program we use Manhattan Distance because it is the most accurate when navigating in a grid without burdens.
The visualization of the 5x5 grid is done using X in order to find the path to the goal state.