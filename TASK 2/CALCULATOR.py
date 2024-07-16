import tkinter as tk

def button_click(number):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_operator(operator):
    current = entry.get()
    if current and current[-1] not in '+-*/':
        entry.insert(tk.END, operator)
    elif current and current[-1] in '+-*/':
        entry.delete(len(current) - 1, tk.END)
        entry.insert(tk.END, operator)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main application window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(background="#3498db")  # Set background color to blue

# Entry widget for displaying calculation result
entry = tk.Entry(root, text='', bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=5, pady=40, padx=25)
entry.config(font=("Helvetica", 30, 'bold'))

# Calculator buttons
buttons = [
    ('9', 1, 0), ('8', 1, 1), ('7', 1, 2), ('+', 1, 3),
    ('6', 2, 0), ('5', 2, 1), ('4', 2, 2), ('-', 2, 3),
    ('3', 3, 0), ('2', 3, 1), ('1', 3, 2), ('*', 3, 3),
    ('AC', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, column) in buttons:
    btn = tk.Button(root, text=text, bg='#ecf0f1', fg='#2c3e50', width=5, height=2)  # Set button colors
    btn.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
    btn.config(font=('Helvetica', 14))

    if text.isdigit() or text == '0':
        btn['command'] = lambda num=text: button_click(int(num))
    elif text in '+-*/':
        btn['command'] = lambda op=text: button_operator(op)
    elif text == 'AC':
        btn['command'] = button_clear
    elif text == '=':
        btn['command'] = button_equal

# Calculate the center position dynamically
window_width = 500
window_height = 460
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

# Set geometry and position the window
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

root.mainloop()
