from knapsack import *
from random import randint

itens = []

def casos_teste(n):

    def letter(n):
        start = 65
        n_alfabeto = 26
        for i in range(n):
            first_letter = chr(start + (i//n_alfabeto))
            second_letter = chr(start + (i % n_alfabeto))
        return f'"{first_letter}{second_letter}"'

    def peso_valor(min, max):
        return randint(min, max)

    for i in range(1, n):
        peso = peso_valor(1, 100)
        valor = peso_valor(0, 100)
        etiqueta = letter(i)
        itens.append(Item(peso, valor, etiqueta))

# Numero de casos de teste
casos_teste(20)

mochila = Mochila(300)

manejador = ManejadorItem()
for item in itens:
    manejador.add_item(item)


manejador.ordenar_Vu()

for item in manejador.get_itens():
    if mochila.adicionar_item(item):
        print(f"Item {item.get_etiqueta()} adicionado com sucesso")
    else:
        print(f"Item {item.get_etiqueta()} não coube")
        continue
    

print('='*20)
print("valor", mochila.valor_acumulado)
print(f"{mochila.peso_ocupado/mochila.peso_maximo*100:.2f} % de {mochila.peso_maximo}kg")