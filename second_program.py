
import time
import os

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
escolha = 1

time.sleep(0.5)



while escolha == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Escolha a operação desejada:\n")
    print("     Adição:           1")
    print("     Subtração:        2")
    print("     Multiplicação:    3")
    print("     Divisão:          4")
    print("     Exponenciação:    5")
    print("     Resto da divisão: 6")
    print("     Divisão inteira:  7")

    operacao = int(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')

    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    elif operacao == 5:
        resultado = num1 ** num2
    elif operacao == 6:
        resultado = num1 % num2 
    else:
        resultado = num1 // num2   


    print("O resultado da operação é: ", resultado)

    print("\n\nDigite 1 para continuar")
    print("Digite 0 para sair")
    escolha = int(input(""))

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    

    while escolha != 0 and escolha != 1:
        print("Escolha inválida!!")
        print("\n\nDigite 1 para continuar")
        print("Digite 0 para sair")
        escolha = int(input(""))
        os.system('cls' if os.name == 'nt' else 'clear')


    


