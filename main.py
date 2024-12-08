import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe - Jackson Downing")
root.geometry("500x600")

gameGrid = tk.Frame(root)
for i in range(3):
    gameGrid.grid_columnconfigure(i, weight=1, uniform="equal")
    gameGrid.grid_rowconfigure(i, weight=1, uniform="equal")
gameGrid.pack(padx=20, pady=20, expand=True, fill="both")

gameBtns = []
for r in range(3):
    for c in range(3):
        btn = tk.Button(gameGrid, text="Wow")
        btn.grid(row=r, column=c, sticky="news")
        gameBtns.append(btn)



root.mainloop()