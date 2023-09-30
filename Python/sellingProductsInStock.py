"""
Altere o Programa de forma a solicitar ao usuário o produto e a quantidade
vendida

the things that I didin't code in this program are the ones with a '# ***' beside it
"""

estoque = {"tomate": [1000, 2.30],  # ***
           "alface": [500, 0.45],  # ***
           "batata": [2000, 1.20],  # ***
           "feijão": [100, 1.50]}  # ***

produtos_compra = []


def produto():
    produto_escolhido = None
    quant_escolhida = None
    stop = 0

    while True:
        produto_escolhido= input('Escolha o produto que quer comprar:\n').lower()
        if produto_escolhido in estoque:
            break
        else:
            print('Este Produto não existe em nosso estoque\n')

    while True:
        try:
            quant_escolhida = int(input('escolha a quantidade que quer comprar. 0 para sair\n'))
            if quant_escolhida == 0:
                break
            for value in estoque:
                if [produto_escolhido] == [value]:
                    if quant_escolhida <= int(estoque[value][0]):
                        produtos_compra.append([produto_escolhido, quant_escolhida])
                        return False
                    elif quant_escolhida > int(estoque[value][0]):
                        print('não temos essa quantidade de ' + f'{produto_escolhido}\n')
        except:
            pass


def compra(escolha_produto):
    print("Vendas:\n")  # ***
    total = 0  # ***

    for operacao in escolha_produto:  # ***
        [produt, quantidade] = operacao  # ***
        preco = estoque[produt][1]  # ***
        custo = preco * quantidade  # ***
        print(f"{produt:12}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")  # ***
        estoque[produt][0] -= quantidade  # ***
        total += custo  # ***

    print(f"Custo total : {total:21.2f}\n")  # ***


def mostrarEstoque():
    print("Estoque:\n")  # ***
    max_len = len(max(estoque.keys()))

    for chave, dados in estoque.items():  # ***
        print("Descrição:".ljust(11), chave.rjust(max_len))
        print("Quantidade:".ljust(11), str(dados[0]).rjust(max_len))
        print("Preço:".ljust(11), f"{dados[1]:6.2f}\n".rjust(max_len))


while True:
    input_Char = input("Insira E para verificar o estoque, C para comprar e S para sair\n").upper()
    if input_Char == 'E':
        mostrarEstoque()

    if input_Char == 'C':
        produto()
        compra(produtos_compra)

    if input_Char == 'S':
        break

