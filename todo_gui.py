import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Entry for new tasks
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Buttons frame
        buttons_frame = tk.Frame(root)
        buttons_frame.pack()

        self.add_button = tk.Button(buttons_frame, text="Add Task", width=12, command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.remove_button = tk.Button(buttons_frame, text="Remove Task", width=12, command=self.remove_task)
        self.remove_button.grid(row=0, column=1, padx=5)

        self.done_button = tk.Button(buttons_frame, text="Mark Done", width=12, command=self.mark_done)
        self.done_button.grid(row=0, column=2, padx=5)

        # Listbox for tasks
        self.listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Load tasks from file
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            for task in self.tasks:
                self.listbox.insert(tk.END, task)

    def save_tasks(self):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            self.tasks.pop(index)
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.endswith(" ✔️"):
                task_done = task + " ✔️"
                self.tasks[index] = task_done
                self.listbox.delete(index)
                self.listbox.insert(index, task_done)
                self.listbox.selection_set(index)
                self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
