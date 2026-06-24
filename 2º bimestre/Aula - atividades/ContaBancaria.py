import tkinter as tk
from tkinter import messagebox, simpledialog


class Cliente:
    def __init__(self, nome:str, cpf:str):
        self.__nome = nome
        self.__cpf = cpf
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_endereco(self):
        return 'oi'
    
    def exibir_dados(self):
        return f'Titular: {self.__nome} \nCPF: {self.__cpf}'


class ContaBancaria:

    numeros_contas = []

    def __init__(self, titular, numero, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        ContaBancaria.numeros_contas.append(numero)

    def get_titular(self):
        return self.__titular
       
    def get_numero(self):
        return self.__numero
       
    def get_saldo(self):
        return self.__saldo
    
    @classmethod
    def verificar_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))
    
    @classmethod
    def contas_duplicadas(cls):
        repetidos = set()
        n_repetidos = []
        for x in cls.numeros_contas:
            if ContaBancaria.numeros_contas.count(x) > 1:
                repetidos.add(x)
            else:
                n_repetidos.append(x)
        return f'{repetidos}'
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            return True
        else:
            return False
        
    def exibir_dados(self):
        return f'Titular: {self.__titular}\nNumero da conta: {self.__numero}\nSaldo: R${self.__saldo}'

class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")

        cliente1 = Cliente("Helia", "164913")
        print(cliente1.exibir_dados())

        self.contas = [
            ContaBancaria(cliente1, 1001, 500)
            # ContaBancaria("Maria", 1002, 1000),
            # ContaBancaria("Pedro", 1003, 300),
            # ContaBancaria("Esther", 1004, 20)
        ]

        if(self.contas[0].verificar_conta_duplicada()):
            messagebox.showerror("Erro", "Existe conta duplicada")
            messagebox.showinfo("contas", self.contas[0].contas_duplicadas())
            exit()

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            # btn_depositar.config(state="disabled")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            # btn_sacar.config(state="disabled")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            # btn_transferir.config(state="disabled")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            # btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)

    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")

        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")

        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")

        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")

        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())


janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()