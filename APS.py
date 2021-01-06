from tkinter import *
import pyperclip

alf = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÉÊÝÇÁÃÍÚÂÕ0123456789õ,éêýçá?ãíúâ~´`'><:;/.{}[]=+§-_(" \
      ")*&¨%$#!@"


def criptografar():
    cript1 = ""

    def copiar():
        pyperclip.copy(cript1)

    texto = label_ciptografar.get()
    nivel = int(label_nivel.get())
    if nivel == 0 or nivel > 113:
        aviso = Label(janela, text="Digite a Chave", bg="#1a75ff", foreground='#ff6666', font="arial 13 bold")
        aviso.place(x=485, y=3)
    else:
        aviso = Label(janela, text="Digite a Chave", bg="#1a75ff", foreground="#1a75ff", font="arial 13 bold")
        aviso.place(x=485, y=3)
        for j in texto:
            ind = alf.index(j)
            if ind == 0:
                cript = alf[ind % len(alf)]
            else:
                cript = alf[(ind + nivel) % len(alf)]
            cript1 += cript
        # Interface
        frame_criptografar2 = Frame(frame_criptografar, borderwidth=1, relief="solid")
        frame_criptografar2.place(x=10, y=80, width=760, height=200)
        Label(frame_criptografar2, text=cript1, wraplength="736", font="arial 20").pack()
        bt_criptografar2 = Button(frame_criptografar, text="Copiar", foreground='white', bg="#4d94ff", command=copiar)
        bt_criptografar2.place(x=365, y=285)


def descriptografar():
    descript1 = ""

    def copiar():
        pyperclip.copy(descript1)

    texto = label_descriptografar.get()
    nivel = int(label_nivel.get())
    if nivel == 0 or nivel > 113:
        aviso = Label(janela, text="Digite a Chave", bg="#1a75ff", foreground="#ff6666", font="arial 15 bold")
        aviso.place(x=480, y=1)
    else:
        aviso = Label(janela, text="Digite a Chave", bg="#1a75ff", foreground="#1a75ff", font="arial 15 bold")
        aviso.place(x=480, y=1)
        for i in texto:
            ind = alf.index(i)
            if ind == 0:
                descript = alf[ind % len(alf)]
            else:
                descript = alf[(ind - nivel) % len(alf)]
            descript1 += descript
        # Interface
        frame_descriptografar2 = Frame(frame_descriptografar, borderwidth=1, relief="solid")
        frame_descriptografar2.place(x=10, y=80, width=760, height=200)
        Label(frame_descriptografar2, text=descript1, wraplength="736", font="arial 20").pack()
        bt_descriptografar2 = Button(frame_descriptografar, text="Copiar", foreground='white', bg="#4d94ff",
                                     command=copiar)
        bt_descriptografar2.place(x=365, y=285)


# Tela Principal
janela = Tk()
janela["bg"] = "#1a75ff"
janela.title("Criptografia")
janela.geometry("800x760")

# Nivel
text = StringVar()
texto_nivel = Label(janela, text="Chave de Criptografia de 1 a 113:", foreground='white', font="arial 12", bg="#1a75ff")
label_nivel = Entry(janela, font="arial 12", textvariable=text)
text.set("0")

# Criptografar
frame_criptografar = Frame(janela, borderwidth=1, relief="solid", bg="#4d94ff")
texto_criptografar = Label(frame_criptografar, text="Palavra a ser Criptografada:", foreground='white', bg="#4d94ff",
                           font="arial 12")
label_ciptografar = Entry(frame_criptografar, width=80)
bt_criptografar = Button(frame_criptografar, bg="#4d94ff", foreground='white', text="Criptografar", font="arial 12",
                         command=criptografar)

# Descriptografar
frame_descriptografar = Frame(janela, borderwidth=1, relief="solid", bg="#4d94ff")
frame_descriptografar.place(x=10, y=420, width=780, height=320)
texto_descriptografar = Label(frame_descriptografar, text="Palavra a ser Descriptografada:", font="arial 12",
                              foreground='white', bg="#4d94ff")
label_descriptografar = Entry(frame_descriptografar, width=80)
bt_descriptografar = Button(frame_descriptografar, text="Descriptografar", bg="#4d94ff", foreground='white',
                            font="arial 12", command=descriptografar)

# Edição Nivel
texto_nivel.place(x=200, y=2)
label_nivel.place(x=445, y=4, width=40)

# Edição Criptografar
frame_criptografar.place(x=10, y=60, width=780, height=320)
texto_descriptografar.pack()
label_descriptografar.pack()
bt_descriptografar.pack()

# Edição Criptografar
texto_criptografar.pack()
label_ciptografar.pack()
bt_criptografar.pack()

janela.mainloop()
