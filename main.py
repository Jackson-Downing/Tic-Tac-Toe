import tkinter as tk

# Global variables
currentPlayer = "X"
gameBtns = []

root = tk.Tk()
root.title("Tic Tac Toe - Jackson Downing")
root.geometry("500x500")

def checkWin():
    global gameBtns
    for i in range(0, 9, 3):
        if gameBtns[i].cget("text") == gameBtns[i+1].cget("text") == gameBtns[i+2].cget("text") and gameBtns[i].cget("text") != "":
            return True # Horizontal win
    for i in range(3):
        if gameBtns[i].cget("text") == gameBtns[i+3].cget("text") == gameBtns[i+6].cget("text") and gameBtns[i].cget("text") != "":
            return True # Vertical win
    if gameBtns[0].cget("text") == gameBtns[4].cget("text") == gameBtns[8].cget("text") and gameBtns[0].cget("text") != "":
        return True # Diagonal win 1
    elif gameBtns[2].cget("text") == gameBtns[4].cget("text") == gameBtns[6].cget("text") and gameBtns[2].cget("text") != "":
        return True # Diagonal win
    return False # No win this round

def checkTie():
    global gameBtns
    isTie = True
    for btn in gameBtns:
        if btn.cget("text") == "":
            isTie = False
    return isTie

# Functions must be at the top, otherwise the program gets hissy when trying to reference them
def preGame():
    textIndicator.pack_forget()
    gameGrid.pack_forget()
    menuBtn.pack_forget()
    startBtn.pack(side="bottom", padx=10, pady=10)

def postGame():
    global gameBtns
    for btn in gameBtns:
        btn.config(state="disabled")
    menuBtn.pack(padx=10, pady=10)

def btnPress(b):
    global currentPlayer
    if b.cget("text") == "":
        b.config(text=currentPlayer)
    else:
        return
    if checkWin():
        textIndicator.config(text=f"{currentPlayer} wins!")
        postGame()
    elif checkTie():
        textIndicator.config(text=f"Tie!")
        postGame()
    else:
        currentPlayer = "O" if currentPlayer == "X" else "X" # Change player
        textIndicator.config(text=f"{currentPlayer}'s turn...")

def startGame():
    global currentPlayer
    global gameBtns
    currentPlayer = "X"
    startBtn.pack_forget()
    textIndicator.pack(padx=10, pady=10)
    for btn in gameBtns:
        btn.config(text="", state="normal")
    gameGrid.pack(padx=20, pady=10, expand=True, fill="both")
    textIndicator.config(text=f"{currentPlayer}'s turn...")

# Grid to hold all the game btns, autofitting to the screen with equal size
gameGrid = tk.Frame(root)
for i in range(3):
    gameGrid.grid_columnconfigure(i, weight=1, uniform="equal")
    gameGrid.grid_rowconfigure(i, weight=1, uniform="equal")


# Loop to create each game btn and store it in an array
for r in range(3):
    for c in range(3):
        btn = tk.Button(gameGrid, text="") 
        btn.config(command=lambda b = btn: btnPress(b))
        btn.grid(row=r, column=c, sticky="news")
        gameBtns.append(btn)

startBtn = tk.Button(root, text="Start game", font=("Ariel", 12), width=20, height=1, command=startGame)
textIndicator = tk.Label(root, font=("Ariel", 12))
menuBtn = tk.Button(root, text="Menu", width=20, height=1, font=("Ariel", 12), command=preGame)
preGame()
root.mainloop()