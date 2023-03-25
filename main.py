from knapsack import *

# n = int(input('Digite a quantidade de itens: '))
# p = float(input('Digite o peso máximo da mochila: '))
    
itens = [
    Item(10, 10, "A"),
    Item(20, 50, "B"),
    Item(40, 30, "C"),
    Item(40, 50, "D"),
    Item(70, 95, "E")
]

mochila = Mochila(100)

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

print('='*10)
print("valor", mochila.valor_acumulado)
print(f"{mochila.peso_ocupado/mochila.peso_maximo*100:.2f} % de {mochila.peso_maximo}kg")