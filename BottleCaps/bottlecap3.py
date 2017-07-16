cap_count = 16
cap_list = ["O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O"]

def output_cap_list(player_name):
    if player_name == "player1":
        player_name = str("\033[91m") + player_name + str("\033[0m")
    elif player_name == "player2":
        player_name = str("\033[0;32m") + player_name + str("\033[0m")
    elif player_name == "beginning":
        player_name = str("\033[90m") + player_name + str("\033[0m")

    cap_list_str = ""
    for i in range(0, len(cap_list)):
        cap = cap_list[i]
        if cap == "P1":
            cap_list[i] = "X"
            cap_list_str += str("\033[91mX\033[0m")
        elif cap == "P2":
            cap_list[i] = "X"
            cap_list_str += str("\033[0;32mX\033[0m")
        elif cap == "X":
            cap_list_str += "_"
        else:
            cap_list_str += cap

    print(player_name + ": " + cap_list_str)

    if cap_list.count(cap_list[0]) == len(cap_list):
        print("*"*50 + "\n" + player_name + " WON!")


# def validate_for_input(selected_caps):
#     length = len(selected_caps)
#     if length == 0 or length > 2:
#         return False

#     if int(selected_caps[1]) - int(selected_caps[0]) != 1:
#         return False

#     for index in selected_caps:
#         try:
#             i = int(index)
#             if cap_list[i-1] != "0": return False
#         except:
#             return False

#     return True

def validate_for_input(selected_caps):
    if len(selected_caps) == 0 or len(selected_caps) > 2: return False

    for one in selected_caps:
        try:
            temp = int(one)
            if cap_list[temp-1] != "O": return False
        except:
            return False

    if len(selected_caps) == 1: return True
    if int(selected_caps[1]) - int(selected_caps[0]) != 1: return False

    return True


def remove_select_caps(player_name, selected_caps):
    if player_name == "player1": mark_string = "P1"
    if player_name == "player2": mark_string = "P2"
    for position in selected_caps:
        cap_list[position-1] = mark_string

    output_cap_list(player_name)



def select_caps_for_bot(selected_caps):
    if selected_caps[0] > 4 and selected_caps[0] < 12:
        for i in range(0, len(selected_caps)):
            if selected_caps[i] > 7:
                selected_caps[i] = selected_caps[i] - 4
            else:
                selected_caps[i] = selected_caps[i] + 4

        return selected_caps

    elif selected_caps[0] == 1:
        return_caps = []
        if cap_list[13] == "O" and cap_list[14] == "O":
            return_caps.extend([14,15])
        else:
            for i in range(12, 16):
                if cap_list[i] == "O":
                    return_caps.append(i + 1)
        return return_caps
    
    else:
        return_caps = []
        if len(selected_caps) == 1:
            if cap_list[selected_caps[0] - 2] == "O" and cap_list[selected_caps[0] - 3] == "O":
                return_caps.extend([selected_caps[0] - 2, selected_caps[0] - 1])
            elif selected_caps[0] < 15 and cap_list[selected_caps[0]] == "O" and cap_list[selected_caps[0] + 1] == "O":
                return_caps.extend([selected_caps[0] + 2, selected_caps[0] + 1])
            else:
                for i in range(12, 16):
                    if cap_list[i] == "O" and i != selected_caps[0] - 1:
                        return_caps.append(i + 1)
                if len(return_caps) == 0 and cap_list[0] == "O":
                    return_caps.append(1)
        else:
            if cap_list[selected_caps[0] - 2] == "O":
                return_caps.append(selected_caps[0] - 1)
            elif cap_list[selected_caps[0] + 1] == "O":
                return_caps.append(selected_caps[0] + 2)
            else:
                if cap_list[0] == "O": return_caps.append(1)

        return return_caps


def end_game():
    for cap in cap_list:
        if cap != "X": return False
    return True


# player the game

def main():
    output_cap_list("starting")
    cap_list[2] = "P1"
    cap_list[3] = "P2"
    output_cap_list("player1")

    while(end_game() == False):
        selected_caps = []
        while(validate_for_input(selected_caps) == False):
            try:
                selected_caps = list(input("Please choose one or two caps(5, or 5,6): "))
            except:
                print("Try to choose again.")
        remove_select_caps("player2", selected_caps)

        selected_caps = select_caps_for_bot(selected_caps)

        remove_select_caps("player1", selected_caps)

if __name__ == '__main__':
    main()
