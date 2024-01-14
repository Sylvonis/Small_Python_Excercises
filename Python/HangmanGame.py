"""

I altered this program in function, so it would be easier to change or edit it later.
I liked how I've done it, so I'm committing anyway

"""
import random


def printNumOfLines(x):
    for i in range(x):
        print()


def wordListMaker(choosenList, listToAppend, minLen = 1):
    while True:
        word = choosenList.readline().strip()
        if len(word) >= minLen:
            listToAppend.append(word)
        if word == "":
            break


def gameStart(wordListToUSe):
    number = random.randint(0, 9999)
    palavra = wordListToUSe[number]
    digitadas = []
    acertos = []
    erros = 0
    printNumOfLines(100)
    while True:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acertos else "."
        print(senha)
        if senha == palavra:
            print("Você acertou!")
            break

        tentativa = input("\nDigite uma letra:").lower().strip()

        while not tentativa.isalpha():
            print("Digite uma LETRA")
            tentativa = input("\nDigite uma letra:").lower().strip()

        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra:
                acertos += tentativa
            else:
                erros += 1
                print("Você errou!")
        print("X==:==\nX  : ")
        print("X  O " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  | "
        elif erros == 3:
            linha2 = " \| "
        elif erros >= 4:
            linha2 = " \|/ "
        print(f"X{linha2}")
        linha3 = ""
        if erros == 5:
            linha3 += " /   "
        elif erros >= 6:
            linha3 += " / \ "
        print(f"X{linha3}")
        print("X\n===========")
        if erros == 6:
            print(f"Enforcado!\nA palavra secreta era {palavra}")
            break


wordList = open(r"wordlist.10000.txt")
listOfWords = []

wordListMaker(wordList, listOfWords, minLen=5)

gameStart(listOfWords)








