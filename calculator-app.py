import math
import tkinter as tk

def evaluate(event):
   try:
       result = eval(entry.get())
       label['text'] = f'Result: {result}'
   except Exception as e:
       label['text'] = str(e)

def add_button(parent, text, command):
   button = tk.Button(parent, text=text, command=command)
   button.pack(side='left', fill='both', expand=True)
   return button

window = tk.Tk()
window.title('Calculator')

entry = tk.Entry(window, width=30)
entry.bind('<Return>', evaluate)
entry.pack(fill='x')

label = tk.Label(window, text='')
label.pack()

buttons = [
   '7', '8', '9', '/', 'sqrt', '^', '(', ')',
   '4', '5', '6', '*', 'log', 'sin', 'cos', 'tan',
   '1', '2', '3', '-', 'e', 'ln', 'sinh', 'cosh', 'tanh',
   '0', '.', '=', '+', '10^', 'abs', 'round', 'floor', 'ceil',
]

for i, text in enumerate(buttons):
   row = i // 4
   col = i % 4
   add_button(window, text, lambda: entry.insert('end', text))
   if col < 3:
       window.grid_columnconfigure(col, weight=1)
   if row < 3:
       window.grid_rowconfigure(row, weight=1)

window.mainloop()
