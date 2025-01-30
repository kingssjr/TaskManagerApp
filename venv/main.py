import tkinter as tk
from app.controllers import TaskManagerController
from app.views import TaskManagerView

if __name__ == "__main__":  # Corrigido o erro no if
    controller = TaskManagerController()
    root = tk.Tk()
    app = TaskManagerView(root, controller)
    root.mainloop()