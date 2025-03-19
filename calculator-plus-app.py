import tkinter as tk
from tkinter import simpledialog, messagebox
import math
import os
from datetime import datetime

class SafeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Safe Calculator")
        master.geometry('800x800')

        # Track last result and input state
        self.last_result = None
        self.result_displayed = False

        # Define a specific notes directory
        self.notes_dir = os.path.join(os.path.expanduser('~'), 'CalculatorNotes')
        os.makedirs(self.notes_dir, exist_ok=True)
        
        # Create a specific notes file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.notes_file = os.path.join(self.notes_dir, f'calculations_{timestamp}.txt')

        # Display field with Enter key binding
        self.display = tk.Entry(master, width=30, font=('Helvetica', 24), justify='right')
        self.display.grid(row=1, column=0, columnspan=4, ipady=20, ipadx=20)
        
        # Bind Enter key to calculate method
        self.display.bind('<Return>', self.calculate_from_event)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '(', ')', '=', 
            'sin', 'cos', 'tan',
            'exp', 'log', 'sqrt',
            '^', '%', 'π'
        ]

        # Create buttons dynamically
        row, col = 2, 0
        for text in buttons:
            button = tk.Button(master, text=text, font=('Helvetica', 18), width=5,
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, ipady=10, ipadx=10, sticky='nsew')
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid weights for responsive layout
        for i in range(row):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        # Calculation history
        self.history_window = None
        self.calculation_history = []

        # Add buttons for notes and history
        notes_button = tk.Button(master, text="Open Notes", font=('Helvetica', 18), 
                                 command=self.open_notes_directory)
        notes_button.grid(row=row+1, column=0, columnspan=2, ipady=10, ipadx=10, sticky='nsew')

        history_button = tk.Button(master, text="History", font=('Helvetica', 18), 
                                   command=self.show_history)
        history_button.grid(row=row+1, column=2, columnspan=2, ipady=10, ipadx=10, sticky='nsew')

    def button_click(self, key):
        # Reset display if a result is currently shown and a new input comes
        current = self.display.get()
        
        # Check if the current display is a result and a new input is coming
        if self.result_displayed:
            # Clear for new input, except for operations that can build on previous result
            if key in '0123456789.()+-*/^%':
                self.display.delete(0, tk.END)
                self.result_displayed = False

        # Handle specific buttons
        if key == 'C':
            self.display.delete(0, tk.END)
            self.result_displayed = False
        elif key == '=':
            self.calculate()
        elif key == 'π':
            self.display.insert(tk.END, str(math.pi))
        else:
            self.display.insert(tk.END, key)

    def calculate_from_event(self, event=None):
        self.calculate()

    def calculate(self):
        try:
            # Get the expression
            expr = self.display.get()
            
            # Replace math functions
            expr = expr.replace('^', '**')
            expr = expr.replace('sqrt', 'math.sqrt')
            expr = expr.replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            expr = expr.replace('tan', 'math.tan')
            expr = expr.replace('exp', 'math.exp')
            expr = expr.replace('log', 'math.log')
            expr = expr.replace('π', str(math.pi))

            # Safely evaluate the expression
            result = eval(expr, {"__builtins__": None}, 
                          {"math": math, "abs": abs})
            
            # Format result
            result_str = f"{result:.4f}" if isinstance(result, float) else str(result)
            
            # Ask for note
            note = simpledialog.askstring("Note", "Enter a note for this calculation:", parent=self.master)
            
            # Save to file and history
            if note:
                full_entry = f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" \
                             f"Expression: {expr}\n" \
                             f"Result: {result_str}\n" \
                             f"Note: {note}\n" \
                             f"{'='*40}\n"
                
                with open(self.notes_file, 'a') as f:
                    f.write(full_entry)
                
                # Add to in-memory history
                self.calculation_history.append(full_entry)

            # Update display
            self.display.delete(0, tk.END)
            self.display.insert(0, result_str)
            
            # Mark that a result is displayed
            self.result_displayed = True

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.result_displayed = False

    def open_notes_directory(self):
        """Open the notes directory in the file explorer"""
        try:
            if os.name == 'nt':  # Windows
                os.startfile(self.notes_dir)
            elif os.name == 'posix':  # macOS and Linux
                import subprocess
                subprocess.Popen(['open', self.notes_dir])
            else:
                messagebox.showinfo("Open Notes", f"Notes are saved in: {self.notes_dir}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open directory: {e}")

    def show_history(self):
        """Show history from the current session"""
        if self.history_window is None or not tk.Toplevel.winfo_exists(self.history_window):
            self.history_window = tk.Toplevel(self.master)
            self.history_window.title("Calculation History")
            self.history_window.geometry('600x400')

            # Create a text widget to display history
            history_text = tk.Text(self.history_window, wrap=tk.WORD)
            history_text.pack(expand=True, fill=tk.BOTH)

            # Insert history entries
            for entry in self.calculation_history:
                history_text.insert(tk.END, entry + "\n")

            # Add buttons
            button_frame = tk.Frame(self.history_window)
            button_frame.pack(fill=tk.X)

            clear_button = tk.Button(button_frame, text="Clear Session History", 
                                     command=self.clear_history)
            clear_button.pack(side=tk.LEFT)

            open_file_button = tk.Button(button_frame, text="Open Notes File", 
                                         command=self.open_notes_file)
            open_file_button.pack(side=tk.LEFT)

    def open_notes_file(self):
        """Open the current notes file"""
        try:
            if os.name == 'nt':  # Windows
                os.startfile(self.notes_file)
            elif os.name == 'posix':  # macOS and Linux
                import subprocess
                subprocess.Popen(['open', self.notes_file])
            else:
                messagebox.showinfo("Open Notes", f"Notes file: {self.notes_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

    def clear_history(self):
        """Clear in-memory and session-based history"""
        self.calculation_history.clear()
        
        # Clear history window text
        if self.history_window:
            for widget in self.history_window.winfo_children():
                if isinstance(widget, tk.Text):
                    widget.delete('1.0', tk.END)

def main():
    root = tk.Tk()
    root.title("Advanced Calculator")
    calculator = SafeCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
