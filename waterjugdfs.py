def DFS(a, b, target):
    # Helper function to perform DFS recursively
    def dfs(state, path, visited):
        if (state[0], state[1]) in visited:
            return False
        if (state[0] > a or state[1] > b or state[0] < 0 or state[1] < 0):
            return False
        
        # Add current state to path and mark as visited
        path.append([state[0], state[1]])
        visited.add((state[0], state[1]))

        # Check if we have reached the target
        if (state[0] == target or state[1] == target):
            # Print the solution path
            for p in path:
                print("(", p[0], ",", p[1], ")")
            return True

        # Explore all possible states
        # Fill Jug1
        if dfs((a, state[1]), path, visited):
            return True
        # Fill Jug2
        if dfs((state[0], b), path, visited):
            return True
        # Empty Jug1
        if dfs((0, state[1]), path, visited):
            return True
        # Empty Jug2
        if dfs((state[0], 0), path, visited):
            return True
        # Pour Jug1 to Jug2
        pour_to_jug2 = min(state[0], b - state[1])
        if dfs((state[0] - pour_to_jug2, state[1] + pour_to_jug2), path, visited):
            return True
        # Pour Jug2 to Jug1
        pour_to_jug1 = min(state[1], a - state[0])
        if dfs((state[0] + pour_to_jug1, state[1] - pour_to_jug1), path, visited):
            return True

        # Backtrack
        path.pop()
        return False

    # Initial state and setup
    initial_state = (0, 0)
    path = []
    visited = set()
    
    # Perform DFS
    if not dfs(initial_state, path, visited):
        print("No solution")

# Driver code
if __name__ == '__main__':
    Jug1, Jug2, target = 4, 3, 2
    print("Path from initial state to solution state ::")
    DFS(Jug1, Jug2, target)
