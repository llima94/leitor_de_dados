from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
janela = Tk()
janela.geometry("400x400")


dados = pd.read_excel(r"C:\Users\MecTecnologia\Desktop\dados.xlsx")


class Application:
    def grafico_linha (self,):
        pd.read_excel = (dados)
        plt.plot (dados["Idade"])
        plt.title("MEUS DADOS")
        plt.xlabel("Nome")
        plt.ylabel("Idade")
        plt.show()

    def grafico_pizza (self,):

        pd.read_excel = (dados)
        plt.pie(dados["Idade"], labels=dados["Nome"], autopct="%1.0f%%")
        plt.title("MEUS DADOS")
        plt.xlabel("")
        plt.ylabel("")
        plt.show()

    def grafico_barra (self,):

        pd.read_excel = (dados)
        plt.hist(dados["Nome"], bins=15)
        plt.title("MEUS DADOS")
        plt.xlabel("Nome")
        plt.ylabel("Idade")
        plt.show()

    def __init__(self, master=None,):
        self.widget1 = Frame(master)
        self.widget1 = Frame(width=1024, height=768, bg="black")
        self.widget1.pack()
        self.msg = Label(self.widget1 , text= "Dados")
        self.msg.pack()
        self.arquivo = Button(self.widget1)
        self.arquivo["text"] = "Grafico de Linha"
        self.arquivo["font"] = ("Calibri", "10")
        self.arquivo["width"] = 15
        self.arquivo ["command"] = self.grafico_linha
        self.arquivo.pack()
        self.painel = Button (self.widget1)
        self.painel ["text"] = "Grafico Pizza"
        self.painel ["font"] = ("Calibri" , "10")
        self.painel ["width"] = 15
        self.painel ["command"] = self.grafico_pizza
        self.painel.pack()
        self.barra = Button(self.widget1)
        self.barra["text"] = "Grafico Barra"
        self.barra["font"] = ("Calibri", "10")
        self.barra["width"] = 15
        self.barra["command"] = self.grafico_barra
        self.barra.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = ("Sair")
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 15
        self.sair["command"] = self.widget1.quit
        self.sair.pack()


root = ()
Application(root)
janela.mainloop()
