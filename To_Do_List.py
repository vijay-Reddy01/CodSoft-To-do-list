import tkinter as tkn
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
      
        self.root = root
        self.root.title("To-Do-List")
        self.tasks = []
        self.heading = tkn.Label(self.root, text="To-Do-List", font=("Helvetica", 16))
        self.heading.pack(pady=10)
        self.entryFrame = tkn.Frame(self.root)
        self.entryFrame.pack(pady=10)
        self.taskInput = tkn.Entry(self.entryFrame, width=40)
        self.taskInput.grid(row=0, column=0, padx=10)
        self.addTaskBtn = tkn.Button(self.entryFrame, text="Add Task", command=self.add_task, bg="green")
        self.addTaskBtn.grid(row=0, column=1)

        self.listFrm = tkn.Frame(self.root)
        self.listFrm.pack(pady=10)

        self.priorityLabel = tkn.Label(self.listFrm, text="Priority", width=10, anchor='w')
        self.priorityLabel.grid(row=0, column=0)

        self.taskLabel = tkn.Label(self.listFrm, text="Task Name", width=40, anchor='w')
        self.taskLabel.grid(row=0, column=1)

        self.scrollBar = tkn.Scrollbar(self.listFrm, orient=tkn.VERTICAL)

        self.priority_listbox = tkn.Listbox(self.listFrm, width=10, height=15, yscrollcommand=self.scrollBar.set)
        self.priority_listbox.grid(row=1, column=0)
        self.tasksbox = tkn.Listbox(self.listFrm, width=40, height=15, yscrollcommand=self.scrollBar.set)
        self.tasksbox.grid(row=1, column=1)

        self.scrollBar.configure(command=self.yview)
        self.scrollBar.grid(row=1, column=2, sticky='ns')

        self.priorityPanel = tkn.Frame(self.root)
        self.priorityPanel.pack(pady=10)

        self.upBtn = tkn.Button(self.priorityPanel, text="↑", command=self.moveUp, bg="orange")
        self.upBtn.grid(row=0, column=0)

        self.downBtn = tkn.Button(self.priorityPanel, text="↓", command=self.moveDown, bg="orange")
        self.downBtn.grid(row=0, column=1)

        self.delete_button = tkn.Button(self.priorityPanel, text="Delete Task", command=self.delete_task, bg="red")
        self.delete_button.grid(row=0, column=2, padx=10)

    def add_task(self):
        task = self.taskInput.get()
        if task:
            self.tasks.append(task)
            self.newListBox()
            self.taskInput.delete(0, tkn.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def newListBox(self):
        self.priority_listbox.delete(0, tkn.END)
        self.tasksbox.delete(0, tkn.END)
        for idx, task in enumerate(self.tasks):
            self.priority_listbox.insert(tkn.END, f"{idx + 1}")
            self.tasksbox.insert(tkn.END, task)

    def yview(self, *args):
        self.priority_listbox.yview(*args)
        self.tasksbox.yview(*args)

    def moveUp(self):
        taskSelected = self.tasksbox.curselection()
        if taskSelected:
            index = taskSelected[0]
            if index != 0:
                self.tasks[index], self.tasks[index - 1] = self.tasks[index - 1], self.tasks[index]
                self.newListBox()
                self.tasksbox.selection_set(index - 1)

    def moveDown(self):
        taskSelected = self.tasksbox.curselection()
        if taskSelected:
            index = taskSelected[0]
            if index != len(self.tasks) - 1:
                self.tasks[index], self.tasks[index + 1] = self.tasks[index + 1], self.tasks[index]
                self.newListBox()
                self.tasksbox.selection_set(index + 1)
    def delete_task(self):
        taskSelected = self.task_listbox.curselection()
        if taskSelected:
            index = taskSelected[0]
            del self.task_list[index]
            self.update_listboxes()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
if __name__ == "__main__":
    root = tkn.Tk()
    app = ToDoListApp(root)
    root.mainloop()
