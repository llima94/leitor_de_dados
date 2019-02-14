from tkinter import *


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.grid()
        self.msg = Label(self.widget1 , text= "Dados")
        self.msg.grid()
        self.arquivo = Button(self.widget1)
        self.arquivo["text"] = "Incluar sua Planilha"
        self.arquivo["font"] = ("Calibri", "10")
        self.arquivo["width"] = 15
        self.arquivo["command"] = self.widget1.after_idle
        self.arquivo.grid()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.grid()


root = Tk()
Application(root)
root.mainloop()
