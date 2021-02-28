import tkinter
from tkinter import messagebox

from SavingGameFiles import SaveGame


def quit_and_save():
    root = tkinter.Tk()
    root.overrideredirect(1)
    root.withdraw()
    res = messagebox.askquestion('', 'Quit and save the game?')
    if res == 'yes':
        messagebox.showinfo('Response', 'Game saved')
        SaveGame.save_game()
    elif res == 'no':
        messagebox.showinfo('Response', 'Game not saved')
    else:
        messagebox.showwarning('error', 'Game not saved')
    root.destroy()
