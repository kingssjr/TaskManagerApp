import tkinter as tk
from tkinter import messagebox

class TaskManagerView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Task Manager")
        self.build_login_view()

    def build_login_view(self):
        self.clear_frame()
        tk.Label(self.root, text="Login").pack()
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.login).pack()
        tk.Button(self.root, text="Register", command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success = self.controller.login(username, password)
        if success:
            messagebox.showinfo("Success", "Login successful!")
            self.build_task_view()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success = self.controller.register(username, password)
        if success:
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "Username already exists!")

    def build_task_view(self):
        self.clear_frame()
        tk.Label(self.root, text="Task Manager").pack()
        tk.Button(self.root, text="Add Task", command=self.add_task).pack()

    def add_task(self):
        pass  # Implementação futura

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()