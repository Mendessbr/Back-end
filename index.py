#Importar as bibliotecas
from tkinter import *
from tkinter import massagebox
from tkinter import ttk
from tkinter import messagebox
import DataBaser

#Criar nossa janela
jan = Tk()
jan .title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

#=====Carregando IMG==========
logo = PhotoImage(file="Icons/logo.png")

#===== Widgets ================
LeftFrame = Frame(jan, width=100, height=300, bg="MIDNIGHTBLUE", reief="reaise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width =395, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=200, y=110)

PasswordLabel = Label(RightFrame, text="Password", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PasswordLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

def LoginAsses():
    DataBaser.cursor.execute("""
    SELECT * FROM Users
     WHERE (User = ? AND Password = ?)
""", (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.execute.fetchone()
    try:
        if (user in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message= "Acesso confirmaod. Bem-vindo")
    except:
             messagebox.showinfo(title="Login Info", message="Acesso negado. Verifique se esta cadastrado no sistema")

#Botoes
LoginInButton = ttk.Button(RightFrame, text= "Register", width=30, command=Login )
LoginInButton.place(x=100, y=225)

def Register():
    #Removendo Widgets de Login
    LoginInButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo Widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=150, y=16)

    EmailLabel = Label(RightFrame, text="Email", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass =PassEntry.get() 

        if (name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message= "Não deixe nenhum campo vazio. Preencha todos os campos")
        else:
            DataBaser.cursor .execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """,(Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

    RegisterButton = ttk.Button(RightFrame, text= "Register", width=30, command=Register)
    RegisterButton.place(x=100, y=225)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(X=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(X=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)
    #trazendo de volta oswidgets de login
    LoginInButton.place(x=100)
    RegisterButton.place(x=125)

RegisterButton = ttk.Button(RightFrame, text= "Register", width=20, command=Register  )
RegisterButton.place(x=100, y=260)


jan.mainloop()