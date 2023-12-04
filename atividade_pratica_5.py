'''
5.	Sistema de Classificação de Hotéis: "Desenvolva um programa que classifique um hotel baseado na avaliação dos hóspedes. 
O usuário deve digitar o nome do hotel e três notas referentes aos critérios de conforto, limpeza e localização. 
O programa deve calcular a média das notas e emitir uma classificação:
•	Média menor que 4: Hotel de 1 estrela
•	Média de 4 a 6: Hotel de 3 estrelas
•	Média de 6 a 8: Hotel de 4 estrelas
•	Média 9 ou superior: Hotel de 5 estrelas 
No final, o programa deve exibir o nome do hotel e sua classificação em estrelas."
'''

nome_hotel = input("Digite o nome do hotel:\n")
conforto = int(input(f"Digite a pontuação entre 1 e 10 para o conforto do hotel {nome_hotel}:\n"))
limpeza = int(input(f"Digite a pontuação entre 1 e 10 para a limpeza do hotel {nome_hotel}:\n"))
localização = int(input(f"Digite a pontuação entre 1 e 10 para a localização do hotel {nome_hotel}:\n"))
media = (conforto + limpeza + localização) / 3

if media < 4 :
    print(f"O hotel {nome_hotel} possui pontuação média de {media} e está classificado como 1 estrela")
elif media >= 4 and media <= 6 :
    print(f"O hotel {nome_hotel} possui pontuação média de {media} e está classificado como 3 estrelas")
elif media >= 6 and media <= 8 :
    print(f"O hotel {nome_hotel} possui pontuação média de {media} e está classificado como 4 estrelas")
else :
    print(f"O hotel {nome_hotel} possui pontuação média de {media} e está classificado como 5 estrelas")
