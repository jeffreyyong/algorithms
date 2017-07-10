
# set cap list
capCount = 12
capList = ["O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"]

#///////////////////////////////////////////////////////
# function name: outputCapList
# function: print cap list
# params:
# date: 2017-07-10
#///////////////////////////////////////////////////////
def outputCapList(playerName):

    # set color for player name
    if playerName =="player1":
        playerName = str("\033[91m") + playerName + str("\033[0m")
    elif playerName == "player2":
        playerName = str("\033[0;32m") + playerName + str("\033[0m")

    # make string for output
    capListStr = ""
    for i in range(0, len(capList)):
        cap = capList[i]
        if cap == "P1":
            capList[i] = "X"
            capListStr += str("\033[91m_\033[0m")
        elif cap == "P2":
            capList[i] = "X"
            capListStr += str("\033[0;32m_\033[0m")
        elif cap == "X":
            capListStr += "_"
        else:
            capListStr += cap

    # print output string
    print(playerName + ": " + capListStr)

#///////////////////////////////////////////////////////
# function name: validateForInput
# function: validate for input value
# params:
# date: 2017-07-10
#///////////////////////////////////////////////////////
def validateForInput(selectedCaps):
    if len(selectedCaps) == 0: return False

    if len(selectedCaps) > 2: return False

    for one in selectedCaps:
        try:
            temp = int(one)
            if capList[temp-1] != "O": return False
        except:
            return False

    if len(selectedCaps) == 1: return True
    if int(selectedCaps[1]) - int(selectedCaps[0]) != 1: return False

    return True

#///////////////////////////////////////////////////////
# function name: removeSelectedCapsFromCapList
# function: remove selected caps from cap list
# params:
# date: 2017-07-10
#///////////////////////////////////////////////////////
def removeSelectedCapsFromCapList(playerName, selectedCaps):
    if playerName == "player1": markStr = "P1"
    if playerName == "player2": markStr = "P2"
    for position in selectedCaps:
        capList[position-1] = markStr

    outputCapList(playerName)

#///////////////////////////////////////////////////////
# function name: selectCapsForComputer
# function: select caps for computer
# params:
# date: 2017-07-10
#///////////////////////////////////////////////////////
def selectCapsForComputer(selectedCaps):
    for i in range(0, len(selectedCaps)):
        if selectedCaps[i] > capCount / 2:
            selectedCaps[i] = selectedCaps[i] - capCount / 2 - 1
        else:
            selectedCaps[i] = selectedCaps[i] + capCount / 2 + 1

    return selectedCaps

#///////////////////////////////////////////////////////
# function name: endGame
# function: check game state
# params:
# date: 2017-07-10
#///////////////////////////////////////////////////////
def endGame():
    for cap in capList:
        if cap != "X": return False
    return True

# first computer select cap
capList[5] = "P1"
outputCapList("player1")

while(endGame() == False):
    # player2(person) select caps
    selectedCaps = []
    while(validateForInput(selectedCaps) == False):
        try:
            selectedCaps = list(input("Please select one or two caps(ex-5, or 5,6): "))
        except:
            print("Try to input again.")

    # remove selected caps from capList
    removeSelectedCapsFromCapList("player2", selectedCaps)

    # player1(computer) select caps
    selectedCaps = selectCapsForComputer(selectedCaps)
    # remove selected caps from capList
    removeSelectedCapsFromCapList("player1", selectedCaps)