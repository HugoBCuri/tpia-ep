import time

def initializeValues(states):
    values = {}
    for state in states.keys():
        values[state] = {
            "value": 0,
            "action": None
        }
    return values

def updateValue(state, value, action, values):
    values[state] = {
        "value": value,
        "action": action
    }

def getBellmanBackup(stateInfo, values):
    minValue = 100000000000
    minAction = ""

    for action, actionInfo in stateInfo.items():
        value = 0

        for item in actionInfo:
            value += item["probability"] * (item["cost"] + values[item["toState"]]["value"])

        if (value < minValue):
            minValue = value
            minAction = action

    return [minValue, minAction]

def hasConverged(valuesPrev, values, goalState):
    diffs = []
    for key, value in values.items():
        if (goalState != key):
          diff = value["value"] - valuesPrev[key]["value"]
          diffs.append(diff)

    return max(diffs) <= 0.1

def printState(values, iteration, x = 21, y = 21):
    print("=------- {} -----".format(iteration))
    for i in reversed(range(1, x)):
        for j in range(1, y):
            if ("robot-at-x{}y{}".format(j, i) in values):
              action = values["robot-at-x{}y{}".format(j, i)]["action"]

              if ("move-south" == action):
                  print("v ", end = '')
              elif ("move-north" == action):
                  print("^ ", end = '')
              elif ("move-east" == action):
                  print("> ", end = '')
              elif ("move-west" == action):
                  print("< ", end = '')
              else:
                  print(" ", end = '')
            else:
              print("- ", end = '')
        print()

def run(states, initialState, goalState, length):
    values = initializeValues(states)
    n = 0
    start_time = time.time()

    for i in range(10000):
        valuesPrev = {**values}
        valuesPrev[goalState]["value"] = 0
        n += 1
        for state, stateInfo in states.items():

            minValue, minAction = getBellmanBackup(stateInfo, valuesPrev)
            updateValue(state, minValue, minAction, values)

        if (hasConverged(valuesPrev, values, goalState)):
            break
    print("--- {} seconds ---".format(time.time() - start_time))

    printState(values, n, length + 1, length + 1)
