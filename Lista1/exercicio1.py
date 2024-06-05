#Variáveis
velPermitida=int(input("Informe a velocidade permitida na via: "))
velMotorista=int(input("Informe a velocidade do motorista: "))
#Caso não ultrasse¹
if(velMotorista>velPermitida):
#Caso ultrapasse
    if(velMotorista>(0.5*velPermitida)+velPermitida):
        print("Infração Gravíssima.\nR$574,00 + 7 pontos + Apreensão da Carteira + Suspensão do Direito de Dirigir")
    elif(velMotorista>(0.2*velPermitida)+velPermitida):
        print("Infração Grave.\nR$127,00 + 5 pontos")
    else:
        print("Infração Média.\nR$85,00 + 4 pontos")
#Caso não ultrapasse²
else:
    print("Você está dentro do limite.")