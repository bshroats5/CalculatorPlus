import tkinter as tk

class Calculator:
  def __init__(self, master):
      self.master = master
      master.title("Calculator")
      master.geometry('400x500')

      self.display = tk.Entry(master, width=30, font=('Helvetica', 24))
      self.display.grid(row=0, column=0, columnspan=4)

      buttons = [
          '7', '8', '9', '/',
          '4', '5', '6', '*',
          '1', '2', '3', '-',
          '0', '.', '=', '+',
          'C'
      ]

      for i, text in enumerate(buttons):
          row = i // 4
          col = i % 4
          button = tk.Button(master, text=text, font=('Helvetica', 18), width=5)
          button.grid(row=row+1, column=col)

  def press(self, char):
      if char == '=':
          try:
              result = eval(self.display.get())
              self.display.delete(0, tk.END)
              self.display.insert(0, str(result))
          except Exception as e:
              self.display.delete(0, tk.END)
              self.display.insert(0, str(e))
      elif char == 'C':
          self.display.delete(0, tk.END)
      else:
          self.display.insert(tk.END, char)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
