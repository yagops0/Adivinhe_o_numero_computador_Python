import random

print("------------------------------Adivinhar números aleatórios------------------------------")
print("- Regras:")
print("- O usuário deverá digitar um número inteiro mínimo e máximo de um intervalo;")
print("- O usuário deve digitar um número inteiro dentro desse intervalo para que o computador acerte;")
print("- O computador terá 3 chances até que perca.")
print("----------------------------------------------------------------------------------------")
print()
print()
print("------------------------------Entrada de dados------------------------------------------")

chances = 3
chancesConseguir = 0
respostaUsuario = ""

nomeUsuario = (str(input("Digite seu nome: ")))
numeroMinimo = int(input("Digite um número mínimo para o intervalo: "))
numeroMaximo = int(input("Digite um número máximo para o intervalo: "))
numeroAdivinhar = int(input("Digite um número dentro desse intervalo para que o computador acerte: "))
print("----------------------------------------------------------------------------------------")
print()
print()
print("------------------------------Jogo------------------------------------------------------")

while True:
    numeroComputador = random.randint(numeroMinimo, numeroMaximo)
    print(f"O número é {numeroComputador}?")
    respostaUsuario = str(input("")).upper()
    
    if respostaUsuario == "não".upper():
        chances -= 1
        print(f"Chances restantes {chances}\n")
        if chances == 0:
            print("Computador perdeu.")
            print(f"{nomeUsuario} ganhou!")
            break
    else:
        if respostaUsuario == "sim".upper():
            if  chances == 3:
                print("O computador ganhou sem perder nenhuma chance!")
                print(f"{nomeUsuario} perdeu.")
            else:
                print(f"O computador ganhou com {chances} restante(s)!")
                print(f"{nomeUsuario} perdeu.")
        break
print("----------------------------------------------------------------------------------------") 
print()



        
    


