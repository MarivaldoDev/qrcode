import qrcode
from customtkinter import *
from tkinter import messagebox
from PIL import Image
from time import sleep


def qr():
    link = link_entrada.get().strip()
    if link == "":
        messagebox.showerror(title="Erro", message="Algo precisa ser digitado!")
    else:
        meu_qr = qrcode.make(link)
        meu_qr.save("qrcode.png")
        sleep(2)
        imagem = Image.open("qrcode.png")
    
        imagem_tk = CTkImage(light_image=imagem, dark_image=imagem, size=(340, 290))
        CTkLabel(frame1, text='', image=imagem_tk).place(x=10, y=10)
        
    
    link_entrada.delete(0, END)

    
tela = CTk()
tela.title("Gerador de QRs")
tela.resizable(width=False, height=False)
tela.geometry("400x500")

frame1 = CTkFrame(tela, width=180, height=170, border_width=5, border_color='blue')

CTkLabel(tela, text="Link", text_color='aliceblue', font=("arial", 25)).place(x=10, y=20)
link_entrada = CTkEntry(tela, width=220, border_width=2, border_color='green', 
placeholder_text='Digite o link...', 
placeholder_text_color='white')

gerar = CTkButton(tela, text="Gerar", fg_color='#191970', text_color='aliceblue',
border_width=1,
border_color='aliceblue', 
width=100, 
font=("arial", 18), 
command=qr)


gerar.place(x=65, y=105)
link_entrada.place(x=10, y=60)
frame1.place(relx=0.05, rely=0.37, relwidth=0.90, relheight=0.62)


tela.mainloop()