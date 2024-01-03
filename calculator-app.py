import tkinter as tk

class Calculator:
   def __init__(self, master):
       self.master = master
       master.title("Calculator")

       self.display = tk.Entry(master, width=30)
       self.display.grid(row=0, column=0, columnspan=4)

       buttons = [
           '7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', '.', '=', '+'
       ]

       for i, text in enumerate(buttons):
           row = i // 4
           col = i % 4
           button = tk.Button(master, text=text, command=lambda t=text: self.press(t))
           button.grid(row=row+1, column=col)

       self.clear_button = tk.Button(master, text='C', command=self.clear)
       self.clear_button.grid(row=5, column=0)

   def press(self, char):
       if char == '=':
           try:
               result = eval(self.display.get())
               self.display.delete(0, tk.END)
               self.display.insert(0, str(result))
           except Exception as e:
               self.display.delete(0, tk.END)
               self.display.insert(0, str(e))
       else:
           self.display.insert(tk.END, char)

   def clear(self):
       self.display.delete(0, tk.END)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
