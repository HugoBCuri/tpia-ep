import reader
import value

fileName = "TestesGrid/RandomGoalInitialState/navigation_1.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 20)

fileName = "TestesGrid/RandomGoalInitialState/navigation_2.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 40)

fileName = "TestesGrid/RandomGoalInitialState/navigation_3.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 60)

fileName = "TestesGrid/RandomGoalInitialState/navigation_4.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 80)

fileName = "TestesGrid/RandomGoalInitialState/navigation_5.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 100)

fileName = "TestesGrid/RandomGoalInitialState/navigation_6.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 120)

fileName = "TestesGrid/RandomGoalInitialState/navigation_7.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 140)

fileName = "TestesGrid/RandomGoalInitialState/navigation_8.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 160)

fileName = "TestesGrid/RandomGoalInitialState/navigation_9.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 180)

fileName = "TestesGrid/RandomGoalInitialState/navigation_10.txt"
print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
value.run(states, initialState, goalState, 200)
