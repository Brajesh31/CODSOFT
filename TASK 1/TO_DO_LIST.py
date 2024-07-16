import tkinter as tk
from tkinter import messagebox, simpledialog


# Function to add a task to the listbox
def add_task():
    task = task_entry.get().strip()  # Strip leading/trailing whitespace
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task")


# Function to delete a selected task from the listbox
def delete_task():
    task_indices = task_listbox.curselection()
    if task_indices:
        task_listbox.delete(task_indices[0])
    else:
        messagebox.showwarning("Warning", "You must select a task to delete")


# Function to edit a selected task in the listbox
def edit_task():
    task_indices = task_listbox.curselection()
    if task_indices:
        selected_task_index = task_indices[0]
        task = task_listbox.get(selected_task_index)
        new_task = simpledialog.askstring("Update Task", "Edit the task:", initialvalue=task)
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
    else:
        messagebox.showwarning("Warning", "You must select a task to edit.")


# Function to clear all tasks from the listbox
def clear_tasks():
    task_listbox.delete(0, tk.END)


# Function to exit the application
def exit_application():
    if messagebox.askokcancel("Exit", "Do you want to exit the application?"):
        root.destroy()


# Main application window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry('800x500')  # Set initial window size
root.config(bg='#f0f0f0')  # Light gray background
root.resizable(False, False)  # Disable resizing

# Title label
add_title = tk.Label(root, text='To-Do List Application', font=("Helvetica", 24, "bold"), bg='#f0f0f0', fg='#333')
add_title.pack(pady=20)

# Entry widget to enter new tasks
task_entry = tk.Entry(root, width=70, font=("Helvetica", 14), bd=2, relief=tk.GROOVE)
task_entry.pack(pady=10)
task_entry.config(highlightbackground='black', highlightthickness=2)

# Frame for buttons in a horizontal layout
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack()

# Add Task button
add_task_button = tk.Button(button_frame, text="Add Task", bg="#4CAF50", fg="white", font=("Helvetica", 14, "bold"),
                            width=15, bd=2, relief=tk.RAISED, command=add_task)
add_task_button.pack(side='left', padx=10, pady=5)

# Delete Task button
delete_task_button = tk.Button(button_frame, text="Delete Task", bg="#f44336", fg="white",
                               font=("Helvetica", 14, "bold"), width=15, bd=2, relief=tk.RAISED, command=delete_task)
delete_task_button.pack(side='left', padx=10, pady=5)

# Update Task button
update_task_button = tk.Button(button_frame, text="Update Task", bg="#2196F3", fg="white",
                               font=("Helvetica", 14, "bold"), width=15, bd=2, relief=tk.RAISED, command=edit_task)
update_task_button.pack(side='left', padx=10, pady=5)

# Clear All Tasks button
clear_tasks_button = tk.Button(button_frame, text="Clear All Tasks", bg="#FFC107", fg="white",
                               font=("Helvetica", 14, "bold"), width=15, bd=2, relief=tk.RAISED, command=clear_tasks)
clear_tasks_button.pack(side='left', padx=10, pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=80, height=10, font=("Helvetica", 14), bd=2, relief=tk.GROOVE,
                          selectbackground="#f0f0f0")
task_listbox.pack(pady=20)
task_listbox.config(highlightbackground='black', highlightthickness=2)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

# Status bar
status_bar = tk.Label(root, text="Status: Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Helvetica", 12),
                      bg='#c0c0c0')
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Exit Application button
exit_button = tk.Button(root, text="Close", bg="#999", fg="white", font=("Helvetica", 14, "bold"), width=10, bd=2,
                        relief=tk.RAISED, command=exit_application)
exit_button.pack(pady=10)

root.mainloop()
