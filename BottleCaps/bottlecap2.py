class BottleCapGame(object):
    def __init__(self, cap_list):
        self.cap_list = cap_list

    def output_cap_list(self, player_name):

        if player_name =="player1":
            player_name = str("\033[91m") + player_name + str("\033[0m")
        elif player_name == "player2":
            player_name = str("\033[0;32m") + player_name + str("\033[0m")
        elif player_name == "start":
            player_name = str("\033[90m") + player_name + str("\033[0m")

        cap_list_str = ""
        for i in range(0, len(self.cap_list)):
            cap = self.cap_list[i]
            if cap == "P1":
                self.cap_list[i] = "X"
                cap_list_str += str("\033[91m_\033[0m")
            elif cap == "P2":
                self.cap_list[i] = "X"
                cap_list_str += str("\033[0;32m_\033[0m")
            elif cap == "X":
                cap_list_str += "_"
            else:
                cap_list_str += cap

        print(player_name + ": " + cap_list_str)

    def validate_for_input(self, selected_caps):
        if len(selected_caps) == 0: return False

        if len(selected_caps) > 2: return False

        for one in selected_caps:
            try:
                temp = int(one)
                if self.cap_list[temp-1] != "O": return False
            except:
                return False

        if len(selected_caps) == 1: return True
        if int(selected_caps[1]) - int(selected_caps[0]) != 1: return False

        return True

    def remove_selected_caps(self, player_name, selected_caps):
        if player_name == "player1": markStr = "P1"
        if player_name == "player2": markStr = "P2"
        for position in selected_caps:
            self.cap_list[position-1] = markStr

        self.output_cap_list(player_name)

    def select_bot_caps(self, selected_caps):
        cap_count = 12
        for i in range(0, len(selected_caps)):
            if selected_caps[i] > cap_count / 2:
                selected_caps[i] = selected_caps[i] - cap_count / 2 - 1
            else:
                selected_caps[i] = selected_caps[i] + cap_count / 2 + 1

        return selected_caps

    def end_game(self):
        for cap in self.cap_list:
            if cap != "X": return False
        return True

def main():
    game = BottleCapGame(["O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"])
    game.output_cap_list("start")
    game.cap_list[5] = "P1"
    game.output_cap_list("player1")
    while(game.end_game() == False):
        selected_caps = []
        while(game.validate_for_input(selected_caps) == False):
            try:
                selected_caps = list(input("Please select one or two caps(ex-5, or 5,6): "))
            except:
                print("Try to input again.")

        game.remove_selected_caps("player2", selected_caps)

        selected_caps = game.select_bot_caps(selected_caps)
        game.remove_selected_caps("player1", selected_caps)

if __name__ == '__main__':
    main()
