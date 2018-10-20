def exercicio001():
    print('')
    print('')
    print('============ Exercício 1 =============')
    print('')
    print("Mostra um intervalo de números inteiros de 1 a 100.")
    print('')
    i = 0
    while(i<100):
        i += 1
        print(i)
        if(i==100):
            break
    inicio()

def exercicio2():
    print('')
    print('')
    print('============ Exercício 2 =============')
    print('')
    print("É uma evolução do primeiro exercício, do qual você pode escolher os valores do intervalo.")
    print('')
    x = int(input("Digite o inicio da contagem: "))
    y = int(input("Digite o fim da contagem: "))

    if(y<x):
        print("O inicio precisa ser menor que o final")
        exercicio2()

    while(x<y):
        x += 1
        print(x)
        if(x==y):
            break
    inicio()

def exercicio3():
    print('')
    print('')
    print('============ Exercício 3 =============')
    print('')
    print("Mostra uma sequêcia de números no intervalo de 1 a 10 na ordem inversa.")
    print('')
    x = 11
    while(x>0):
        x -= 1
        print(x)
        if(x==1):
            break
    inicio()

def exercicio4():
    print('')
    print('')
    print('============ Exercício 4 =============')
    print('')
    print("Mostra os números pares entre 0 e 100.")
    print('')
    x = 0

    while(x<101):
        x += 1
        if(x%2==0):
            print(x)
    inicio()

def exercicio5():
    print('')
    print('')
    print('============ Exercício 5 =============')
    print('')
    print("Exercício 5: Mostra a soma dos números pares encontrados de 0 a 100.")
    print('')
    x = 0
    y = 0

    while(x<101):
        x += 1
        if(x%2==0):
            y = y + x
        if(x==100):
            print("O somatório dos números de 0 a 100 é ", y)
            break
    inicio()

def exercicio6():
    print('')
    print('')
    # Imprime números primos de 0 a 100
    print('============ Exercício 6 =============')
    print('')
    print('Estes são os números primos de 0 a 100')
    print('')
    # Números primos são divisíveis por 1 e por ele mesmo
    # Ou seja, são divisíveis apenas duas vezes

    x = 0
    y = 0


    while(x <= 100):
        c = 0
        d = 1
        x += 1
        while(d <= 100):
            y = x%d
            d += 1
            if(y == 0):
                c += 1
            if(d == 100):
                break
        if(c == 2):
            print(x)
        if(x == 100):
            break

    inicio()

def exercicio7():
    # Imprimir os números primos em um intervalo determinado pelo usuário
    print('')
    print('')
    print('============ Exercício 7 =============')
    print('Estes são os números primos em um intervalo')
    print('')

    min = int(input('Digite o início do intervalo: '))
    max = int(input('Digite o final do intervalo: '))

    x = min
    y = 0

    while (x <= max):
        c = 0
        d = 1
        x += 1
        while (d <= max):
            y = x % d
            d += 1
            if (y == 0):
                c += 1
            if (d == max):
                break
        if (c == 2):
            print(x)
        if (x == max):
            break
    inicio()


def exercicio8():
    # Imprime um intervalo numérico definido pelo usuário exceto 3 números escolhidos
    print('')
    print('')
    print('============ Exercício 8 =============')
    print('')
    print("Mostra um intervalo numérico definido por você e que permita você escolher 3 números para serem ignorados.")
    print('')
    print('Defina um intervalo e escolha 3 números para não aparecer')
    print('')

    x = int(input('Defina o início do intervalo: '))
    max = int(input('Defina o valor máximo do intervalo: '))
    a = int(input('Defina um número que não deve aparecer: '))
    b = int(input('Defina outro: '))
    c = int(input('Defina o último que não deve aparecer: '))

    while(x <= max):
        x += 1
        if((x != a) and (x != b) and (x != c)):
            print(x)
        if(x > max):
            break
    inicio()

def exercicio9():
    #Imprime uma frase repetidamente até que o usuário tecle "q"
    print('')
    print('')
    print('============ Exercício 9 =============')
    print('Looping')
    print('')
    x = 0
    while(x != "q"):
        print("--- estou em looping ---")
        x = input('Digite uma letra: ')
        if(x == "q"):
            break
    inicio()

def inicio():
    # menu de seleção dos exercíos, menu de ajuda e função de sair do programa
    print('')
    print('')
    print('============ Lista de exercícios ===========')
    print('')
    inicio = input("Digite o número do exercício q deseja ver, 'ajuda' para abrir o menu de ajuda ou 'sair' para sair: ")

    if(inicio == "sair"):
        return 0
    if(inicio == "ajuda"):
        print("")
        print("==== Menu de ajuda ====")
        print('')
        print("Os exercícios estão numerados de 1 a 9, você pode digitar o numero do exercício para vê-lo.")
        print('')
        print("Exercício 1: Mostra um intervalo de números inteiros de 1 a 100.")
        print("Exercício 2: É uma evolução do primeiro exercício, do qual você pode escolher os valores do intervalo.")
        print("Exercício 3: Mostra uma sequêcia de números no intervalo de 1 a 10 na ordem inversa.")
        print("Exercício 4: Mostra os números pares entre 0 e 100.")
        print("Exercício 5: Mostra a soma dos números pares encontrados de 0 a 100.")
        print("Exercício 6: Mostra os números primos de 0 a 100.")
        print('Exercício 7: Mostra os números primos dentro de um intervalo numérico definido por você.')
        print("Exercício 8: Imprime um intervalo numérico definido por você e que permita você escolher 3 números para serem ignorados.")
        print("Exercício 9: Mostra a frase 'Estou em looping' e solicita uma letra, se a letra for 'q' o looping é finalizado.")
        print('')
        print('Digite sair para finalizar o programa')

    if(inicio == "1"):
        exercicio001()
    if(inicio == "2"):
        exercicio2()
    if(inicio == "3"):
        exercicio3()
    if (inicio == "4"):
        exercicio4()
    if (inicio == "5"):
        exercicio5()
    if (inicio == "6"):
        exercicio6()
    if (inicio == "7"):
        exercicio7()
    if (inicio == "8"):
        exercicio8()
    if (inicio == "9"):
        exercicio9()
    else:
        inicio = None
        reset()
        return 0

def reset():
    inicio()

inicio()

