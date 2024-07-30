import random

class VacuumWorld:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice(['clean', 'dirty']) for _ in range(cols)] for _ in range(rows)]
        self.vacuum_pos = (0, 0)  # starting position at top-left corner

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

    def clean(self):
        row, col = self.vacuum_pos
        if self.grid[row][col] == 'dirty':
            self.grid[row][col] = 'clean'
            print(f"Cleaned room at position ({row}, {col})")
        else:
            print(f"Room at position ({row}, {col}) is already clean")

    def move(self):
        row, col = self.vacuum_pos
        if col < self.cols - 1:
            self.vacuum_pos = (row, col + 1)
        elif row < self.rows - 1:
            self.vacuum_pos = (row + 1, 0)

    def run(self):
        while any('dirty' in row for row in self.grid):
            self.clean()
            self.display_grid()
            self.move()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    vacuum_world = VacuumWorld(n, m)
    print("Initial grid state:")
    vacuum_world.display_grid()
    
    vacuum_world.run()
    print("Final grid state:")
    vacuum_world.display_grid()
