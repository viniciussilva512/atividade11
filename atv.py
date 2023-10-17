# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = int(input("insira a distancia da sua viagem"))

if dist < int("200"):
    print("o valor da sua passagem é:" ,float (dist*0.50))
else:
    print("o valor da sua passagem é:" ,float(dist*0.45))