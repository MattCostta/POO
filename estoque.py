


class Estoque:
    def __init__(self):

        self.listaFabricantes = []
        self.listaFabricantes.append(Fabricante(1, "Dell"))
        self.listaFabricantes.append(Fabricante(2, "AOC"))




        self.listaProdutos = []
        self.listaProdutos.append(Produto(1, 'Notebook', self.listaFabricantes[0]))
        self.listaProdutos.append((2, 'Monitor', 'AOC'))