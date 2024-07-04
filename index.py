from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

# Criar nossa janela
jan = Tk()
jan.title("Remina")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

# ===== Carregando IMG ==========
logo = PhotoImage(file="icons/logo.png")

# ===== Widgets ================
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PasswordLabel = Label(RightFrame, text="Password", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PasswordLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def LoginAsses():
    User = UserEntry.get()
    Pass = PassEntry.get()
    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBase.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso confirmado. Bem-vindo")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso negado. Verifique se está cadastrado no sistema")

# Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=LoginAsses)
LoginButton.place(x=100, y=225)

def Register():
    # Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # Inserindo Widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=150, y=16)

    EmailLabel = Label(RightFrame, text="Email", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=150, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if Name == "" or Email == "" or User == "" or Pass == "":
            messagebox.showerror(title="Register Error", message="Não deixe nenhum campo vazio. Preencha todos os campos")
        else:
            DataBase.cursor.execute("""
            INSERT INTO Users (Name, Email, User, Password) VALUES (?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBase.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

    RegisterButton = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    RegisterButton.place(x=100, y=225)

    def BackToLogin():
        # Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        RegisterButton.place(x=5000)
        Back.place(x=5000)
        # Trazendo de volta os widgets de login
        LoginButton.place(x=100, y=225)
        RegisterButton.place(x=100, y=260)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=100, y=260)

jan.mainloop()