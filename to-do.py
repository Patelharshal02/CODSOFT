import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, padx=10)

        self.scrollbar = tk.Scrollbar(self.task_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.show_tasks_button = tk.Button(self.button_frame, text="Show Tasks", command=self.show_tasks)
        self.show_tasks_button.pack(side=tk.LEFT, padx=5)

        self.mark_done_button = tk.Button(self.button_frame, text="Mark Task as Done", command=self.mark_task_done)
        self.mark_done_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        n_tasks = simpledialog.askinteger("Add Task", "How many tasks do you want to add?", parent=self.root)
        
        if n_tasks:
            for i in range(n_tasks):
                task = simpledialog.askstring("Add Task", f"Enter task {i+1}:", parent=self.root)
                if task:
                    self.tasks.append({"task": task, "done": False})
                    messagebox.showinfo("Add Task", "Task added successfully!")
                else:
                    messagebox.showwarning("Add Task", "Task cannot be empty!")

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Not Done"
            self.task_listbox.insert(tk.END, f"{index + 1}. {task['task']} - {status}")

    def mark_task_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            if not self.tasks[task_index]["done"]:
                self.tasks[task_index]["done"] = True
                self.show_tasks()
                messagebox.showinfo("Mark Task as Done", "Task marked as done!")
            else:
                messagebox.showwarning("Mark Task as Done", "Task is already marked as done!")
        else:
            messagebox.showwarning("Mark Task as Done", "Please select a task to mark as done.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
