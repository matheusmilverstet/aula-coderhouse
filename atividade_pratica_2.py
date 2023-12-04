'''
2.	Verificador de elegibilidade para votação: "Desenvolva um programa que determine se uma pessoa está apta a votar.
O usuário deve informar o nome e a idade. As regras para determinar a elegibilidade são:
•	Menos de 16 anos: não pode votar
•	De 16 a 17 anos: voto facultativo
•	De 18 a 70 anos: voto obrigatório
•	Mais de 70 anos: voto facultativo O programa deve informar o nome da pessoa e se ela deve votar, não pode votar ou se o voto é 
facultativo."
'''

nome = input("Digite o nome do eleitor(a):\n")
idade = int(input("Digite a idade do eleitor(a):\n"))

if idade >= 16 and idade <= 17 :
    print(f"O voto do eleitor(a) {nome} é facultativo!")
elif idade >= 18 and idade <= 70 :
    print(f"O voto do eleitor(a) {nome} é obrigatório!")
elif idade > 70 :
    print(f"O voto do eleitor(a) {nome} é facultativo!")
else :
    print(f"{nome} não pode votar!")