while(True):
#Variáveis
    codigoSalgados=int(input("Digite o código do salgado: "))
    quantidadeSalgados=int(input("Digite a quantidade de salgados: "))
#salgados
    coxinha=1
    pastel=2
    paoDeQueijo=3
    Enroladinho=4
#cálculo
    if(codigoSalgados==1):
        print(f"Sua conta deu {quantidadeSalgados*0.5}")
        break
    elif(codigoSalgados==2):
        print(f"Sua conta deu {quantidadeSalgados*0.75}")
        break
    elif(codigoSalgados==3):
        print(f"Sua conta deu {quantidadeSalgados*0.40}")
        break
    elif(codigoSalgados==4):
        print(f"Sua conta deu {quantidadeSalgados*0.80}")
        break
    else:
        print("Digite um caracter válido!")