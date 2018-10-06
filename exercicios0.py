
def exercicio1():
    x = int(input("Digite um número: "))

    if(x != int(x)):
        print("Não é um número")
        exercicio1()

    if(x>0):
        print("O número é positivo")
        exercicio1()
    else:
        if(x < 0):
            print("O numero é negativo")
            exercicio1()
        else:
            if(x == 0):
                print("O número é 0")
                exercicio1()
            else:
                if(type(x) == str or type(x) == bool):
                    print("Não é um número")
                    exercicio1()

def exercicio2():
    x = int(input("Digite um número: "))

    if((x/2 == int(x/2)) and (x != 0)):
        print("O número é par")
        exercicio2()
    else:
        if(x == 0):
            print("O número é 0")
            exercicio2()
        else:
            print("O número é impar")
            exercicio2()

def exercicio3():
    n = input("Digite um número: ")
    m = input("Digite outro: ")

    if((type(n) != float) or (type(m) != float)):
        print("Digite um número válido")
        exercicio3()
    else:
        if(n > m):
            print(n," é maior que ", m)
            exercicio3()
        if(m > n):
            print(m," é maior que ",n)
            exercicio3()
        if(m == n):
            print(m,"e",n,"são iguais")
            exercicio3()

def inicio():
    inicio = int(input("Digite o número do exercício que deseja ver: "))

    if(inicio == 1):
        exercicio1()
    if(inicio == 2):
        exercicio2()
    if(inicio == 3):
        exercicio3()
inicio()