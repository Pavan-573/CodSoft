import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("665x400+550+250")
        self.root.resizable(0, 0)
        self.root.configure(bg="#B5E5CF")

        self.db_connection = sql.connect('listOfTasks.db')
        self.cursor = self.db_connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')
        self.tasks = []

        self.create_widgets()
        self.retrieve_tasks()
        self.update_task_list()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#8EE5EE")
        frame.pack(side="top", expand=True, fill="both")

        tk.Label(frame, text="TO-DO LIST \n Enter the Task Title:",
                 font=("arial", 14, "bold"), bg="#8EE5EE", fg="#FF6103").place(x=20, y=30)

        self.task_entry = tk.Entry(frame, font=("Arial", 14), width=42, bg="white")
        self.task_entry.place(x=180, y=30)

        tk.Button(frame, text="Add", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=self.add_task).place(x=18, y=80)
        tk.Button(frame, text="Remove", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=self.delete_task).place(x=240, y=80)
        tk.Button(frame, text="Delete All", width=15, bg='#D4AC0D', font=("arial", 14, "bold"), command=self.delete_all_tasks).place(x=460, y=80)
        tk.Button(frame, text="Exit / Close", width=52, bg='#D4AC0D', font=("arial", 14, "bold"), command=self.close).place(x=17, y=330)

        self.task_listbox = tk.Listbox(frame, width=70, height=9, font="bold", selectmode='SINGLE', bg="white", fg="black",
                                      selectbackground="#FF8C00", selectforeground="black")
        self.task_listbox.place(x=17, y=140)

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task)
            self.cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task,))
            self.update_task_list()
            self.task_entry.delete(0, 'end')

    def delete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            if selected_task in self.tasks:
                self.tasks.remove(selected_task)
                self.update_task_list()
                self.cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task,))
        except IndexError:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        if messagebox.askyesno('Delete All', 'Are you sure?'):
            self.tasks.clear()
            self.cursor.execute('DELETE FROM tasks')
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, 'end')
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def retrieve_tasks(self):
        self.tasks.clear()
        for row in self.cursor.execute('SELECT title FROM tasks'):
            self.tasks.append(row[0])

    def close(self):
        self.db_connection.commit()
        self.cursor.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
