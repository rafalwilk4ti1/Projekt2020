def draw_board(lista):
    print("\t\tTic-Tac-Toe")
    print("\t-------------------")
    print("\t || "+str(lista[0])+" || "+str(lista[1])+" || "+str(lista[2]) + " ||")
    print("\t-------------------")
    print("\t || "+str(lista[3])+" || "+str(lista[4])+" || "+str(lista[5]) + " ||")
    print("\t-------------------")
    print("\t || "+str(lista[6])+" || "+str(lista[7])+" || "+str(lista[8]) + " ||")
    print("\t-------------------")

def get_player_input(place, lista):
    move = True
    while move:
        place = int(input("\nWhere would you like place your piece? (0-8)"))
        if place in range(0,10):
            if lista[place] =="_":
                return place
            else:
                print("\nThe spot has already been chosen")
                move = True
        elif place >= 9:
            print("\nI regret to inform you that your move is not a spot on the board.")
        else:
            print("\nI regret to inform you that your move is not a spot on the board.")


def place_char_on_board(place,player_desired_move,lista):
    lista[place] = player_desired_move

def is_winner(lista, place):
    if  lista[0] == place and lista[1] == place and lista[2] == place:
        print("\nWinner is player "+place+". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True

    elif lista[2] == place and lista[4] == place and lista[5] == place:
        print("Winner is player " + place + ". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True
    elif lista[6] == place and lista[7] == place and lista[8] == place:
        print("Winner is player " + place + ". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True
    elif lista[0] == place and lista[4] == place and lista[8] == place:
        print("Winner is player" + place + ". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True
    elif lista[2] == place  and lista[4] == place and lista[6] == place:
        print("Winner is player" + place + ". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True
    elif lista[0] == place and lista[3] == place and lista[6]== place:
        print("Winner is player " + place + ". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True
    elif lista[1] == place and lista[4] == place and lista[7] == place:
        print("Winner is player "+place+". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True
    elif lista[2] == place and lista[5] == place and lista[8] == place :
        print("Winner is player " + place + ". Congratulations!")
        print("\nThanks for game, see you next time!")
        return True

    else:
        return False

player_1 = "X"
player_2 = "O"

c_list = ["_","_","_","_","_","_","_","_","_"]
n_list = ["0","1","2","3","4","5","6","7","8"]

draw_board(n_list)

draw_board(c_list)

active = True
while active:
    #1 player move
    first_move = get_player_input(player_1,c_list)
    place_char_on_board(first_move,player_1,c_list )
    draw_board(n_list)
    draw_board(c_list)
    result1 = is_winner(c_list,player_1)
    if result1:
        print("Player 1 is winner")
        break
    elif "_" not in c_list:
        print("The game was a tie")
        break
    #2 player move
    second_move = get_player_input(player_2,c_list)
    place_char_on_board(second_move,player_2,c_list)
    draw_board(n_list)
    draw_board(c_list)
    result2 = is_winner(c_list,player_2)
    if result2:
        print("Player 2 is winner")
        break



    # if is_winner(c_list,player_1):
    #     print("Player 1 is winner!")
    #     active = False
    # elif is_winner(c_list,player_2):
    #     print("Player 2 is winner")
    #     active = False
    # else:
    #     active = True









