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
            if modificar == str(self.listaProdutos[i].cod)
                self.listaProdutos[i].descricao = input('Digite outra descricao')



    def cadastrar(self):
        cod_informado = int(input('Informe o código do fabricante: '))
        for j in range(len(self.listaFabricantes)):
            if cod_informado == self.listaFabricantes[j].cod_fabricante:
                cod = len(self.listaProdutos)+1
                descricao = input('Informe a descrição do produto: ')
                objeto = self.listaFabricantes[j]
                self.listaProdutos(Produto(cod = cod, descricao=descricao, objeto=objeto ))








    def cadastrar_fabricante(self):
        cod = len(self.listaProdutos)
        objeto =






