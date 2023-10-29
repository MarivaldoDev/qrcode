import qrcode
from tkinter import *
from tkinter import messagebox


def qr():
    link = link_entrada.get()
    if link == "":
        messagebox.showerror(title="Erro", message="Algo precisa ser digitado!")
    else:
        meu_qr = qrcode.make(link)
        meu_qr.save("qrcode.png")
        messagebox.showinfo(title="Sucesso", message="Código qr gerado com sucesso!")
        meu_qr.show()
    
    link_entrada.delete(0, END)

    
tela = Tk()
tela.title("Gerador de QRs")
tela.configure(background='#dfe3ee')
tela.geometry("280x140")

Label(tela, text="Link", bg='#dfe3ee', font="arial 15").place(x=10, y=10)
link_entrada = Entry(tela, width=40)
link_entrada.place(x=10, y=40)

Button(tela, text="Gerar", bg='#107db2', fg='white', font="arial 12", command=qr).place(x=100, y=90)

tela.mainloop()