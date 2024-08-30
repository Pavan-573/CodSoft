import tkinter as tk
import math

class SC_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Scientific Calculator')
        self.root.configure(bg='#0000FF')
        self.root.resizable(width=False, height=False)

        self.ent_field = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25),
                                  borderwidth=10, justify="right")
        self.ent_field.grid(row=0, columnspan=10, padx=10, pady=10, sticky='nsew')
        self.ent_field.insert(0, '0')

        self.current = ''
        self.inp_value = True
        self.result = False
        self.FONT = ('Arial', 10, 'bold')

        self.create_buttons()

    def Entry(self, value):
        self.ent_field.delete(0, 'end')
        self.ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = self.ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        try:
            temp_str = self.ent_field.get()
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    def Deg(self):
        try:
            self.current = math.degrees(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Rad(self):
        try:
            self.current = math.radians(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Exp(self):
        try:
            self.current = math.exp(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Fact(self):
        try:
            self.current = math.factorial(int(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Sin(self):
        try:
            self.current = math.sin(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Cos(self):
        try:
            self.current = math.cos(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Tan(self):
        try:
            self.current = math.tan(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Ln(self):
        try:
            self.current = math.log(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Log_10(self):
        try:
            self.current = math.log10(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Log_2(self):
        try:
            self.current = math.log2(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_2(self):
        try:
            self.current = float(self.ent_field.get()) ** 2
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_3(self):
        try:
            self.current = float(self.ent_field.get()) ** 3
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Pow_10_n(self):
        try:
            self.current = 10 ** float(self.ent_field.get())
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def One_div_x(self):
        try:
            self.current = 1 / float(self.ent_field.get())
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Abs(self):
        try:
            self.current = abs(float(self.ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def create_buttons(self):
        buttons = [
            ('CE', self.Clear_Entry), ('√', self.SQ_Root), ('/', lambda: self.Standard_Ops('/')),
            ('7', lambda: self.Enter_Num(7)), ('8', lambda: self.Enter_Num(8)), ('9', lambda: self.Enter_Num(9)), ('*', lambda: self.Standard_Ops('*')),
            ('4', lambda: self.Enter_Num(4)), ('5', lambda: self.Enter_Num(5)), ('6', lambda: self.Enter_Num(6)), ('-', lambda: self.Standard_Ops('-')),
            ('1', lambda: self.Enter_Num(1)), ('2', lambda: self.Enter_Num(2)), ('3', lambda: self.Enter_Num(3)), ('+', lambda: self.Standard_Ops('+')),
            ('0', lambda: self.Enter_Num(0)), ('.', lambda: self.Standard_Ops('.')), ('=', lambda: self.Standard_Ops('=')), ('+', lambda: self.Standard_Ops('+')),
            ('π', self.Pi), ('e', self.E), ('Deg', self.Deg), ('Exp', self.Exp),
            ('x!', self.Fact), ('sin', self.Sin), ('cos', self.Cos), ('tan', self.Tan),
            ('Rad', self.Rad), ('ln', self.Ln), ('log10', self.Log_10), ('log2', self.Log_2),
            ('x²', self.Pow_2), ('x³', self.Pow_3), ('10ⁿ', self.Pow_10_n), ('1/x', self.One_div_x),
            ('Abs', self.Abs)
        ]

        row = 1
        col = 0
        for text, cmd in buttons:
            btn = tk.Button(self.root, text=text, command=cmd, font=self.FONT,
                            width=5, height=2, fg="#000000", highlightbackground='#ADD8E6', highlightthickness=2)
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

if __name__ == '__main__':
    root = tk.Tk()
    sc_app = SC_Calculator(root)
    root.mainloop()
