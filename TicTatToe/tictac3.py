#25.09.2025 - AIPM NeueFische - TicTacToe Game - Heinrich Gronauer

# "random" is to choose random numbers, without it, it will throw an error. This is a Python built-in library
    # „random“ dient zur Auswahl von Zufallszahlen. Ohne diese Funktion wird ein Fehler ausgegeben. Es handelt sich hierbei um eine in Python integrierte Bibliothek.
import random 
import os
import time
import tictac_resources as r #importing the file with colors and logo
import python_terminal_colors_def as c #importing the file with colors and logo
from colorama import init, Fore, Style
import tictac_ai_random
import tictac_ai_heuristic
import tictac_ai_minimax

#import os
#import time

init(autoreset=True)  # grant colors on Windows ( funcion from colorama)
ai = 1
ai_options = { "1": tictac_ai_random, "2": tictac_ai_heuristic, "3": tictac_ai_minimax }

os_clear = lambda: os.system("cls" if os.name == "nt" else "clear") #this one is to clear the screen, works on Windows and Linux/Mac
clear = lambda: print("\n" * 100) #just a simulation of cleeear screen,  this "\n" means new line, so its *100, it helsp simulating a clear screen


tictac_board = [" "] * 9; 
#creates a variable with a list of 9 empty spaces, #but also could be done with [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    #Erstellt eine Variable mit einer Liste von 9 Leerzeichen, #könnte aber auch mit [„ “, „ “, „ “, „ “, „ “, „ “, „ “, „ “, „ “]

playerName1 = "";
playerName2 = "";


def show_board(board, highlight=None):
    
    """Print the board, with optional highlight for winner line"""
    
    def symbol(i):
        if highlight and i in highlight:
            return Fore.RED + board[i] + Style.RESET_ALL
        return board[i]

    print()
    print(f" {symbol(0)} | {symbol(1)} | {symbol(2)} ")
    print("---+---+---")
    print(f" {symbol(3)} | {symbol(4)} | {symbol(5)} ")
    print("---+---+---")
    print(f" {symbol(6)} | {symbol(7)} | {symbol(8)} ")
    print()  

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
            return c
    return None

def blink_winner_line(board, winner, combo):
    """Make the winning line blink"""
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Fore.GREEN} 🎉🎉🎉 Yahooooo! -->    {winner}   <-- WON! 🎉🎉🎉 {Style.RESET_ALL}")
    time.sleep(2)
    
    for _ in range(6): 
        #_ or "banana" doesnt matter, its just a counter great to learn!
        #_ oder „Hauptbahnhof“ spielt keine Rolle, es ist nur ein Zähler, der sich gut lernen lässt!
        os.system("cls" if os.name == "nt" else "clear")
        show_board(board)  # normal
        time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")
        show_board(board, highlight=combo)  # highlighted
        time.sleep(0.3)
    
    print(f"{Fore.GREEN} 🎉🎉🎉 Yahooooo! -->    {winner}   <-- WON! 🎉🎉🎉 {Style.RESET_ALL}")

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
               
#clear()       
os_clear()
def yahooooo_letsPlay(): 
    r.show_logo(random.choice([0,1,2])) #shows a random logo from the 3 available
    #dont forget r is a shortcut for tictac_resources, declared in the header of the file -> import tictac_resources as r
    #vergiss nicht, dass r eine Abkürzung für tictac_resources ist, deklariert im Header der Datei -> importiere tictac_resources als r
    
    playerName1 = input("Whats is your Name?: ")
    playerName2 = input("\nWho are playing against you?: ( or type You/Computer or leave it blank to play with me! ): ")            

    is_against_mrRobot = False
    is_against_mrRobot = playerName2.lower() in ["computer", "you", "", " "]
    
    if is_against_mrRobot:        
        print("\nAhh! So you want a real challenge, do you? I will let you choose the Dificulty Level: " )
        print("\n    (1) Drunked AI - Good for Ducks🦤🦤, ah sorry!, i mean, BEGINNERS" )
        print("\n    (2) AI Brain  - for Heuristics ( Level is Medium, if you dare... )" )
        print("\n    (3) AI Brain  - for Minimax Strategy, go ahead, make my day!\n\n\n" )
    
        ai = input("Choose the Level ( 1, 2 or 3 ) [default is 1]: ")
        
        if ai in ai_options:
            chosen_level = ai_options[ai]
            print("Chosen:", chosen_level.__name__)
        else:
            print("Invalid option! I am assuming you are a Duck🦤🦤, so I will choose the Drunked AI for you!") 
            ai = "1"       
            
    show_board(tictac_board)

    while True:
        # Player 1
        user(tictac_board, playerName1)
        show_board(tictac_board)
        combo = check_winner_combinations(tictac_board, "X")
        if combo:
            blink_winner_line(tictac_board, playerName1, combo)
            break
        if draw(tictac_board):
            print("Draw!")
            break

        # Player 2 (or robot)
        if is_against_mrRobot:
            pos = ai_options[ai].get_move(tictac_board)
            if pos is not None:
                tictac_board[pos] = "O"
                print(f"mrRobot placed at {pos+1}")
        else:
            user(tictac_board, playerName2, "O")
        show_board(tictac_board)

        combo = check_winner_combinations(tictac_board, "O")
        if combo:
            winner = "mrRobot" if is_against_mrRobot else playerName2
            blink_winner_line(tictac_board, winner, combo)
            if is_against_mrRobot:
                print(f"{ c.bcolors.WARNING} Quac-Quac-Quac you Duck🦤 🦤 🦤 🦤! You lost against mrRobot! Better luck next time! { c.bcolors.RESET_ALL}")
            break
        if draw(tictac_board):
            print("Draw!")
            break
    
    print(f"{ c.bcolors.RESET_ALL} ")    

if __name__ == "__main__":
    yahooooo_letsPlay()