import tkinter as tk
from tkinter import simpledialog, Text, Scrollbar, END
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry('400x500')

        # Display field
        self.display = tk.Entry(master, width=30, font=('Helvetica', 24))
        self.display.grid(row=1, column=0, columnspan=4, ipady=20, ipadx=20)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'CE', '+',
            '(', ')', '=', '0',
            'sin', 'cos', 'tan',
            'exp', 'log', 'sqr',
            '^', '%', 'π'
        ]

        for i, text in enumerate(buttons):
            row = i // 4 + 2
            col = i % 4
            button = tk.Button(master, text=text, font=('Helvetica', 18), width=5)
            button.grid(row=row, column=col, ipady=20, ipadx=20)
            if text == 'CE':
                button.config(command=self.clear_entry)
            elif text == '=':
                button.config(command=self.evaluate)
            elif text in ['sin', 'cos', 'tan', 'exp', 'log', 'sqr']:
                button.config(command=lambda t=text: self.press(t))
            else:
                button.config(command=lambda t=text: self.press(t))

        self.notes = []

    def press(self, char):
        self.display.insert(tk.END, char)

    def clear_entry(self):
        self.display.delete(0, tk.END)

    def evaluate(self):
        try:
            expr = self.display.get()
            result = eval(expr)
            note = simpledialog.askstring("Note", "Enter a note for this calculation:", parent=self.master)
            if note is not None:
                self.notes.append((str(result), note))
                with open('notes.txt', 'a') as f:
                    f.write(f"{str(result)} - {note}\n")
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, str(e))

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
