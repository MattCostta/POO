from ahuhuh import *

class Final:
    def __init__(self):
        lista = Lista()

        while True:
            entrada = input('1 - Cadastrar produto \n 2 - Listar todos os produtos \n 3 - Procurar produto \n 4 - Alterar produto \n 0 - Sair')
            if entrada == '1':
                lista.salvar_produtos()
            elif entrada == '2':
                lista.listar_produtos()
            #elif entrada == '3':

            elif entrada == '4':
                lista.alterar()
            elif entrada == '0':
                break
            else:
                print('Opção inválida!')

