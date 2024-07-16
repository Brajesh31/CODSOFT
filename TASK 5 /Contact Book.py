import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, filedialog
import csv

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = []

def add_contact():
    dialog = AddUpdateContactDialog(root)

def view_contacts():
    contact_tree.delete(*contact_tree.get_children())
    for index, contact in enumerate(contacts, start=1):
        contact_tree.insert("", "end", values=(index, contact.name, contact.address, contact.phone, contact.email))

def search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone:")
    contact_tree.delete(*contact_tree.get_children())
    if query:
        for index, contact in enumerate(contacts, start=1):
            if query.lower() in contact.name.lower() or query in contact.phone:
                contact_tree.insert("", "end", values=(index, contact.name, contact.address, contact.phone, contact.email))
    else:
        view_contacts()

def update_contact():
    selected_item = contact_tree.selection()
    if selected_item:
        index = int(contact_tree.item(selected_item)['values'][0]) - 1
        selected_contact = contacts[index]
        dialog = AddUpdateContactDialog(root, contact=selected_contact)
    else:
        messagebox.showerror("Error", "No contact selected")

def delete_contact():
    selected_item = contact_tree.selection()
    if selected_item:
        index = int(contact_tree.item(selected_item)['values'][0]) - 1
        contacts.pop(index)
        messagebox.showinfo("Success", "Contact deleted successfully")
        view_contacts()
    else:
        messagebox.showerror("Error", "No contact selected")

def export_to_csv():
    if contacts:
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email", "Address"])
                for contact in contacts:
                    writer.writerow([contact.name, contact.phone, contact.email, contact.address])
            messagebox.showinfo("Success", "Contacts exported to CSV successfully")
    else:
        messagebox.showwarning("Warning", "No contacts to export")

class AddUpdateContactDialog(simpledialog.Dialog):
    def __init__(self, parent, contact=None):
        self.contact = contact
        super().__init__(parent)

    def body(self, master):
        tk.Label(master, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        tk.Label(master, text="Phone:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        tk.Label(master, text="Email:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        tk.Label(master, text="Address:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.name_entry = tk.Entry(master, font=("Arial", 12), width=30)
        self.phone_entry = tk.Entry(master, font=("Arial", 12), width=30)
        self.email_entry = tk.Entry(master, font=("Arial", 12), width=30)
        self.address_entry = tk.Entry(master, font=("Arial", 12), width=30)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        if self.contact:
            self.name_entry.insert(tk.END, self.contact.name)
            self.phone_entry.insert(tk.END, self.contact.phone)
            self.email_entry.insert(tk.END, self.contact.email)
            self.address_entry.insert(tk.END, self.contact.address)

    def validate_phone(self):
        phone = self.phone_entry.get().strip()
        if not phone.isdigit():
            messagebox.showerror("Error", "Phone number should contain only digits.")
            return False
        return True

    def apply(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and self.validate_phone():
            if self.contact:
                # Update existing contact
                self.contact.name = name
                self.contact.phone = phone
                self.contact.email = email
                self.contact.address = address
                messagebox.showinfo("Success", "Contact updated successfully")
            else:
                # Add new contact
                new_contact = Contact(name, phone, email, address)
                contacts.append(new_contact)
                messagebox.showinfo("Success", "Contact added successfully")

            view_contacts()
        else:
            messagebox.showerror("Error", "Name and phone are required")

root = tk.Tk()
root.title("Contact Management System")
root.geometry("800x500")
root.configure(background="#d9e1f2")

# Set ttk theme to 'clam' for blue accents
style = ttk.Style()
style.theme_use('clam')

# Frame for treeview and scrollbar
tree_frame = tk.Frame(root, bg="#d9e1f2")
tree_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)

# Create Treeview widget
contact_tree = ttk.Treeview(tree_frame, columns=("S.No.", "Name", "Address", "Phone", "Email"), show="headings", height=15)
contact_tree.grid(row=0, column=0, sticky=tk.NSEW)

# Configure column headings
contact_tree.heading("S.No.", text="S.No.")
contact_tree.heading("Name", text="Name")
contact_tree.heading("Address", text="Address")
contact_tree.heading("Phone", text="Phone", anchor=tk.CENTER)
contact_tree.heading("Email", text="Email")

# Configure column widths
contact_tree.column("S.No.", width=50)
contact_tree.column("Name", width=150)
contact_tree.column("Address", width=200)
contact_tree.column("Phone", width=120)
contact_tree.column("Email", width=200)

# Set font size for treeview content
tree_font = ("Arial", 10)  # Increase font size here
contact_tree.tag_configure("Treeview", font=tree_font)

# Scrollbar for treeview
tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=contact_tree.yview)
tree_scroll.grid(row=0, column=1, sticky="ns")
contact_tree.configure(yscrollcommand=tree_scroll.set)

# Buttons
button_frame = tk.Frame(root, bg="#d9e1f2")
button_frame.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)

button_width = 20
button_height = 2
button_font = ("Arial", 12)
button_bg = "#1976d2"
button_fg = "white"

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, bg=button_bg, fg=button_fg, width=button_width, height=button_height, font=button_font)
add_button.grid(row=0, column=0, padx=10, pady=10)

view_button = tk.Button(button_frame, text="View Contacts", command=view_contacts, bg=button_bg, fg=button_fg, width=button_width, height=button_height, font=button_font)
view_button.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact, bg=button_bg, fg=button_fg, width=button_width, height=button_height, font=button_font)
search_button.grid(row=0, column=2, padx=10, pady=10)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact, bg=button_bg, fg=button_fg, width=button_width, height=button_height, font=button_font)
update_button.grid(row=1, column=0, padx=10, pady=10)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact, bg=button_bg, fg=button_fg, width=button_width, height=button_height, font=button_font)
delete_button.grid(row=1, column=1, padx=10, pady=10)

export_button = tk.Button(button_frame, text="Export to CSV", command=export_to_csv, bg=button_bg, fg=button_fg, width=button_width, height=button_height, font=button_font)
export_button.grid(row=1, column=2, padx=10, pady=10)

# Configure grid weights
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
