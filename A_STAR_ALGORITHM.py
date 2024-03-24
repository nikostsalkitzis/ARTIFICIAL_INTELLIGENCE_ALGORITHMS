import heapq


class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node
        self.g = g  # Cost from the start node to this node
        self.h = h  # Heuristic estimate from this node to the goal node

    def f(self):
        return self.g + self.h  # Total estimated cost of the cheapest solution

    def __lt__(self, other):
        return self.f() < other.f()  # Comparison based on total estimated cost


def astar(start_state, goal_state, heuristic, neighbors):
    open_set = []  # Priority queue of nodes to be evaluated
    closed_set = set()  # Set of nodes already evaluated

    start_node = Node(state=start_state, g=0, h=heuristic(start_state, goal_state))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current_node.state)

        for neighbor in neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            g = current_node.g + 1  # Assuming uniform cost for each step
            h = heuristic(neighbor, goal_state)
            new_node = Node(state=neighbor, parent=current_node, g=g, h=h)

            # Check if the neighbor is already in the open set
            for existing_node in open_set:
                if existing_node.state == neighbor and new_node.f() < existing_node.f():
                    open_set.remove(existing_node)
                    heapq.heapify(open_set)
                    break

            heapq.heappush(open_set, new_node)

    return None  # No path found


def visualize_grid(start_state, goal_state, path, explored_states=None):
    grid_size = 5  # Size of the grid
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    start_x, start_y = start_state
    goal_x, goal_y = goal_state

    # Mark start and goal states
    grid[start_y][start_x] = 'S'
    grid[goal_y][goal_x] = 'G'

    # Mark path
    if path:
        for state in path:
            x, y = state
            grid[y][x] = 'X'

    # Mark explored states if provided
    if explored_states:
        for state in explored_states:
            x, y = state
            if grid[y][x] == '.':
                grid[y][x] = 'o'  # Explored but not part of the path

    # Print the grid
    for row in grid:
        print(' '.join(row))


# Example usage
def manhattan_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbors(state):
    x, y = state
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]  # Assuming 4-connected grid
    return [(x, y) for x, y in neighbors if 0 <= x < 5 and 0 <= y < 5]  # Boundaries of the grid


if __name__ == "__main__":
    start_state = (0, 0)
    goal_state = (4, 4)

    path = astar(start_state, goal_state, heuristic=manhattan_distance, neighbors=get_neighbors)

    if path:
        print("Path found:")
        visualize_grid(start_state, goal_state, path)
    else:
        print("No path found")
