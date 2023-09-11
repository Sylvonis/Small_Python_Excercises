

inputtext = input("digite algo para ser repetido")
number = int(input("quantas vezes você deseja que essa frase seja repetida?"))


def repetir (text, xtimes):
    i = 0
    while xtimes > i:
        print(text)
        i += 1


repetir(inputtext, number)

print("end")




