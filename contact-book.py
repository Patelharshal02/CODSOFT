import tkinter as tk

def add_contact():
    name = name_entry.get()
    phone_no = phone_no_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts.append({"Name": name, "Phone_no": phone_no, "Email": email, "Address": address})
    update_display()
    clear_entries()

def search_contact():
    search_term = search_entry.get()
    search_results = [contact for contact in contacts if search_term.lower() in contact["Name"].lower()]
    update_display(search_results)

def delete_contact():
    delete_index = contact_listbox.curselection()[0]
    del contacts[delete_index]
    update_display()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_no_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    
def update_display(display_contacts=None):
    contact_listbox.delete(0, tk.END)
    if display_contacts is None:
        for contact in contacts:
            contact_listbox.insert(tk.END, contact["Name"])
    else:
        for contact in display_contacts:
            contact_listbox.insert(tk.END, contact["Name"])


root = tk.Tk()
root.title("Contact Book")


name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
phone_no_label = tk.Label(root, text="Phone Number:")
phone_no_entry = tk.Entry(root)
email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)
address_label = tk.Label(root, text="Address:")
address_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Contact", command=add_contact)

search_label = tk.Label(root, text="Search:")
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_contact)

contact_listbox = tk.Listbox(root, width=50, height=10)


delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)


name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry.grid(row=0, column=1, padx=5, pady=5)
phone_no_label.grid(row=1, column=0, padx=5, pady=5)
phone_no_entry.grid(row=1, column=1, padx=5, pady=5)
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry.grid(row=2, column=1, padx=5, pady=5)
address_label.grid(row=3, column=0, padx=5, pady=5)
address_entry.grid(row=3, column=1, padx=5, pady=5)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

search_label.grid(row=5, column=0, padx=5, pady=5)
search_entry.grid(row=5, column=1, padx=5, pady=5)
search_button.grid(row=5, column=2, padx=5, pady=5, sticky="WE")

contact_listbox.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

delete_button.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="WE")

contacts = []

update_display()

root.mainloop()
