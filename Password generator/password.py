import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

class GUI():
    def __init__(self, master):
        self.master = master
        self.master.title('Password Generator')
        self.master.geometry('660x500')
        self.master.config(bg='#FF8000')
        self.master.resizable(False, False)

        # Initialize database
        self.init_db()

        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_passwordlen = IntVar()

        self.create_widgets()

    def init_db(self):
        """Initialize the database and create the table if it does not exist."""
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (Username TEXT NOT NULL UNIQUE, GeneratedPassword TEXT NOT NULL);")
            db.commit()

    def create_widgets(self):
        """Create and place all the widgets in the window."""
        Label(text=":PASSWORD GENERATOR:", anchor=N, fg='darkblue', bg='#FF8000', font='arial 20 bold underline').grid(row=0, column=1)

        Label(text="").grid(row=1, column=0, columnspan=2)
        Label(text="").grid(row=2, column=0, columnspan=2)
        Label(text="").grid(row=3, column=0, columnspan=2)

        Label(text="Enter User Name: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=4, column=0)
        self.textfield = Entry(textvariable=self.n_username, font='times 15', bd=6, relief='ridge')
        self.textfield.grid(row=4, column=1)
        self.textfield.focus_set()

        Label(text="").grid(row=5, column=0)

        Label(text="Enter Password Length: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=6, column=0)
        self.length_textfield = Entry(textvariable=self.n_passwordlen, font='times 15', bd=6, relief='ridge')
        self.length_textfield.grid(row=6, column=1)

        Label(text="").grid(row=7, column=0)

        Label(text="Generated Password: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=8, column=0)
        self.generated_password_textfield = Entry(textvariable=self.generatedpassword, font='times 15', bd=6, relief='ridge', fg='#DC143C', state='readonly')
        self.generated_password_textfield.grid(row=8, column=1)

        Label(text="").grid(row=9, column=0)

        Button(text="GENERATE PASSWORD", bd=3, relief='solid', padx=1, pady=1, font='Verdana 15 bold', fg='#68228B', bg='#BCEE68', command=self.generate_pass).grid(row=11, column=1)

        Label(text="").grid(row=12, column=0)

        Button(text="ACCEPT", bd=3, relief='solid', padx=1, pady=1, font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0', command=self.accept_fields).grid(row=13, column=1)

        Label(text="").grid(row=14, column=1)

        Button(text="RESET", bd=3, relief='solid', padx=1, pady=1, font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0', command=self.reset_fields).grid(row=15, column=1)

    def generate_pass(self):
        """Generate a random password based on user input."""
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        chars = "@#%&()\"?!"
        numbers = string.digits

        name = self.n_username.get()
        length = self.n_passwordlen.get()

        if not name:
            messagebox.showerror("Error", "Username cannot be empty")
            return

        if not name.isalpha():
            messagebox.showerror("Error", "Username must be a string")
            self.textfield.delete(0, END)
            return

        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            self.length_textfield.delete(0, END)
            return

        # Generate password
        u = random.randint(1, length - 3)
        l = random.randint(1, length - 2 - u)
        c = random.randint(1, length - 1 - u - l)
        n = length - u - l - c

        password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers, n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        self.generatedpassword.set(gen_passwd)

    def accept_fields(self):
        """Accept the generated password and store it in the database."""
        username = self.n_username.get()
        password = self.generatedpassword.get()

        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute("INSERT INTO users (Username, GeneratedPassword) VALUES (?, ?)", (username, password))
                db.commit()
                messagebox.showinfo("Success!", "Password generated and saved successfully")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists. Please choose another username")

    def reset_fields(self):
        """Reset all input fields."""
        self.textfield.delete(0, END)
        self.length_textfield.delete(0, END)
        self.generatedpassword.set("")

if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.mainloop()
