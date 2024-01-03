import tkinter as tk

class Calculator:
   def __init__(self, master):
       self.master = master
       master.title("Calculator")
       master.geometry('400x500')

       self.display = tk.Entry(master, width=30, font=('Helvetica', 24))
       self.display.grid(row=0, column=0, columnspan=4, ipady=20, ipadx=20)
       self.display.bind('<Return>', self.evaluate)

       buttons = [
           '7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', '.', '=', '+',
           'C', '0'
       ]

       for i, text in enumerate(buttons):
           row = i // 4
           col = i % 4
           button = tk.Button(master, text=text, font=('Helvetica', 18), width=5)
           button.grid(row=row+1, column=col, ipady=20, ipadx=20)
           button.config(command=lambda t=text: self.press(t))

   def press(self, char):
       self.display.insert(tk.END, char)

   def evaluate(self, event):
       try:
           result = eval(self.display.get())
           self.display.delete(0, tk.END)
           self.display.insert(0, str(result))
       except Exception as e:
           self.display.delete(0, tk.END)
           self.display.insert(0, str(e))

   def clear(self):
       self.display.delete(0, tk.END)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
