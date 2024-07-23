def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    loc = input("Enter Location of Vacuum: ")
    status = input("Enter status: ")
    otherstatus = input("Enter status of other room: ")

    if status == '1':
        print(f"Location {loc} is Dirty.")
        goal_state[loc] = '0'
        cost += 1
        print(f"Cost for CLEANING {loc} " + str(cost))

    if otherstatus == '1':
        otherloc = 'B' if loc == 'A' else 'A'
        print(f"Location {otherloc} is Dirty.")
        cost += 1
        print("Moving to other Location. Cost for moving " + str(cost))
        goal_state[otherloc] = '0'
        cost += 1
        print(f"Cost for CLEANING {otherloc}: " + str(cost))

    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))

vacuum_world()
