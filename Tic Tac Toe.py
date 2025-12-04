import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")

current_player = "X"
buttons = []

def check_winner():

    combos = [
        [0,1,2], [3,4,5], [6,7,8],   
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]             
    ]
    for combo in combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            messagebox.showinfo("Game Over", f"Player {buttons[combo[0]]['text']} wins!")
            window.quit()
 
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a Draw!")
        window.quit()

def on_click(i):
    global current_player
    if buttons[i]["text"] == "":
        buttons[i]["text"] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"


for i in range(9):
    btn = tk.Button(window, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

window.mainloop()