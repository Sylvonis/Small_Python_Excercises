LARGURA = 79

def verify():
    return input()

with open("fileReadingText.txt") as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue
        elif linha[0] == ">":
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == "*":
            print(linha[1:].center(LARGURA))
        elif linha[0] == "=":
            [print("=") for __ in range(41)]
        elif linha[0] == ".":
            while input("Stopped. Press ENTER to continue") != '':
                pass
        else:
            print(linha)










