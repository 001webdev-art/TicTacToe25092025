#25.09.2025 - AIPM NeueFische - TicTacToe Game - Heinrich Gronauer

# "random" is to choose random numbers, without it, it will throw an error. This is a Python built-in library
    # „random“ dient zur Auswahl von Zufallszahlen. Ohne diese Funktion wird ein Fehler ausgegeben. Es handelt sich hierbei um eine in Python integrierte Bibliothek.
import random 
import tictac_resources as r #importing the file with colors and logo
import python_terminal_colors_def as c #importing the file with colors and logo
from colorama import init, Fore, Style

#import os
#import time

init(autoreset=True)  # grant colors on Windows ( funcion from colorama)

tictac_board = [" "] * 9; 
#creates a variable with a list of 9 empty spaces, #but also could be done with [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    #Erstellt eine Variable mit einer Liste von 9 Leerzeichen, #könnte aber auch mit [„ “, „ “, „ “, „ “, „ “, „ “, „ “, „ “, „ “]

playerName1 = "";
playerName2 = "";


def show_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
    # could be done also with print( board[6] + " | " + board[7] + " | " + board[8] ")
    # but with this "f" function, its easier to format the output!!! 
    
        # könnte auch mit print( board[6] + „ | “ + board[7] + „ | “ + board[8] ") gemacht werden.
        # Aber mit dieser „f”-Funktion ist es einfacher, die Ausgabe zu formatieren!!!     

#testing, it must show something in the console    
#show_board(tictac_board);

def check_winner_combinations(board, symbol):
    combi = [
        [0,4,8], [2,4,6], #check the diagonals,
        [0,1,2], [3,4,5], [6,7,8],  # Lines 
        [0,3,6], [1,4,7], [2,5,8]  # Columns                        
    ]
    for c in combi:
        if board[c[0]] == board[c[1]] == board[c[2]] == symbol:
            return True
    return False

def draw(board):
    return " " not in board

def user(board, playerName, symbol="X" ):
    while True:
        try:
            pos = int(input(f"{playerName}, What position? (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("\nWrong one! Pickup something between 1 e 9.\n")                
            elif board[pos] != " ":                
                print("\nOccupied position!, do you need Glasses? Choose another one!\n")
            else:
                #board[pos] = "X"
                board[pos] = symbol
                break
        except ValueError:
            print()
            print("Not a Valid Number!")
            print()
            
            #this print() gives a new line, to make it more readable, is the if you put a  \n inside the string
            

def robot(board):
    remainingPlaces = [i for i in range(9) if board[i] == " "]
    """this appends the array var remainingPlaces with the remaining places
        **** dies fügt der Array-Variable remainingPlaces die verbleibenden Plätze hinzu
     
     lightining fast to code! something like this in Pascal for example would be something like this:
      for i:=0 to length( board ) -1 do
        begin 
          if board[i] = " " remainingPlaces.add( board[i] );
        end;, 
        or even more then 3 lines of code!!!!
    """
    pos = random.choice(remainingPlaces)
    board[pos] = "O"
    print(f"Where mrRobot placed {pos+1}")  
    
clear = lambda: print("\n" * 100) #just a simulation of clear screen,  this "\n" means new line, so its *100, it helsp simulating a clear screen
           
clear()       
def letsPlay(): 
    r.show_logo(random.choice([0,1,2])) #shows a random logo from the 3 available
    playerName1 = input("Whats is your Name?: ")
    playerName2 = input("Who are playing against you?: ( or type You/Computer or leave it blank to play with me! ): ")

    is_against_mrRobot = False
    is_against_mrRobot = playerName2.lower() in ["computer", "you", "", " "]

    show_board(tictac_board)

    while True:
        # First player
        user(tictac_board, playerName1)
        show_board(tictac_board)
        if check_winner_combinations(tictac_board, "X"):
            print(f"{ c.fg.RED} {playerName1} Won!")            
            break
        if draw(tictac_board):
            print(" Draw!")            
            break

        # player 2 (or mrRobot ;) )
        if is_against_mrRobot:
            robot(tictac_board)
        else:
            user(tictac_board, playerName2, "O")
        show_board(tictac_board)

        if check_winner_combinations(tictac_board, "O"):
            theWinnerIs = "Computador" if is_against_mrRobot else playerName1
            print(f"{ c.fg.RED} {theWinnerIs} Won!")            
            break
        if draw(tictac_board):
            print(f"{ c.fg.RED} Draw!")            
            break
    
    print(f"{ c.bcolors.RESET_ALL} ")    

if __name__ == "__main__":
    letsPlay()