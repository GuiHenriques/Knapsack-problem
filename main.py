from knapsack import *
from random import randint


# função que cria os casos de teste
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
        valor = peso_valor(1, 100)
        etiqueta = letter(i)
        itens.append(Item(peso, valor, etiqueta))

itens = []
casos_teste(80)



mochila = Mochila(randint(150, 350))
manejador = ManejadorItem()
for item in itens:
    manejador.add_item(item)

# Ordenação por Valor utilitário (Vu)
manejador.ordenar_Vu()

for item in manejador.get_itens():
    mochila.adicionar_item(item)


print("Ordenação por Valor Utilitário")
print("Valor: R$", mochila.valor_acumulado)
print(f"{mochila.peso_ocupado/mochila.peso_maximo*100:.2f}% de {mochila.peso_maximo}kg")

# Limpar mochila
mochila.reset()
print("="*30)

# Ordenação por Valor
manejador.ordenar_valor()
for item in manejador.get_itens():
    mochila.adicionar_item(item)

print("Ordenação por Valor ")
print("Valor: R$", mochila.valor_acumulado)
print(f"{mochila.peso_ocupado/mochila.peso_maximo*100:.2f}% de {mochila.peso_maximo}kg")
