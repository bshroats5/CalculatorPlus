import tkinter as tk
from tkinter import Text, Scrollbar

class Calculator:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        master.title("Calculator")
        master.geometry('400x500')

        self.note_frame = tk.Frame(master)
        self.note_frame.grid(row=0, column=0, columnspan=4, sticky='nswe')
        self.note_text = Text(self.note_frame, height=10, width=30, wrap='word')
        self.scrollbar = Scrollbar(self.note_frame, orient="vertical", command=self.note_text.yview)
        self.note_text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.note_text.pack(side='left', fill='both', expand=True)

        self.display = tk.Entry(master, width=30, font=('Helvetica', 24))
        self.display.grid(row=1, column=0, columnspan=4, ipady=20, ipadx=20)

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

    def clear_entry(self) -> None:
        pass

    def evaluate(self) -> None:
        pass

    def press(self, text: str) -> None:
        pass