import tkinter as tk

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
gameBtns = []
for r in range(3):
    for c in range(3):
        btn = tk.Button(gameGrid)
        btn.grid(row=r, column=c, sticky="news")
        gameBtns.append(btn)

startBtn = tk.Button(root, text="Start game", font=("Comic Sans MS", 20), width=20, height=3, command=startGame)
startBtn.pack(pady=50, padx=50)

turnIndicator = tk.Label(root, font=("Ariel", 12))

root.mainloop()