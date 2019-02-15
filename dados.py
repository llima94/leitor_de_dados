from tkinter import *


class Application:
    def __init__(self, master=None,):
        self.widget1 = Frame(master)
        self.widget1 = Frame(width=1024, height=768, bg='black')
        self.widget1.pack()
        self.msg = Label(self.widget1 , text= "Dados")
        self.msg.pack()
        self.arquivo = Button(self.widget1)
        self.arquivo["text"] = "Incluar sua Planilha"
        self.arquivo["font"] = ("Calibri", "10")
        self.arquivo["width"] = 15
        self.arquivo ["command"] = self.widget1.grid
        self.arquivo.pack()
        self.painel = Button (self.widget1)
        self.painel ["text"] = "Criar Grafico"
        self.painel ["font"] = ("Calibri" , "10")
        self.painel ["width"] = 15
        self.painel ["command"] = self.widget1.anchor
        self.painel.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = ("Sair")
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 15
        self.sair["command"] = self.widget1.quit
        self.sair.pack()



root = Tk()
Application(root)
root.mainloop()
