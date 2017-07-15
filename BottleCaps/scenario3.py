
# set cap list
capCount = 16
capList = ["O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O"]

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
    elif playerName == "beginning":
        playerName = str("\033[90m") + playerName + str("\033[0m")

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
    if selectedCaps[0] > 4 and selectedCaps[0] < 12:
        # print("first")
        offset = 4
        tempcapCount = 7
        for i in range(0, len(selectedCaps)):
            if selectedCaps[i] - offset > tempcapCount / 2:
                # print(len(selectedCaps))
                # print("first first")
                selectedCaps[i] = selectedCaps[i] - tempcapCount / 2 - 1
            else:
                # print(i)
                # print(len(selectedCaps))
                # print("first second")
                selectedCaps[i] = selectedCaps[i] + tempcapCount / 2 + 1
                # print(tempcapCount / 2)
                # print(selectedCaps[i])

        return selectedCaps
    elif selectedCaps[0] == 1:
        # print("second")
        retCaps = []
        if capList[13] == "O" and capList[14] == "O":
            # print("second first")
            retCaps.append(14)
            retCaps.append(15)
        else:
            # print("second second")
            for i in range(12, 16):
                if capList[i] == "O":
                    retCaps.append(i + 1)
        return retCaps
    else:
        print("third")
        retCaps = []
        if len(selectedCaps) == 1:
            print("third first")
            if capList[selectedCaps[0] - 2] == "O" and capList[selectedCaps[0] - 3] == "O":
                print("third first first")
                retCaps.append(selectedCaps[0] - 2)
                retCaps.append(selectedCaps[0] - 1)
            elif selectedCaps[0] < 15 and capList[selectedCaps[0]] == "O" and capList[selectedCaps[0] + 1] == "O":
                print("third first second")
                retCaps.append(selectedCaps[0] + 1)
                retCaps.append(selectedCaps[0] + 2)
            else:
                print("third first third")
                for i in range(12, 16):
                    if capList[i] == "O" and i != selectedCaps[0] - 1:
                        retCaps.append(i + 1)
                if len(retCaps) == 0 and capList[0] == "O": retCaps.append(1)
        else:
            print("third second")
            if capList[selectedCaps[0] - 2] == "O":
                print("third second first")
                retCaps.append(selectedCaps[0] - 1)
            elif capList[selectedCaps[1]] == "O":
                print("third second second")
                retCaps.append(selectedCaps[0] + 2)
            else:
                print("third second third")
                if capList[0] == "O": retCaps.append(1)
                print("third second third first")

        return retCaps

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
outputCapList("starting")
capList[2] = "P1"
capList[3] = "P1"
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
