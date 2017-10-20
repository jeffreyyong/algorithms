import math

def main():
     input = [
         '000000', 
              '0000000000', 
              '00000_00000', 
              '0 00000 000 0000',  ]

     for item in input:
         PlayBottleCapGame(item)

def PlayBottleCapGame(input):
    print('-------------------------------------------------------------')
    print('The board starts this way -> ' + input)
    print('Player 1 starts')
    player1Win = False
    player1Turn = True
    inputList = []
    pairs = 0
    lastZero = False
    for item in input:
        if item == '0':
            if lastZero == True:
                pairs += 1
                lastZero = False
                inputList.append(item)
                continue
            lastZero = True
        else:
            lastZero = False
        inputList.append(item)

    
    while inputList.count('0') > 0:
        print('The board starts this round like this -> ' + ''.join(inputList))
        pairs = CountZeros(inputList)
        areTwo = GetZeros(inputList)
        zeroCount = inputList.count('0')
        if (player1Turn):
            if pairs > 0 :
                if pairs - 1 == 0:
                    if zeroCount - 1 == 2 or (zeroCount - 2 == 2 and pairs > 0):
                        print('Player 1 wins, because no more pairs left after Player 1 removes this one and only two moves remains, one for Player 2 and the finish one for Player 1 -> ' + ''.join(inputList))
                        player1Win = True
                        break
                    else:
                        if zeroCount <= 2:
                            inputList[areTwo[0]] = '_'
                            inputList[areTwo[0] + 1] = '_'
                            print('Player 1 makes a move, and the result is -> ' + ''.join(inputList))
                        else:
                            pairs -= 1
                            inputList[areTwo[0]] = '_'
                            print('Player 1 makes a move, and the result is -> ' + ''.join(inputList))
                else:
                    if pairs - 1 == 1:
                         i = 0
                         for item in inputList:
                            if item == '0':
                                inputList[i] = '_'
                                print('Player 1 makes a move, and the result is -> ' + ''.join(inputList))
                                break
                            i += 1
                    else:
                        pairs -= 1
                        if math.fmod(zeroCount - 2,2) != 0:
                            inputList[areTwo[0]] = '_'
                            print('Player 1 makes a move, and the result is -> ' + ''.join(inputList))
                        else:
                            inputList[areTwo[0]] = '_'
                            inputList[areTwo[0] + 1] = '_'
                            print('Player 1 makes a move, and the result is -> ' + ''.join(inputList))
            else:
                i = 0
                for item in inputList:
                    if item == '0':
                        inputList[i] = '_'
                        print('Player 1 makes a move, and the result is -> ' + ''.join(inputList))
                        break
                    i += 1
            player1Turn = False
            if inputList.count('0') == 0:
                player1Win = True
        else:
            if pairs > 0 :
                if pairs - 1 == 0:
                    if math.fmod(zeroCount - 2,2) == 0:
                        pairs -= 1
                        inputList[areTwo[0]] = '_'
                        print('Player 2 makes a move, and the result is -> ' + ''.join(inputList))
                    else:
                        if pairs - 1 > 0:
                            pairs -= 1
                            inputList[areTwo[0]] = '_'
                            print('Player 2 makes a move, and the result is -> ' + ''.join(inputList))
                        else:
                            pairs -= 1
                            inputList[areTwo[0]] = '_'
                            inputList[areTwo[0] + 1] = '_'
                            print('Player 2 makes a move, and the result is -> ' + ''.join(inputList))
                else:
                    if pairs - 1 == 1:
                        i = 0
                        for item in inputList:
                            if item == '0':
                                inputList[i] = '_'
                                print('Player 2 makes a move, and the result is -> ' + ''.join(inputList))
                                break
                            i += 1
                    else:
                        pairs -= 1
                        inputList[areTwo[0]] = '_'
                        inputList[areTwo[0] + 1] = '_'
                        print('Player 2 makes a move, and the result is -> ' + ''.join(inputList))
            else:
                i = 0
                for item in inputList:
                    if item == '0':
                        inputList[i] = '_'
                        print('Player 2 makes a move, and the result is -> ' + ''.join(inputList))
                        break
                    i += 1
            player1Turn = True
            if inputList.count('0') == 1:
                player1Win = True

    if player1Win == True:
        print('Player 1 wins using input -> ' + input)
    else:
        print('Player 2 wins! Wrong algorithm!')

def CountZeros(input):
    pairs = 0
    lastZero = False
    for item in input:
        if item == '0':
            if lastZero == True:
                pairs += 1
                lastZero = False
                continue
            lastZero = True
        else:
            lastZero = False
    return pairs

def GetZeros(inputList):
    i = 0
    index = 0
    count = 0
    areTwo = False
    for item in inputList:
        if item == '0':
            count += 1
        else:
            count = 0
        i += 1
        if count == 2:
            areTwo = True
            index = i - 2
            break
    return (index, areTwo)

if __name__ == "__main__":
    main()
