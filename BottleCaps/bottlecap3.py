capCount = 16
capList = ["O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O"]


def output_cap_list(playerName):
    if playerName == "player1":
        playerName = str("\033[91m") + playerName + str("\033[0m")
    elif playerName == "player2":
        playerName = str("\033[0;32m") + playerName + str("\033[0m")
    elif playerName == "beginning":
        playerName = str("\033[90m") + playerName + str("\033[0m")

    capListStr = ""
    for i in range(0, len(capList)):
        cap = capList[i]
        if cap == "P1":
            capList[i] = "X"
            capListStr += str("\033[91mX\033[0m")
        elif cap == "P2":
            capList[i] = "X"
            capListStr += str("\033[0;32mX\033[0m")
        elif cap == "X":
            capListStr += "_"
        else:
            capListStr += cap

    print(playerName + ": " + capListStr)

    if capList.count(capList[0]) == len(capList):
        print("*"*50 + "\n" + playerName + " WON!")


# def validateForInput(selectedCaps):
#     length = len(selectedCaps)
#     if length == 0 or length > 2:
#         return False

#     if int(selectedCaps[1]) - int(selectedCaps[0]) != 1:
#         return False

#     for index in selectedCaps:
#         try:
#             i = int(index)
#             if capList[i-1] != "0": return False
#         except:
#             return False

#     return True

def validateForInput(selectedCaps):
    if len(selectedCaps) == 0 or len(selectedCaps) > 2: return False

    for one in selectedCaps:
        try:
            temp = int(one)
            if capList[temp-1] != "O": return False
        except:
            return False

    if len(selectedCaps) == 1: return True
    if int(selectedCaps[1]) - int(selectedCaps[0]) != 1: return False

    return True


def removeSelectedCapsFromCapList(playerName, selectedCaps):
    if playerName == "player1": markString = "P1"
    if playerName == "player2": markString = "P2"
    for position in selectedCaps:
        capList[position-1] = markString

    output_cap_list(playerName)



def selectCapsForComputer(selectedCaps):
    if selectedCaps[0] > 4 and selectedCaps[0] < 12:
        for i in range(0, len(selectedCaps)):
            if selectedCaps[i] > 7:
                selectedCaps[i] = selectedCaps[i] - 4
            else:
                selectedCaps[i] = selectedCaps[i] + 4

        return selectedCaps

    elif selectedCaps[0] == 1:
        returnCaps = []
        if capList[13] == "O" and capList[14] == "O":
            returnCaps.extend([14,15])
        else:
            for i in range(12, 16):
                if capList[i] == "O":
                    returnCaps.append(i + 1)
        return returnCaps
    
    else:
        returnCaps = []
        if len(selectedCaps) == 1:
            if capList[selectedCaps[0] - 2] == "O" and capList[selectedCaps[0] - 3] == "O":
                returnCaps.extend([selectedCaps[0] - 2, selectedCaps[0] - 1])
            elif selectedCaps[0] < 15 and capList[selectedCaps[0]] == "O" and capList[selectedCaps[0] + 1] == "O":
                returnCaps.extend([selectedCaps[0] + 2, selectedCaps[0] + 1])
            else:
                for i in range(12, 16):
                    if capList[i] == "O" and i != selectedCaps[0] - 1:
                        returnCaps.append(i + 1)
                if len(returnCaps) == 0 and capList[0] == "O":
                    returnCaps.append(1)
        else:
            if capList[selectedCaps[0] - 2] == "O":
                returnCaps.append(selectedCaps[0] - 1)
            elif capList[selectedCaps[0] + 1] == "O":
                returnCaps.append(selectedCaps[0] + 2)
            else:
                if capList[0] == "O": returnCaps.append(1)

        return returnCaps


def endGame():
    for cap in capList:
        if cap != "X": return False
    return True


# player the game

output_cap_list("starting")
capList[2] = "P1"
capList[3] = "P2"
output_cap_list("player1")

while(endGame() == False):
    selectedCaps = []
    while(validateForInput(selectedCaps) == False):
        try:
            selectedCaps = list(input("Please choose one or two caps(5, or 5,6): "))
        except:
            print("Try to choose again.")
    removeSelectedCapsFromCapList("player2", selectedCaps)

    selectedCaps = selectCapsForComputer(selectedCaps)

    removeSelectedCapsFromCapList("player1", selectedCaps)








    






            
            





        

