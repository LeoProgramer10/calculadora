# Importa as bibliotecas "time" e "os"
import time   # Usada para criar pausas no programa (sleep)
import os     # Usada para interagir com o sistema operacional (limpar tela, etc.)

# Solicita os dois números do usuário
num1 = int(input("Digite o primeiro número:"))  # Armazena o primeiro número
num2 = int(input("Digite o segundo número:"))   # Armazena o segundo número

escolha = 1  # Variável de controle de fluxo (1 = continuar, 0 = sair)

# Pausa o programa por 0,5 segundos antes de começar
time.sleep(0.5)

# Loop principal do programa, só para quando escolha for igual a 0
while escolha == 1:
    # Limpa a tela antes de mostrar o menu
    os.system('cls' if os.name == 'nt' else 'clear')

    # Exibe o menu de operações disponíveis
    print("Escolha a operação desejada:\n")
    print("     Adição:           1")
    print("     Subtração:        2")
    print("     Multiplicação:    3")
    print("     Divisão:          4")
    print("     Exponenciação:    5")
    print("     Resto da divisão: 6")
    print("     Divisão inteira:  7")

    # Recebe a escolha do usuário
    operacao = int(input(""))

    # Limpa a tela novamente após a escolha
    os.system('cls' if os.name == 'nt' else 'clear')

    # Estrutura condicional para realizar a operação escolhida
    if operacao == 1:          # Adição
        resultado = num1 + num2
    elif operacao == 2:        # Subtração
        resultado = num1 - num2
    elif operacao == 3:        # Multiplicação
        resultado = num1 * num2
    elif operacao == 4:        # Divisão
        resultado = num1 / num2
    elif operacao == 5:        # Exponenciação (potenciação)
        resultado = num1 ** num2
    elif operacao == 6:        # Resto da divisão
        resultado = num1 % num2 
    else:                      # Divisão inteira (caso o número digitado seja diferente de 1–6)
        resultado = num1 // num2   

    # Mostra o resultado da operação
    print("O resultado da operação é: ", resultado)

    # Pergunta ao usuário se deseja continuar ou sair
    print("\n\nDigite 1 para continuar")
    print("Digite 0 para sair")
    escolha = int(input(""))

    # Aguarda 1 segundo antes de prosseguir
    time.sleep(1)

    # Limpa a tela novamente após a escolha
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Caso o usuário digite um valor inválido (diferente de 0 ou 1), força ele a escolher de novo
    while escolha != 0 and escolha != 1:
        print("Escolha inválida!!")
        print("\n\nDigite 1 para continuar")
        print("Digite 0 para sair")
        escolha = int(input(""))
        os.system('cls' if os.name == 'nt' else 'clear')
