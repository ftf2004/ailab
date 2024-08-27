class Environment:
    def __init__(self):
        # A simple 3x3 room with some dirty spots
        self.room = [
            ['C', 'D', 'C'],
            ['D', 'C', 'D'],
            ['C', 'C', 'D']
        ]
        self.agent_position = (0, 0)

    def get_percept(self):
        x, y = self.agent_position
        return self.room[x][y]

    def clean_spot(self):
        x, y = self.agent_position
        if self.room[x][y] == 'D':
            self.room[x][y] = 'C'

    def move_agent(self, new_position):
        self.agent_position = new_position


class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment

    def act(self):
        if self.environment.get_percept() == 'D':
            self.environment.clean_spot()


class ModelBasedAgent:
    def __init__(self, environment):
        self.environment = environment
        self.model = [['C' for _ in range(3)] for _ in range(3)]  # Initially assume all spots are clean

    def update_model(self):
        x, y = self.environment.agent_position
        self.model[x][y] = self.environment.get_percept()

    def act(self):
        self.update_model()
        x, y = self.environment.agent_position
        if self.model[x][y] == 'D':
            self.environment.clean_spot()


class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment
        self.goal = 'Clean'  # The goal is to clean the room

    def act(self):
        if self.environment.get_percept() == 'D' and self.goal == 'Clean':
            self.environment.clean_spot()

    def move_towards_goal(self):
        # Simple movement strategy for demonstration
        for i in range(3):
            for j in range(3):
                if self.environment.room[i][j] == 'D':
                    self.environment.move_agent((i, j))
                    return


# Example usage
environment = Environment()

print("Initial Room State:")
for row in environment.room:
    print(row)

# Simple Reflex Agent
print("\nSimple Reflex Agent:")
simple_reflex_agent = SimpleReflexAgent(environment)
simple_reflex_agent.act()
for row in environment.room:
    print(row)

# Model-Based Agent
print("\nModel-Based Agent:")
model_based_agent = ModelBasedAgent(environment)
model_based_agent.act()
for row in environment.room:
    print(row)

# Goal-Based Agent
print("\nGoal-Based Agent:")
goal_based_agent = GoalBasedAgent(environment)
goal_based_agent.move_towards_goal()  # Move to a dirty spot
goal_based_agent.act()
for row in environment.room:
    print(row)
