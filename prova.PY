def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b 

def divisao (a,b):
    if b != 0:
        return a / b
    else: 
        return "ERRO! Divisão por zero!"
    

vetor = []
resultado = 0
for _ in range(10):
    print("digite 1 para soma")
    print("digite 2 para subtração")
    print("digite 3 para multiplicação")
    print("digite 4 para divisão")
    print("digite 5 para sair")

    opcao = int(input("escolha uma operação: "))

    if opcao == 5:
        break

    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))

    if opcao == 1:
        resultado = soma(num1,num2)
    elif opcao == 2:
        resultado = subtracao(num1,num2)
    elif opcao == 3:
        resultado = multiplicacao(num1,num2)
    elif opcao == 4: divisao(num1,num2)

    vetor.append(resultado)

    print("Resultados:")
    for resultado in vetor:
        print(resultado, " ")

