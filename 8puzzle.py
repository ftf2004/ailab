import copy
from heapq import heappush, heappop

# This variable can be adjusted for 8-puzzle (n=3) or 15-puzzle (n=4)
n = 3

# Directions: bottom, left, top, right
rows = [1, 0, -1, 0]
cols = [0, -1, 0, 1]

# Priority Queue implementation
class priorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap

# Node structure to store puzzle states
class nodes:
    def __init__(self, parent, mats, empty_tile_posi, costs, levels):
        self.parent = parent
        self.mats = mats
        self.empty_tile_posi = empty_tile_posi
        self.costs = costs
        self.levels = levels

    def __lt__(self, nxt):
        return self.costs < nxt.costs

# Calculate the number of misplaced tiles (heuristic function)
def calculateCosts(mats, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mats[i][j] and mats[i][j] != final[i][j]:
                count += 1
    return count

# Generate a new node after moving the empty tile
def newNodes(mats, empty_tile_posi, new_empty_tile_posi, levels, parent, final) -> nodes:
    new_mats = copy.deepcopy(mats)
    x1, y1 = empty_tile_posi
    x2, y2 = new_empty_tile_posi
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]
    costs = calculateCosts(new_mats, final)
    return nodes(parent, new_mats, new_empty_tile_posi, costs, levels)

# Print the N*N matrix
def printMatrix(mats):
    for i in range(n):
        for j in range(n):
            print("%d " % mats[i][j], end=" ")
        print()

# Check if the tile position is valid
def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n

# Print the solution path from root to final state
def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.mats)
    print()

# Solve N*N-1 puzzle using Branch and Bound
def solve(initial, empty_tile_posi, final):
    pq = priorityQueue()
    costs = calculateCosts(initial, final)
    root = nodes(None, initial, empty_tile_posi, costs, 0)
    pq.push(root)

    while not pq.empty():
        minimum = pq.pop()

        if minimum.costs == 0:
            printPath(minimum)
            return

        for i in range(n):
            new_tile_posi = [minimum.empty_tile_posi[0] + rows[i], minimum.empty_tile_posi[1] + cols[i]]
            if isSafe(new_tile_posi[0], new_tile_posi[1]):
                child = newNodes(minimum.mats, minimum.empty_tile_posi, new_tile_posi, minimum.levels + 1, minimum, final)
                pq.push(child)

# Initial puzzle configuration (0 represents the blank space)
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_tile_posi = [1, 2]

# Solve the puzzle
solve(initial, empty_tile_posi, final)
