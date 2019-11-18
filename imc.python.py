#Atividade 3 de linguagens de programação
#Interface gráfica para o cálculo do imc


from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte1 = ("Arial"), ("10")

        self.espaço1 = Frame(master)
        self.espaço1["pady"] = 10
        self.espaço1.pack()

        self.espaço12 = Frame(master)
        self.espaço12["padx"] = 20
        self.espaço12.pack()

        self.espaço13 = Frame(master)
        self.espaço13["padx"] = 20
        self.espaço13.pack()

        self.espaço2 = Frame(master)
        self.espaço2["padx"] = 20
        self.espaço2.pack()

        self.espaço3 = Frame(master)
        self.espaço3["padx"] = 20
        self.espaço3.pack()

        self.espaço4 = Frame(master)
        self.espaço4["padx"] = 20
        self.espaço4.pack()

        self.espaço5 = Frame(master)
        self.espaço5["padx"] = 20
        self.espaço5.pack()

        self.espaço6 = Frame(master)
        self.espaço6["padx"] = 20
        self.espaço6.pack()

        self.nome = Label(self.espaço1, text="CÁLCULO DO IMC-Indice de massa corporal")
        self.nome["font"] = ("Arial", "10", "bold")
        self.nome.pack()

        self.nome1Label = Label(self.espaço12, text="NOME DO PACIENTE", font=self.fonte1)
        self.nome1Label.pack(side=LEFT)

        self.nome1 = Entry(self.espaço12)
        self.nome1["width"] = 30
        self.nome1["font"] = self.fonte1
        self.nome1.pack(side=LEFT)

        self.nome2Label = Label(self.espaço13, text="ENDEREÇO COMPLETO:", font=self.fonte1)
        self.nome2Label.pack(side=LEFT)

        self.nome2 = Entry(self.espaço13)
        self.nome2["width"] = 33
        self.nome2["font"] = self.fonte1
        self.nome2.pack(side=LEFT)

        self.digitoLabel = Label(self.espaço2, text="PESO", font=self.fonte1)
        self.digitoLabel.pack(side=LEFT)

        self.digito = Entry(self.espaço2)
        self.digito["width"] = 17
        self.digito["font"] = self.fonte1
        self.digito.pack(side=LEFT)

        self.digito2Label = Label(self.espaço3, text="ALTURA", font=self.fonte1)
        self.digito2Label.pack(side=LEFT)

        self.digito2 = Entry(self.espaço3)
        self.digito2["width"] = 19
        self.digito2["font"] = self.fonte1
        self.digito2.pack(side=LEFT)

        # Definindo caixa "IMC"
        self.imcLabel = Label(self.espaço4, text="IMC", font=self.fonte1)
        self.imcLabel.pack(side=LEFT)

        self.imcValor = Label(self.espaço5, text="", font=self.fonte1)
        self.imcValor.pack(side=RIGHT)

        # Definindo o botão de calcular
        self.calcular = Button(self.espaço6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack()

    # Calculando o imc
    def calcula(self):
        peso = self.digito.get()
        altura = self.digito2.get()

        resp = (float(peso)) / (float(altura) * float(altura))

        if peso:
            self.imcValor["text"] = resp


root = Tk()
Application(root)
root.mainloop()
