while(True):
#Variáveis
    primeiroNumero=float(input("Digite o primeiro valor: "))
    segundoNumero=float(input("Digite o segundo valor: "))
    operacaoMatematica=input("Digite a operação desejada: ").lower()
#Operações Matemáticas
    adicao=(primeiroNumero+segundoNumero)
    subtracao=(primeiroNumero-segundoNumero)
    multiplicacao=(primeiroNumero*segundoNumero)
    divisao=(primeiroNumero/segundoNumero)
#Código
    if(operacaoMatematica=='adição'):
        print(f"{primeiroNumero} + {segundoNumero} = {adicao}")
        break
    elif(operacaoMatematica=='subtração'):
        print(f"{primeiroNumero} - {segundoNumero} = {subtracao}")
        break
    elif(operacaoMatematica=='multiplicação'):
        print(f"{primeiroNumero} x {segundoNumero} = {multiplicacao}")
        break
    elif(operacaoMatematica=='divisão'):
        print(f"{primeiroNumero} / {segundoNumero} = {divisao}")
        break
    else:
        print("Digite uma operação válida!")