while(True):
#Variável Idade
    idade=int(input("Digite a sua idade: "))
#Condições
    if(idade<10):
        print("Sua mensalidade será de R$180,00")
        break
    elif(idade>=10 and idade<=30):
        print("Sua mensalidade será de R$150,00")
        break
    elif(idade>30 and idade<=60):
        print("Sua mensalidade será de R$195,00")
        break
    elif(idade>60):
        print("Sua mensalidade será de R$130,00")
        break
    else:
        print("Digite um caracter válido!")