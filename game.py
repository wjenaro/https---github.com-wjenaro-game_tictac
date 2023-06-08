def welcome_player():
    print("welcome to this exciting game")
    play=input(" do you want to play the game, input 'Y' to play and 'N' to abort ")
    if play=='Y':
        print('Start')
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        print_board(board)
        #has player choosen 
        player_tool=player_input()
        if player_tool== 'O' or place_marker=='X':
            #continue with playing
            #call place_marker(board, marker, position)
            

            def place_marker(board, marker, position):
                board[position] = marker
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            player_marker = "X"
            desired_position = 5
            place_marker(board, player_marker, desired_position)
            print(board)


            
            print(f"Good, you will be playing using {player_tool}")
        else:
            print(f"Good, you will be playing using {player_tool}")

        
    else:
        print("Bye")



def print_board(board):
    print("-------------")
    print("|", board[7], "|", board[8], "|", board[9], "|")
    print("-------------")
    print("|", board[4], "|", board[5], "|", board[6], "|")
    print("-------------")
    print("|", board[1], "|", board[2], "|", board[3], "|")
    print("-------------")

#player input function:
def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Choose your marker (X or O): ").upper()
        if marker != "X" and marker != "O":
            print("Invalid input. Please choose either 'X' or 'O'.")
    return marker
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def place_marker(board, marker, position):
    board[position] = marker



welcome_player()
