import random

print("------------------------------Adivinhar números aleatórios------------------------------")
print("- Regras:")
print("- O usuário deverá digitar um número inteiro mínimo e máximo de um intervalo;")
print("- O usuário deve digitar um número inteiro dentro desse intervalo para que o computador acerte;")
print("- O computador terá 3 chances até que perca.")
print("----------------------------------------------------------------------------------------")

print("------------------------------Entrada de dados-----------------------------------------")

print(str(input("Digite seu nome: ")))
numeroMinimo = int(input("Digite um número mínimo para o intervalo: "))
numeroMaximo = int(input("Digite um número máximo para o intervalo: "))
numeroAdivinhar = int(input("Digite um número dentro desse intervalo para que o computador acerte: "))

numeroComputador = random.radnint(numeroMinimo, numeroMaximo)
