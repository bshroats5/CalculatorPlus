import tkinter as tk
from tkinter import simpledialog, Text, Scrollbar, END
import math

class Calculator:
 def __init__(self, master):
    self.master = master
    master.title("Calculator")
    master.geometry('400x500')

    # Add a scrollable text field for displaying notes
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

 def press(self, char):
    if char in ['sin', 'cos', 'tan', 'exp', 'log', 'sqr']:
        self.display.insert(tk.END, f"math.{char}(")
    elif char == 'π':
        self.display.insert(tk.END, str(math.pi))
    else:
        self.display.insert(tk.END, char)

 def clear_entry(self):
    self.display.delete(len(self.display.get())-1, tk.END)

def evaluate(self):
   try:
       expr = self.display.get().replace(' ', '')
       if '(' in expr and ')' not in expr or '(' not in expr and ')' in expr:
           raise SyntaxError("Unbalanced parentheses")
       result = eval(expr)
       note = simpledialog.askstring("Note", "Enter a note for this calculation:", parent=self.master)
       if note is not None:
           self.notes.append((str(result), note))
           with open('notes.txt', 'w') as f:
               for r, n in self.notes:
                  f.write(f"{r} - {n}\n")
           self.display.delete(0, tk.END)
           self.display.insert(0, str(result))
           self.note_text.insert(END, f"\n{str(result)} - {note}")
           self.note_text.see(END)
   except SyntaxError as e:
       self.display.delete(0, tk.END)
       self.display.insert(0, str(e))
   except Exception as e:
       self.display.delete(0, tk.END)
       self.display.insert(0, str(e))


 def clear(self):
    self.display.delete(0, tk.END)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()