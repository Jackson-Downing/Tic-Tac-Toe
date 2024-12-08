import tkinter as tk

currentPlayer = "X"
gameBtns = []

def checkWin():
    global gameBtns
    for i in range(0, 9, 3):
        if gameBtns[i].cget("text") == gameBtns[i+1].cget("text") == gameBtns[i+2].cget("text") and gameBtns[i].cget("text") != "":
            return True # Horizontal win
    for i in range(3):
        if gameBtns[i].cget("text") == gameBtns[i+3].cget("text") == gameBtns[i+6].cget("text") and gameBtns[i].cget("text") != "":
            return True # Vertical win
    if gameBtns[0].cget("text") == gameBtns[4].cget("text") == gameBtns[8].cget("text") and gameBtns[0] != "":
        return True # Diagonal win 1
    elif gameBtns[2].cget("text") == gameBtns[4].cget("text") == gameBtns[6].cget("text") and gameBtns[0] != "":
        return True # Diagonal win 2
    return False # No win this round

# Functions must be at the top, otherwise the program gets hissy when trying to reference them
def preGame():
    gameGrid.pack_forget()
    startBtn.pack(root)

def inGame(player="X"):
    turnIndicator.config(text=f"{player}'s turn...")

def postGame():
    pass

def btnPress(player):
    if False: # Check if won
        pass
    elif player == "X":
        return "O"
    else:
        return "X"

def startGame():
    startBtn.pack_forget()
    turnIndicator.pack()
    gameGrid.pack(padx=20, pady=20, expand=True, fill="both")
    inGame()

root = tk.Tk()
root.title("Tic Tac Toe - Jackson Downing")
root.geometry("500x550")

# Grid to hold all the game btns, autofitting to the screen with equal size
gameGrid = tk.Frame(root)
for i in range(3):
    gameGrid.grid_columnconfigure(i, weight=1, uniform="equal")
    gameGrid.grid_rowconfigure(i, weight=1, uniform="equal")


# Loop to create each game btn and store it in an array
for r in range(3):
    for c in range(3):
        btn = tk.Button(gameGrid, text="")
        btn.grid(row=r, column=c, sticky="news")
        gameBtns.append(btn)

startBtn = tk.Button(root, text="Start game", font=("Comic Sans MS", 20), width=20, height=3, command=startGame)
startBtn.pack(pady=50, padx=50)

turnIndicator = tk.Label(root, font=("Ariel", 12))

root.mainloop()