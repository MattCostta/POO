from uhuhu import Produtos

class Lista:
    def __init__(self):
        self.listaProdutos = []



    def salvar_produtos(self):
        self.listaProdutos.append(Produtos())


    def listar_produtos(self):
        for i in range(len(self.listaProdutos[i])):
            print('Cod:', self.listaProdutos[i].cod,
                  'Descricao:', self.listaProdutos[i].descricao,
                  'Fabricante', self.listaProdutos[i].fabricante,
                  'Quantidade:', self.listaProdutos[i].quantidade)

    def alterar(self):
        modificar = input("Informe o código do produto")
        for i in range(len(self.listaProdutos)):
            if modificar == self.listaProdutos[i].cod
                self.listaProdutos[i].descricao = input('Digite outra descricao')


















