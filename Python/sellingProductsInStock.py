"""
Altere o Proograma de forma a solicitar ao usuário o produto e a quantidade
vendida
"""


estoque ={"tomate": [1000, 2.30],
          "alface": [ 500, 0.45],
          "batata": [2001, 1.20],
          "feijão": [ 100, 1.50]}


venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0

print("Vendas:\n")

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto:12}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo


print(f"Custo total: {total:21.2f}\n")

print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
