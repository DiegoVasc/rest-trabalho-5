from Tkinter import *
import requests


def bt_click():
    valor = ed.get()
    retorno = requests.post("http://10.180.61.164:4000/mid/%s" % (valor))
    lb["text"] = retorno.json()


janela = Tk()

lb1 = Label(janela, text = "INFORME SEU TEXTO",font = ("Times New Roman",15))
lb1.place(x=100, y=10)

ed = Entry(janela,width=50)
ed.place(x=100, y=40)

bt  = Button(janela,width=20, text = "ENVIAR", command=bt_click)
bt.place(x=200, y=100)

lb2 = Label(janela, text = "RESULTADOS:",font = ("Times New Roman",15))
lb2.place(x=100, y=190)

lb = Label(janela, text = "",font = ("Times New Roman",20))
lb.place(x=100, y=220)

janela.title("Tela de Usuario")
janela.geometry("710x500+700+100")

janela.mainloop()
