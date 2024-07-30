class VacuumCleaner:

    def __init__(self):

        # Initialize the environment

        self.environment = {'A': 'Dirty', 'B': 'Dirty'}  # Both rooms start dirty

        self.location = 'A'  # The vacuum starts in room A

        self.model = {'A': 'Dirty', 'B': 'Dirty'}  # Model of the environment

        self.steps = 0

    def update_model(self):

        # Update the model based on the current environment state

        self.model[self.location] = self.environment[self.location]

    def perception(self):

        # The vacuum perceives the current state of the room it's in

        return self.model[self.location]

    def action(self):

        # Decide on an action based on the model

        state = self.perception()

        

        if state == 'Dirty':

            return 'Clean'

        else:

            # Move to the other room if the current room is clean

            return 'Move' if self.location == 'A' else 'Move Back'

    def execute_action(self, action):

        if action == 'Clean':

            print(f"Cleaning room {self.location}")

            self.environment[self.location] = 'Clean'

        elif action == 'Move':

            self.location = 'B'

        elif action == 'Move Back':

            self.location = 'A'

        self.steps += 1

    def run(self):

        while any(value == 'Dirty' for value in self.environment.values()):

            self.update_model()

            action = self.action()

            self.execute_action(action)

            print(f"Location: {self.location}, Environment: {self.environment}, Steps: {self.steps}")

# Initialize and run the vacuum cleaner agent

agent = VacuumCleaner()

agent.run()