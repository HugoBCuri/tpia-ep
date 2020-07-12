import reader
import value
import policy

fileName = "TestesGrid/FixedGoalInitialState/navigation_1.txt"
jsonFile = "TestesGrid/FixedGoalInitialState/navigation_1.net_politicas.json"

print("###### {} ######".format(fileName))
states, initialState, goalState = reader.readFile(fileName)
# value.run(states, initialState, goalState)
policy.run(states, initialState, goalState, reader.readInitialPolicyJson(jsonFile))
