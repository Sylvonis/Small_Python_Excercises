

frase = input("escolha uma frase para ser repetida")
numero = int(input("quantas vezes você deseja que essa frase seja repetida?"))


def repetir (texto, numero_de_vezes):
    contador = 0
    while numero_de_vezes > contador:
        print(texto)
        contador += 1


repetir(frase, numero)

print("fim")




