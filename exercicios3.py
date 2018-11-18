#!/usr/bin/python3
# coding: utf-8

# author: Guilherme Isaías Silva

# Exercícios de funções

def exercicio1():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 1 ==============================")
    print('')
    print(" Exibe a frase 'Estamos esutdando funções ")
    print("")
    # Função que quando executada imprime a frase "Estamos estudando funções"
    def estudo():
        # Exibe a string
        print('Estamos estudando funções')
        # Retorna dizendo que ocorreu tudo bem
        return 0
    # Invoca a função estudo()
    estudo()
    # Retorna dizendo que ocorreu tudo bem
    return 0

def exercicio2():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 2 ==============================")
    print('')
    print(" Contém uma função que receberá um número por parâmetro digitado pelo usuário e que será exibido por ela ")
    print("")
    # Função que exibe o resultado do exercício
    def estudo(n):
        # Exibe o resultado
        print("Função invocada com sucesso. O valor passado pelo argumento 'x' é", n)
        return 0
    # Loop infinito
    while True:
        # Tenta executar a entrada de um número e sua conversão de string para inteiro
        try:
            x = int(input("Digite um número para ser passado como parâmtero: "))
            print('\n')
            estudo(x)
            break
        # Se a tentativa der errado diz para o usuário digitar apenas números, porque o que não for número não será possível converter
        except:
            print("\n")
            print(" ======= Digite apenas números inteiros! =======")
            print("\n")
    return 0

def exercicio3():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 3 ==============================")
    print('')
    print(" Recebe dois números e mostra a soma entre os dois valores ")
    print("")
    # Função que soma as variáveis que o usuário informou e exibe o resultado
    def soma(x, y):
        soma = x + y
        print("A soma dos dois números é ", soma)
        return 0
    ''' Loop infinito que tentar receber duas variáveis informadas pelo usuário e converte-las para um valor inteiro, se der errado exibe para o usuário digitar apenas números,
    uma vez que digitado algo diferente de um número inteiro ocorre um erro ao converter.'''
    while True:
        try:
            x = int(input("Digite o primeiro número: "))
            y = int(input("Digite o segundo número: "))
            soma(x, y)
            break
        except:
            print("Digite apenas números inteiros")
    return 0

def exercicio4():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 4 ==============================")
    print('')
    print(" Recebe 3 números, mostra eles em ordem crescente e a média aritmética ")
    print("")
    # Função que ordena e exibe as variáveis informadas pelo usuário de forma crescente
    def ordemMedia(x, y, z):
        lista = [x, y, z]
        ordem = sorted(lista)
        print("\nA ordem é: \n")
        print(ordem[0],";", ordem[1],";", ordem[2])
        print("\n")
        media = (x + y + z)/3
        print("A média é: ", media)
        print("\n")
        return 0
    # Função que exibe a entrada para o primeiro número informado pelo usuário
    def recebeA():
        try:
            a = int(input("Digite o primeiro número: "))
            recebeB(a)
            return 0
        except:
            print("\n ===== Digite apenas números inteiros! =======\n")
            recebeA()
            return 1
    # Função que exibe a entrada para o segundo número informado pelo usuário
    def recebeB(a):
        try:
            b = int(input("Digite o segundo número: "))
            recebeC(a, b)
            return 0
        except:
            print("\n ===== Digite apenas números inteiros! =======\n")
            recebeB(a)
            return 1
    # Função que exibe a entrada para o último número informado pelo usuário
    def recebeC(a, b):
        try:
             c = int(input("Digite o último número: "))
             ordemMedia(a, b, c)
             return 0
        except:
            print("\n ===== Digite apenas números inteiros! =======\n")
            recebeC(a, b)
            return 1

    recebeA()
    return 0

def exercicio5():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 5 ==============================")
    print('')
    print(" Recebe 2 parâmetros, um é obrigatório e o outro é facultativo, depois os exibe ")
    print("")
    # Função que exibe os parâmetros informados pelo usuário
    def func(x, ind = 0):
        print('\nOs parametros são: ','"' + x +'"', 'e','"'+ str(ind) +'"','\n')
        return 0
    ''' Loop infinito que tenta capturar parâmetros informados pelo usuário, até que ele digite um parâmetro vazio
    e exiba o resultado, se der errado ele informa o usuário e reinicia.'''
    while True:
        try:
            x = input("Digite um parametro: ")
            ind = input("Digite opcionalmente mais um parametro: ")
            if(ind != ''):
                func(x, ind)
            else:
                func(x)
            break
        except:
            print("Erro")
    return 0

def exercicio6():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 6 ==============================")
    print('')
    print(" Recebe 2 números e mostra sua soma ")
    print("")
    '''Loop infinito que tenta receber dois números inteiros do usuário, se for digitado algo
    diferente de inteiro ele tenta novamente até que seja digitado'''
    while True:
        try:
            x = int(input("Digite um número para ser somado: "))
            y = int(input("Digite mais um: "))
            break
        except:
            print("Erro! Digite apenas números inteiros!")

    # Função que retorna a soma dos parâmetros informados pelo usuário
    def func2(a, b):
        soma = a + b
        return soma
    # Comando para exibir o resultado da soma
    print('A soma de', x, 'e', y, 'é: ', func2(x, y))

def exercicio7():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 7 ==============================")
    print('')
    print(" Recebe uma quantidade variável de parâmetros e os exibe ")
    print("")
    # Declaração de variáveis utilizadas no exercício
    var = 0
    lista = []
    lista2 = []
    x = 0
    # Função que exibe a lista desempacotada para o usuáirio caso seja mais de 1
    def func0(lista):
        print("\nOs parâmetros digitado são: ")
        print(*lista)
        return lista

    # Função que exibe a lista desempacotada para o usuáirio caso seja menos de 1 ou 0
    def func1(y, lista2):
        if(y == 1):
            lista2 = [lista2[0] + '.']
            print('\nO parâmtro digitedo é: \n', *lista2)
            return 0
        if(y == 0):
            print('\n O parâmetro está vazio\n')
            return 0

    '''Loop infinito que tenta capturar um parâmetro informado pelo usuário até que 
    ele digite um parâmetro vazio, insere os parâmtros em uma lista e envia para a func1() ou func0()
    exibirem de aconrdo com a quantidade de parâmetros informados, se der erro será informado ao usuário e 
    reiniciará o programa.'''
    while True:
        try:
            while (var != ''):
                var = input("Digite um parâmetro: ")
                if(var == ''):
                    if(x <= 1):
                        func1(x, lista2)
                        break
                    if(x >= 2):
                        del lista[-1]
                        del lista[-1]
                        lista = lista + [lista2[-2] + ' e']
                        lista = lista + [lista2[-1] + '.']
                        func0(lista)
                        break
                x += 1
                lista2 = lista2 + [var]
                lista = lista + [var + ',']
            if(var == ''):
                break

        except:
            print("\n\n##########################################\n "
                  "################  ERRO! #################\n"
                  "###########################################\n")
            exercicio7()
    return 0

def exercicio8():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 8 ==============================")
    print('')
    print(" Recebe uma quantidade variável de parâmetros, associa a uma chave e os exibe. ")
    print("")

    dic = {}
    z = 0
    x = 0

    # Função qu exibe os parãmtros informados pelo usuário e sua respectiva chave
    def imprime(dicionario):
        print('')
        print('')
        print('')
        print('Os parâmetros com suas respectivas chaves são: ')
        print('')
        print('')
        for i in dicionario:
            print(str(i) + ':', dicionario[i] + ';')
        return 0

    ''' Loop que captura parâmetros informados pelo usuário e os insere em um dicionário vinculando a uma chave ordenada
     e envia para a função imprime para ser exibida para o usuário'''
    while(x != ''):
        x = input("Digite um parâmetro: ")
        if(x == ''):
            imprime(dic)
            break
        dic[z] = x
        z += 1
    return 0

def exercicio9():

    print('')
    print('')
    print('')
    print(" =============================== Exercício 9 ==============================")
    print('')
    print(" Transfere os valores de uma lista para uma função desdempacotados e exibe sua soma. ")
    print("")

    def func(a, b, c, d):
        print(a + b + c + d)

    lista = [1, 2, 3, 4]

    func(*lista)

    return 0

def exercicio10():

    print('')
    print('')
    print('')
    print(" =============================== Exercício 9 ==============================")
    print('')
    print(" Recebe 3 números e exibe o maior. ")
    print("")

    def recebe1():
        # Função que captura um parâmtro informado pelo usuário e converte em um valor inteiro
        # Se der errado será pedido ao usuário que digite apenas números e tentará novamente
        try:
            lista1 = [int(input('Digite o primeiro número: '))]
            recebe2(lista1)
            return 0
        except:
            print('\n ======= Digite apenas números! =======\n')
            recebe1()
            return 1
    def recebe2(lista2):
        # Função que captura um parâmtro informado pelo usuário e converte em um valor inteiro
        # Se der errado será pedido ao usuário que digite apenas números e tentará novamente
        try:
            lista = lista2 + [int(input('Digite o segundo número: '))]
            recebe3(lista)
            return 0
        except:
            print('\n ======= Digite apenas números! =======\n')
            lista = lista2
            recebe2(lista)
            return 1
    def recebe3(lista3):
        # Função que captura um parâmtro informado pelo usuário e converte em um valor inteiro
        # Se der errado será pedido ao usuário que digite apenas números e tentará novamente
        try:
            lista = lista3 + [int(input('Digite o último número: '))]
            organiza(lista)
            return 0
        except:
            print('\n ======= Digite apenas números! =======\n')
            lista = lista3
            recebe3(lista)
            return 1
    def organiza(lista):
        # Função que organiza os parâmtros informados pelo usuário de forma crescente e envia para a função seleciona()
        try:
            listaOrdenada = sorted(lista)
            seleciona(listaOrdenada)
            return 0
        except:
            print('Erro ao ordernar lista!')
            return 1
    def seleciona(listaOrdenada):
        # Seleciona o maior número da lista e envia para a função exibe()
        try:
            maior = listaOrdenada[2]
            exibe(maior)
            return 0
        except:
            print('Erro ao selecionar o maior número!')
            return 1
    def exibe(maior):
        # Exibe o resultado para o usuário
        try:
            print('\n\nO maior número digitado foi o "' + str(maior) + '".')
            return 0
        except:
            print('Erro ao exibir o valor!')
            return 1
    recebe1()
    return 0

def exercicio11():
    print('')
    print('')
    print('')
    print(" =============================== Exercício 11 ==============================")
    print('')
    print(" Recebe números, os insere em uma lista e soma os valores. ")
    print("")

    n = 0
    def recebe(n):
        # recebe um parâmetro informado pelo usuário e envia para a função converteNumero()
        numero = 0
        try:
            while(numero != ''):
                if(n == 0):
                    numero = input('Digite um número ou pressione enter para exibir a soma: ')
                    converteNumero(numero)
                else:
                    numero = input('Digite outro número ou pressione enter para exibir a soma: ')
                    converteNumero(numero)
                n += 1
        except:
            print('\n ===== Erro ao capturar número =====\n')
            recebe(n)
            return 1

    def converteNumero(numero):
        # Converte o parâmtro recebido para um número inteiro, ser der errado pede para o usuário digitar apenas números inteiros
        # Se der certo envia o número convertido para a função insereNumero()
        if(numero != ''):
            try:
                numeroInteiro = int(numero)
                insereNumero(numeroInteiro)
            except:
                print('\n======= Digite apenas números! ======\n')
                recebe()
                return 1
        else:
            soma(lista)
            return 0

    lista = []
    def insereNumero(numeroInteiro):
        # Insere o número recebido em uma lista e envia para função soma()
        try:
            lista.append(numeroInteiro)
            return lista
        except:
            print('\n ===== Erro ao inserir valor na lista =====\n')

    def soma(lista):
        # Soma os valores da lista e envia o resultado para a função exibe()
        try:
            soma = sum(lista)
            exibe(soma)
            return soma
        except:
            print('\n ===== Erro somar lista =====\n')

    def exibe(soma):
        # Exibe o resultado da soma recebido
        try:
            print('\n\nA soma dos valores é "' + str(soma) + '".\n\n')
            return 0
        except:
            print('\n ===== Erro ao exibir soma =====\n')

    recebe(n)

def exercicio12(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício",num,"==============================")
    print('')
    print(" Recebe números, os insere em uma lista, multiplica os valores e exibe o resultado. ")
    print("")

    n = 0

    def recebe(n):
        # Recebe os parâmetros digitados pelo usuário e envia para a função converteNumero()
        # Se o usuário não digitou nenhum parâmtro ainda ele diz para digitar o primeiro
        # Se o usuário já digitou algum parâmtro ele pede para digitar outro
        numero = 0
        try:
            while (numero != ''):
                if (n == 0):
                    numero = input('Digite um número ou pressione enter para exibir a multiplicação: ')
                    converteNumero(numero)
                else:
                    numero = input('Digite outro número ou pressione enter para exibir a multiplicação: ')
                    converteNumero(numero)
                n += 1
                if(numero == ''):
                    return 0
        except:
            print('\n ===== Erro ao capturar número =====\n')
            recebe(n)
            return 1

    def converteNumero(numero):
        # Recebe um número como string e converte para inteiro e envia para a função insereNumero()
        # Se não for um número pede para o usuário digitar apenas números e retorna para a função recebe()
        # Se o parâmetro for vazio ele envia a lista retornada por insereNumero() para a função multiplicacao()
        if (numero != ''):
            try:
                numeroInteiro = int(numero)
                insereNumero(numeroInteiro)
            except:
                print('\n======= Digite apenas números! ======\n')
                recebe()
                return 1
        else:
            multiplicacao(lista)
            return 0

    lista = []

    def insereNumero(numeroInteiro):
        # Insere os números recebidos em uma lista e retorna com o resultado
        try:
            lista.append(numeroInteiro)
            return lista
        except:
            print('\n ===== Erro ao inserir valor na lista =====\n')

    def multiplicacao(lista):
        # Multiplica os valores de uma lista e envia o resultado para a função exibe()
        try:
            multiplicacao = 1
            for i in lista:
                multiplicacao = multiplicacao * i
            exibe(multiplicacao)
            return multiplicacao
        except:
            print('\n ===== Erro somar lista =====\n')

    def exibe(multiplicacao):
        # Exibe o resultado da multiplicação
        try:
            print('\n\nA multiplicacao dos valores é "' + str(multiplicacao) + '".\n\n')
            return 0
        except:
            print('\n ===== Erro ao exibir multiplicacao =====\n')

    recebe(n)

def exercicio13(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Recebe uma palavra, transforma em uma lista, inverte e exibe. ")
    print("")

    def recebe():
        # Recebe uma palavra informada pelo usuário e envia para a função transforma()
        try:
            palavra = input('\nDigite uma palavra para ser invertida: ')
        except:
            print('\n ===== Erro ao capturar palavra! ======\n'
                  '=========== Digite novamente!=========')
            recebe()
            return 1
        transforma(palavra)
        return 0

    def transforma(palavra):
        # Transforma uma string em uma lista e envia a lista para a função inverte()
        try:
            lista = []
            for i in palavra:
                lista = lista +[i]
            inverte(lista)
            return 0
        except:
            print('\n ====== Erro ao transformar em lista! ====== \n')
            print('\n ====== Digite novamente! ====== \n')
            recebe()
            return 2

    def inverte(lista):
        # Inverte a lista recebida e envia para a função retornaString()
        try:
            a = 0
            listaInvertida = []
            while(-a < len(lista)):
                a -= 1
                listaInvertida.append(lista[a])
                if(-a > len(lista)):
                    break
            retornaString(listaInvertida)
            return 0
        except:
            print('\n ====== Erro ao inverter em lista! ====== \n')
            print('\n ====== Digite novamente! ====== \n')
            recebe()
            return 2

    def retornaString(listaInvertida):
        # Tansforma a lista recebida em string e envia para a função exibe()
        try:
            stringInvertida = ''
            for i in listaInvertida:
                stringInvertida = stringInvertida + i
            exibe(stringInvertida)
            return 0
        except:
            print('\n ====== Erro ao transformar em string! ====== \n')
            print('\n ====== Digite novamente! ====== \n')
            recebe()
            return 2

    def exibe(stringInvertida):
        # Constroi um texto com o resultado do programa e exibe para o usuário
        try:
            print('\n A palavra se transformou em "' + stringInvertida +'".\n')
            return 0
        except:
            print('\n ====== Erro ao exibir palavra ====== \n')
            print('\n ====== Digite novamente ====== \n')
            recebe()
            return 2
    recebe()


def exercicio14(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Recebe um número e calcula seu fatorial. ")
    print("")

    def recebe():
        # Recebe os parâmtros informados pelo usuário e envia para a função converte()
        # Se ele não tiver digitado nenhum parâmtro é pedido para digitar o primeiro
        # Se ja foi digitado algúm parâmtro é pedido para digitar mais um
        try:
            numero = input('\n Digite um número para ser calculado seu fatorial:')
            converte(numero)
            return 0
        except:
            print('\n ==== Erro ao capturar número, digite novamente! ===== \n')
            recebe()
            return 1

    def converte(numero):
        # Converte um número recebido como string em inteiro
        # Se não tiver recebido um número é pedido para o usuário para digitar apenas números
        try:
            inteiro = int(numero)
            fatorial(inteiro)
            return 0
        except:
            print('\n ==== Erro ao converter número, digite apenas números! ===== \n')
            recebe()
            return 1

    def fatorial(inteiro):
        # Calcula o fatorial do número recebido e envia o resultado para a função exibir()
        try:
            fatorial = 1
            if(inteiro != 0):
                for i in range(inteiro):
                    if(i == 0):
                        i += 1
                    fatorial = fatorial * i
            else:
                fatorial = 0
            exibir(fatorial, inteiro)
            return 0
        except:
            print('\n ==== Erro ao calcular fatorial, digite novamente! ===== \n')
            recebe()
            return 1

    def exibir(fatorial, inteiro):
        # Exibe o resultado do fatorial recebido
        try:
            print('\n O fatorial de', str(inteiro), 'é', str(fatorial)+'.')
            return 0
        except:
            print('\n ==== Erro ao exibit número, digite novamente! ===== \n')
            recebe()
            return 1

    recebe()



def exercicio15(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Verifica se o número informado pertence à um intervalo informado ")
    print("")

    def recebeInicioIntervalo():
        # Recebe o inicio do intervalo informado pelo usuário e envia para a função converte()
        # Armazena o retorno da função converte() na variável inicioConvertido
        # Insere como 1º parâmrtro de um a lista e a envia para a função recebeIntervalo()
        try:
            inicio = input('\n Digite o inicio do intervalo: ')
            inicioConvertido = converte(inicio)
            lista = [inicioConvertido]
            recebeFinalIntervalo(lista)
            return 0
        except:
            print('\n ===== Erro ao capturar inicio do intervalo ===== \n')
            return 1

    def recebeFinalIntervalo(lista):
        # Recebe o final do intervalo e envia para a função converte()
        # Armazena o retorno da função converte() na variável fimConvertido
        # Insere a variável fimConvertido no 2º parâmtro da lista e envia para a função recebeNumero()
        try:
            fim = input('\n Digite o final do intervalo: ')
            fimConvertido = converte(fim)
            lista = lista + [fimConvertido]
            recebeNumero(lista)
            return 0
        except:
            print('\n ===== Erro ao capturar fim do intervalo ===== \n')
            return 1

    def recebeNumero(lista):
        # Recebe o valor a ser conferido e envia para a função converte()
        # Armazena o retorno da função converte() na variável numeroConvertido
        # Insere a variável numeroConvertido no 3º parâmtro da lista e envia para a função recebeNumero()
        try:
            numero = input('\n Digite o valor a ser conferido: ')
            numeroConvertido = converte(numero)
            lista = lista + [numeroConvertido]
            confere(lista)
            return 0
        except:
            print('\n ===== Erro ao capturar valor ===== \n')
            return 1

    def converte(valor):
        # Converte um número de string para inteiro e retorna seu valor
        # Se o valor não for um número é pedido ao usuário para digitar apenas números
        try:
            inteiro = int(valor)
            return inteiro
        except:
            print('\n ===== Erro ao converter número ===== \n')
            return 1

    def confere(lista):
        # Varifica se o inicio da lista é maior que o final e organiza o menor antes
        # Verifica se o valor está dentro do intervalo
        # Se o valor não esiver os parâmtros são enviados para a função exibeNao()
        # Se o valor estiver fora do intervalo os parâmtros são enviados para a função exibe()
        try:
            if(lista[0] < lista[1]):
                if(lista[0] <= lista[2] <= lista[1]):
                    exibe(lista[0], lista[1], lista[2])
                    return 0
                else:
                    exibeNao(lista[0], lista[1], lista[2])
                    return 0
            if(lista[1] < lista[0]):
                if (lista[1] <= lista[2] <= lista[0]):
                    exibe(lista[1], lista[0], lista[2])
                else:
                    exibeNao(lista[1], lista[0], lista[2])
                    return 0
            if(lista[0] ==  lista[1]):
                if(lista[0] == lista[2]):
                    exibe(lista[0], lista[1], lista[2])
                    return 0
                else:
                    exibeNao(lista[0], lista[1], lista[2])
                    return 0
        except:
            print('\n ===== Erro ao comparar os valores ===== \n')
            return 1

    def exibe(menor, maior, valor):
        # Exibe que o valor está incluso no intervalo
        try:
            print('\n O valor', str(valor), 'está contido no intervalo de', str(menor), 'a', str(maior) + '.')
        except:
            print('\n ===== Erro ao exibir resultado ===== \n')
            return 1

    def exibeNao(menor, maior, valor):
        # Exibe que o valor não está incluso no intervalo
        try:
            print('\n O valor', str(valor), 'não está contido no intervalo de', str(menor), 'a', str(maior) + '.')
        except:
            print('\n ===== Erro ao exibir resultado ===== \n')
            return 1

    recebeInicioIntervalo()
    return 0

def exercicio16(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Verifica a quantidade de letras maiusculas e minusculas em uma expressão ")
    print("")

    def recebe():
        # Recebe a uma expressão informada pelo usuário e envia para a função transformaEmLista()
        try:
            expressao = input('\nDigite uma expressão para calcular o número de letras maiusculas e minusculas: ')
            transformaEmLista(expressao)
            return 0
        except:
            print('\n ====== Erro ao receber expressão, digite novamente! ========\n')
            recebe()
            return 1

    def transformaEmLista(expressao):
        # Recebe uma string, transforma em uma lista e a envia para a função conta()
        try:
            lista = []
            for i in expressao:
                lista.append(i)
            conta(lista)
            return 0
        except:
            print('\n ======= Erro ao transformar expressão, digite novamente! =======\n')
            recebe()
            return 1

    def conta(lista):
        # Recebe uma lista, conta o número de letras maiusculas e minusculas e envia o resultado para a função exibe()
        try:
            maiuscula = 0
            minuscula = 0
            for i in lista:
                if(i.isupper()):
                    maiuscula += 1
                elif(i.islower()):
                    minuscula += 1
            exibe(maiuscula, minuscula)
            return 0
        except:
            print('\n ======= Erro ao contar letras, digite novamente! =======\n')
            recebe()
            return 1

    def exibe(maiuscula, minuscula):
        # Constroi o texto a ser exibido de acordo com a quantidade de letras maiusculas e minusculas e exibe
        try:
            letra1 = ''
            letra2 = ''
            maius = ''
            minus = ''
            nao = ' '
            if(maiuscula <= 1):
                letra2 = 'letra'
                maius = 'maiuscula'
                if (maiuscula == 0):
                    maiuscula = 'nenhuma'
            elif(maiuscula > 1):
                letra2 = 'letras'
                maius = 'maiusculas'
            if(minuscula <= 1):
                letra1 = 'letra'
                minus = 'minuscula'
                if (minuscula == 0):
                    minuscula = 'nenhuma'
                    nao = ' não '
            elif(minuscula > 1):
                letra1 = 'letras'
                minus = 'minusculas'


            print('\n A expressão informada'+ nao + 'contém', str(minuscula), letra1, minus, 'e', str(maiuscula), letra2, maius + '.')
            return 0
        except:
            print('\n ====== Não foi possível exibir o resultado, tende novamente ======== \n')
            recebe()
            return 1
    recebe()


def exercicio17(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Recebe valores, insere em uma lista se não estiver repetido e a exibe. ")
    print("")


    def guia():
        # Guia a execução do programa
        valor = 0
        x = 0
        lista = []
        while(valor != ''): # Pede para receber um valor até que seja nulo
            valor = recebe(x) # Armazena o valor informado
            conferido = confere(valor) # Envia o valor para ser conferido
            lista = insere(valor, conferido, lista) # Insere o valor em uma lista
            if(valor == ''):
                break
            x += 1
        listaFiltrada = filtro(lista) # Envia a lista para ser filtrada
        textoMontado = montaTexto(listaFiltrada) # Monta um texto de acordo com os valores da lista
        exibe(textoMontado) # Exibe o texto
        return 0

    def recebe(x):
        # Pede ao usuário para informar um parâmetro e retorna o valor
        try:
            if(x == 0):
                valor = input('\nDigite um parâmetro para inserir a lista, ou enter para concluir: ')
            else:
                valor = input('\nDigite mais um parâmetro para inserir a lista ou enter para concluir: ')
            return valor
        except:
            print('\n===== Erro ao capturar valor! Digite novamente! =====\n')
            return 1

    def confere(valor):
        # Confere se o valor informado está vazio
        try:
            if(valor == ''):
                return 'vazio'
            if(valor == 1):
                guia()
                return 1
            else:
                return 'preenchido'
        except:
            print('\n===== Erro ao conferir valor! Digite novamente! =====\n')
            guia()
            return 1

    def insere(valor, conferido, lista):
        # Insere os valores não vazios e sem erro em uma lista e a retorna
        try:
            if(conferido == 'vazio'):
                return lista
            if(conferido == 1):
                return 1
            else:
                lista.append(valor)
                return lista
        except:
            print('\n===== Erro ao gerar lista! Digite novamente! =====\n')
            guia()
            return 1

    def filtro(lista):
        # Recebe uma lista e retorna outra sem números repetidos
        try:
            listaFiltrada = []
            for i in lista:
                x = 0
                for n in listaFiltrada:
                    if(i == n):
                        x = 1
                if(x == 0):
                     listaFiltrada.append(i)
            return listaFiltrada
        except:
            print('\n===== Erro ao filtrar lista! Digite novamente! =====\n')
            guia()
            return 1

    def montaTexto(listaFiltrada):
        # Retorna um texto montado a partir de uma lista recebida
        try:
            if(listaFiltrada == []):
                textoMontado = '\nA lista está vazia'
            if(len(listaFiltrada) == 1):
                textoMontado = '\nA nova lista retornou com o parâmetro "' + str(listaFiltrada[0]) + '".\n'
            elif(len(listaFiltrada) > 1):
                textoMontado = '\nA nova lista retornou com ' + str(len(listaFiltrada)) + ' parâmtros: '
                for i in listaFiltrada:
                    if(listaFiltrada[len(listaFiltrada) - 2] == i):
                        textoMontado = textoMontado + str(i) + ' e '
                    if(listaFiltrada[-1] == i):
                        textoMontado = textoMontado + str(i) + '.\n'
                    elif(i != listaFiltrada[-1] and i != listaFiltrada[len(listaFiltrada) - 2]):
                        textoMontado = textoMontado + str(i) + ', '
            return textoMontado
        except:
            print('\n===== Erro ao montar texto! Digite novamente! =====\n')
            guia()
            return 1

    def exibe(texto):
        # Exibe o texto recebido
        try:
            print(texto)
            return 0
        except:
            print('\n===== Erro ao exibir texto! Digite novamente! =====\n')
            guia()
            return 1

    guia()


def exercicio18(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Recebe valores e imprime os números primos contidos. ")
    print("")

    def main():
        # Guia a execução do programa

        lista = recebe() # Armazena a lista de parâmtros informados pelo usuário

        listaNumerica = confere(lista) # Envia a lista para conferir quais são núemros

        listaInteira = converte(listaNumerica) # Envia os números para serem convertidos em inteiro e os armazena

        listaPrimo = seleciona(listaInteira) # Envia os núemeros para serem selecionados os primos

        semRepetir = tiraRepetidos(listaPrimo) # Envia os números primos para controlar os repetidos

        texto = constroiTexto(semRepetir) # Envia os números primos para construir o texto de saída

        print(texto) # Exibe o texto


    def recebe():
        # Recebe parâmtros informados pelo usuário
        while True:
            try:
                lista = list()
                valor = 0
                while(valor != ''):
                    x = 0
                    if(x == 0):
                        valor = input('\nDigite um parâmtro para ser conferido: ')
                        x += 1
                    else:
                        valor = input('\nDigite mais um ou pressione enter para ver o resultado: ')
                    if(valor == ''):
                        break
                    insere(valor, lista)
                return lista
            except:
                print('\n ======== Erro ao capturar valor! =========\n'
                      '\n =========== Digite novamente!=============\n')

    def insere(valor, lista):
        # Insere os valores recebidos em uma lista
        try:
            lista += [valor]
            return lista
        except:
            print('\n ======== Erro ao inserir valor a lista! =========\n'
                  '\n =========== Digite novamente!=============\n')
            recebe()
            return 1

    def confere(lista):
        # Separa as strings numéricas
        listaNumerica = []
        try:
            for i in lista:
                if(i.isdigit()):
                    insere(i, listaNumerica)
            return listaNumerica
        except:
            print('\n ======== Erro ao conferir lista! =========\n'
                  '\n =========== Digite novamente!=============\n')
            main()
            return 1

    def converte(listaNumerica):
        # Converte uma lista de strings em uma lista de valores inteiros
        try:
            listaInteira = []
            for i in listaNumerica:
                inteiro = int(i)
                insere(inteiro, listaInteira)
            return listaInteira
        except:
            print('\n ======== Erro ao converter lista! =========\n'
                  '\n =========== Digite novamente!=============\n')
            main()
            return 1

    def seleciona(listaInteira):
        # Seleciona os números primos de uma lista
        try:
            listaPrimos = []
            for i in listaInteira:
                n = 0
                x = 0
                while(n <= i):
                    n += 1
                    if(i%n == 0):
                        x += 1
                if(x == 2):
                    listaPrimos = insere(i, listaPrimos)
            return listaPrimos
        except:
            print('\n ======== Erro ao selecionar numeros primos! =========\n'
                  '\n =========== Digite novamente!=============\n')
            main()
            return 1

    def tiraRepetidos(listaPrimos):
        # Verifica os números repetidos e vincula a quantidade de vezes ele é exibido
        try:
            semRepetir = {}
            for i in listaPrimos:
                x = 0
                if(i not in semRepetir):
                    for n in listaPrimos:
                        if(i == n):
                            x += 1
                    semRepetir[i] = x
            return semRepetir
        except:
            print('\n ======== Erro ao controlar numeros repetidos! =========\n'
                  '\n =========== Digite novamente!=============\n')
            main()
            return 1

    def constroiTexto(semRepetir):
        # Constroi um texto com o resultado do programa
        try:
            if(len(semRepetir) == 0):
                texto = '\nNão foi digitado nenhum número primo!\n'
            elif(len(semRepetir) == 1):
                if(list(semRepetir.values())[0] == 1):
                    texto = '\nO número primo digitado foi o ' + str(list(semRepetir.keys())[0]) + '.\n'
                else:
                    texto = '\nO número primo digitado foi o ' + str(list(semRepetir.keys())[0]) + ' por ' + str(list(semRepetir.values())[0]) + ' vezes.\n'
            else:
                texto = '\nOs números primos digitados foram o '
                for i, n in semRepetir.items():
                    if(i == list(semRepetir.keys())[-1]):
                        if(n == 1):
                            texto += str(i) + '.\n'
                        else:
                            texto += str(i) + ' por ' + str(n) + ' vezes.'
                    elif(i == list(semRepetir.keys())[-2]):
                        if(n == 1):
                            texto += str(i) + ' e o '
                        else:
                            texto += str(i) + ' por ' + str(n) + ' vezes e o '
                    else:
                        if(n == 1):
                            texto += str(i) + ', '
                        else:
                            texto += str(i) + ' por ' + str(n) + ' vezes, '
            return texto
        except:
            print('\n ======== Erro ao gerar texto! =========\n'
                  '\n =========== Digite novamente!=============\n')
            main()
            return 1

    main()




def exercicio19(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Recebe valores e imprime os números pares contidos. ")
    print("")

    def main():
        # Guia de execução do programa

        while True:
            try:
                # Recebe um valor informado pelo usuário e insere em uma lista
                valor = 0
                x = 0
                lista = []
                while(valor != ''):
                    if(x == 0):
                        valor = input('\nDigite um parâmetro para ser conferido: ')
                        x += 1
                    else:
                        valor = input('\nDigite outro ou pressione enter para conferir: ')
                    if(valor.isdigit()):
                        lista.append(int(valor))
                    elif(valor == ''):
                        break
                break
            except:
                print('\n====== Erro ao capturar valor! Digite novamente =========')
                main()
                return 1

        try:
            # Remove os números impares da lista
            for i in lista:
                if(i%2 != 0):
                    lista.remove(i)
        except:
            print('\n========== Erro ao excluir números impares! ==========\n')
            main()
            return 1

        try:
            # Combina o número da lista com a quantidade de vezes que aparece
            dicionario = {}
            for n in lista:
                y = 0
                for k in lista:
                    if(n == k):
                        y += 1
                dicionario[n] = y
        except:
            print('\n========== Erro ao combinar números com quantidades! ==========\n')
            main()
            return 1

        try:
            # Constroi um texto com o resultado do programa e exibe
            if(len(dicionario) == 0):
                print('\nNão foi digitado nenhum número par!\n')
            elif(len(dicionario) == 1):
                if(list(dicionario.values())[0] == 1):
                    fim = str(list(dicionario.keys())[0]) + '!\n'
                    print('\nO número par digitado foi o', fim)
                else:
                    print('\nO número par digitado foi o ' + str(list(dicionario.keys())[0]) + ' por ' + str(list(dicionario.values())[0]) + ' vezes!')
            else:
                texto = '\nOs nḿeros pares digitados foram '
                for k, v in dicionario.items():
                    if(k == list(dicionario.keys())[-1]):
                        if(v == 1):
                            texto = texto + str(k) + '!\n'
                        else:
                            texto = texto + str(k) + ' por ' + str(v) + ' vezes!\n'
                    elif(k == list(dicionario.keys())[-2]):
                        if(v == 1):
                            texto = texto + str(k) + ' e '
                        else:
                            texto = texto + str(k) + ' por ' + str(v) + ' vezes e '
                    else:
                        if (v == 1):
                            texto = texto + str(k) + ', '
                        else:
                            texto = texto + str(k) + ' por ' + str(v) + ' vezes, '
                print(texto)
            return 0
        except:
            print('\n ====== Erro ao cirar e exibir texto ======\n')
            main()
            return 1
    main()

def exercicio20(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Verifica se o termo informado pelu usuário é um palindromo. ")
    print("")

    def main():
        # Guia a execução do programa

        while True:
            try:
                # Recebe o valor informado pelo usuário
                valor = input('\nDigite uma expressão para ser verificada: ')
                break
            except:
                print('\n ====== Erro ao capturar valor! Digite novamente! ========')

        try:
            # Deixa o valor inforado minusculo
            valorMinusculo = valor.lower()
        except:
            print('\n ======= Erro ao tornar minuscula =========\n')
            main()
            return 1

        try:
            # Verifica se a string é igual a ela mesma invertida
            if(valorMinusculo == valorMinusculo[::-1]):
                print('\nA expressão informada é um palindromo!')
                return 0
            else:
                print('\nA expressão informada não é um palindromo!\n')
                return 0
        except:
            print('\n========= Erro ao verirficar se é palindromo! Digite novamente =========\n')
            main()
            return 1
    main()

def exercicio21(num):
    print('')
    print('')
    print('')
    print(" =============================== Exercício", num, "==============================")
    print('')
    print(" Verifica se o termo informado pelu usuário é um palindromo. ")
    print("")

    def main():
        # Guia a execução do programa
        def recebe():
            try:
                return input('\nDigite algum parâmetro para ser exibido: ')
            except:
                print('\n======= Erro ao receber parâmetro! Digite novamente! =======')
        print('\n"' + recebe() + '"\n')
        return 0
    main()

def inicio():
    print('')
    print('')
    print(" =============================== Exercícios de funçoes em Python ==============================")
    print('')
    print("Os exercícios estão numerados de 1 a 21, digite o número do exercío para executar o mesmo, 'sair' para finalizar e 'ajuda' para obter ajuda")
    print("")
    try:
        # Recebe um parâmetro informado pelo usuário
        num = input("Número do exercício: ")
    except:
        print("\n============ Digite apenas valores válidos! ==========\n")
        inicio()
    print('')
    print('')
    # Compara o parâmtro informado pelo usuário e selciona o exercício de acordo
    if(num == '1'):
        exercicio1()
        inicio()
    elif(num == '2'):
        exercicio2()
        inicio()
    elif(num == '3'):
        exercicio3()
        inicio()
    elif(num == '4'):
        exercicio4()
        inicio()
    elif(num == '5'):
        exercicio5()
        inicio()
    elif(num == '6'):
        exercicio6()
        inicio()
    elif(num == '7'):
        exercicio7()
        inicio()
    elif(num == '8'):
        exercicio8()
        inicio()
    elif(num == '9'):
        exercicio9()
        inicio()
    elif(num == '10'):
        exercicio10()
        inicio()
    elif(num == '11'):
        exercicio11()
        inicio()
    elif(num == '12'):
        exercicio12(num)
        inicio()
    elif(num == '13'):
        exercicio13(num)
        inicio()
    elif(num == '14'):
        exercicio14(num)
        inicio()
    elif(num == '15'):
        exercicio15(num)
        inicio()
    elif(num == '16'):
        exercicio16(num)
        inicio()
    elif(num == '17'):
        exercicio17(num)
        inicio()
    elif(num == '18'):
        exercicio18(num)
        inicio()
    elif(num == '19'):
        exercicio19(num)
        inicio()
    elif(num == '20'):
        exercicio20(num)
        inicio()
    elif(num == '21'):
        exercicio21(num)
        inicio()
    elif(num == 'sair'):
        exit(0)
        return 0
    elif(num == 'ajuda'):
        print('\n=================================================================== Exercícios de python ================================================================\n'
              '\n1) Escreva um algoritmo que contenha uma função de nome estudo() e que quando executada imprima na saída padrão a frase "Estamos estudando as funções":'
              '\n'
              '\n2) Escreva um código contendo uma função de nome estudo e defina que a mesma deva receber um número como argumento. Chame este argumento de x.\n No corpo da função imprima a seguinte frase na tela: "Função invocada com sucesso. O valor passado pelo argumento x é: <valor de x>"'
              '\n'
              '\n3) Escreva um algoritmo que receba dois números através da declaração de dois parâmetros cujos nomes serão: x e y. No bloco de instrução faça a soma de ambos valores e imprima o resultado no monitor:'
              '\n'
              '\n4) Escreva um algoritmo contendo uma função que necessite de três argumentos. Em seguida, imprima na tela os argumentos em ordem ascendente e, por fim, imprima a média aritmética:'
              '\n'
              '\n5) Escreva uma função que contenha dois parâmetros. O primeiro deve ser obrigatório e o segundo facultativo:'
              '\n'
              '\n6) Escreva uma função que invocará outra função na qual tenha dois parâmetros definidos. Invoque a primeira função de ``func1()`` e a segunda de ``func2()``. \nEm seguida, invoque os parâmetros da segunda função de x e y. Some x e y e retorne o resultado. Em func1(), ao receber o resultado, retorne-o também como valor de retorno da função. \nPor fim, imprima na tela o valor que foi calculado por func2(), retornado para func1() e retornado a quem invocou a função inicialmente:'
              '\n'
              '\n7) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros. Em seguida, imprima os parâmetros recebidos na tela:'
              '\n'
              '\n8) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados a uma chave. Em seguida, imprima na tela o nome da chave e o respectivo valor:'
              '\n'
              '\n9) Considere o trecho de código a seguir.'
              '\n'
              '\n     def func(a, b, c, d):'
              '\n         print(a+b+c+d)'
              '\n     lista = 1, 2, 3, 4'
              '\n'
              '\nInvoque a função func(), passando como argumento os valores contidos em lista, com a respectiva ordem, de forma a utilizar o conceito de desempacotamento:'
              '\n'
              '\n10) Escreva um algoritmo que encontre o maior dentre 3 números. Para facilitar a resolução do exercício utilize funções.'
              '\n'
              '\n11) Escreva um função que some todos os números contidos numa lista.'
              '\n'
              '\n     Lista: (1, 2, 3, 4, 5)'
              '\n     Soma: 15'
              '\n'
              '\n12) Escreva uma função que multiplique todos os números de uma lista.'
              '\n'
              '\nLista: (1, 2, 3, 4, 5)'
              '\nMultiplicação: 120'
              '\n'
              '\n13) Escreva uma função que inverta a ordem dos elementos de uma lista manualmente. Não utilize a função interna do Python que faz inverção, crie o algoritmo que faça a inversão.'
              '\n'
              '\nLista: "1234abcd"'
              '\nSaída: "dcba4321"'
              '\n'
              '\n14) Escreva uma função que calcule o fatorial de um número (um inteiro não negativo). Envie o valor do número que será calcula como argumento da função.'
              '\n'
              '\n15) Escreva uma função que verifique se um número está num intervalo determinado.'
              '\n'
              '\n16) Escreva uma função que aceite Strings e calcule a quantidade de letras em mauisculas e minúsculas que a String possui.'
              '\n'
              '\n17) Escreva uma função que receba como argumento uma lista que poderá ter valores duplicados e retorne uma nova lista sem que haja valores iguais.'
              '\n'
              '\nLista: [1,2,3,3,3,3,4,5]'
              '\nRetorno: [1, 2, 3, 4, 5]'
              '\n'
              '\n18) Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros e imprima na telas os números primos contidos nessa lista.'
              '\n'
              '\n19) Escreva uma função que imprima somente os números pares'
              '\n'
              '\nLista: [1, 2, 3, 4, 5, 6, 7, 8, 9]'
              '\nSaída: [2, 4, 6, 8]'
              '\n'
              '\n20) Escreva uma função que verifica se uma String enviada é um palíndromo ou não.'
              '\n'
              '\n21) Escreva uma função que tenha definida uma função em seu escopo. Invoque a função aninhada, retorne algum valor, imprima esse valor na tela e finalize a aplicação.')

        inicio()
    else:
        print("\n============ Digite apenas valores válidos! ==========\n")
        inicio()
inicio()
