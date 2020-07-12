import json

def initializeStates(items):
    states = {}

    for item in items:
       states[item.strip()] = {}

    return states

def addAction(actionInfo, actionName, states):
    if (actionName in states[actionInfo[0]]):
        states[actionInfo[0]][actionName].append({
            'toState': actionInfo[1],
            'probability': float(actionInfo[2]),
            'discard': float(actionInfo[3]),
            'cost': 1.00
        })
    else:
        states[actionInfo[0]][actionName] = [{
            'toState': actionInfo[1],
            'probability': float(actionInfo[2]),
            'discard': float(actionInfo[3]),
            'cost': 1.00
        }]

def addCost(costInfo, states):
    for action in states[costInfo[0]][costInfo[1]]:
        action["cost"] = float(costInfo[2])

def readFile(fileName):
    file1 = open(fileName, 'r')
    lines = file1.readlines()
    countLine = 0
    states = {}
    action = None
    cost = False
    initialState = ""
    goalState = ""

    for line in lines:
        countLine += 1
        if (line.strip() == "states"):
            states = initializeStates(lines[countLine].split(","))
        elif (line.strip() == "endcost"):
            cost = False
        elif (line.strip() == "cost"):
            cost = True
        elif (cost):
            addCost(line.strip().split(" "), states)
        elif (line.find("endaction") != -1):
            action = None
        elif (type(action) == str):
            actionInfo = line.strip().split(" ")
            addAction(actionInfo, action, states)
        elif (line.find("action") != -1):
            action = line.strip("action ").strip()
        elif (line.find("initialstate") != -1 and line.strip() == "initialstate"):
            initialState = lines[countLine].strip()
        elif (line.find("goalstate") != -1 and line.strip() == "goalstate"):
            goalState = lines[countLine].strip()

    return [
        states,
        initialState,
        goalState
    ]

def readInitialPolicyJson(jsonFile):
    file = open(jsonFile, 'r')
    lines = file.readlines()
    loadedJson = json.loads(lines[0])
    return loadedJson