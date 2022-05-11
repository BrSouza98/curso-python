#Python POO

class contaBancaria():
    #metodo construtor
    def __init__(self, nome, senha, saldo):
        self.nome = nome
        self.senha = senha
        self.saldo = int(saldo)

    #getters e setters - nome
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


    #getters e setters - senha
    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha


    # getters e setters - saldo
    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = int(saldo)


    def sacarDinheiro(self, valorSaque):
        if (valorSaque > self.getSaldo()):
            print(f'Erro! Você tentou sacar {valorSaque} enquanto sua conta possuí APENAS {self.getSaldo()}')
            print('Vai trabalhar pobre')
        else:
            self.saldo = self.saldo - valorSaque
            print(f'Muito bem, senhor {self.getNome()}, foram sacados {valorSaque} restando {self.getSaldo()}')



nome = 'Pedro Sampaio'
idade = 20

print(f'O seu nome é: {nome}  e sua idade é: {idade}')




