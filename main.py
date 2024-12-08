import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe - Jackson Downing")
root.geometry("500x600")

gameGrid = tk.Frame(root)
gameGrid.grid_columnconfigure(0, weight=1)
gameGrid.grid_columnconfigure(1, weight=1)
gameGrid.grid_columnconfigure(2, weight=1)
gameGrid.pack(padx=10, pady=10)

root.mainloop()