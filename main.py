from knapsack import *
    
# PESO, VALOR, ETIQUETA
itens = [
    Item(10, 10, "A"),
    Item(20, 50, "B"),
    Item(40, 30, "C"),
    Item(40, 50, "D"),
    Item(70, 95, "E"),
    Item(30, 56, 'F'),
    Item(40, 67, 'G'),
    Item(45, 87, 'H'),
    Item(67, 89, 'J'),
    Item(54, 80, 'K'),
    Item(89, 90, 'L'),
    Item(45, 85, 'M'),
    Item(50, 70, 'N'),
    Item(60, 80, 'O'),
    Item(56, 78, 'P'),
    Item(45, 80, 'Q'),
    Item(70, 90, 'R'),
    Item(890, 60, 'S'),
    Item(70, 210, 'T'),
    Item(110, 70, 'U'),
    Item(122, 459, 'V'),
    Item(80, 20, 'W'),
    Item(50, 110, 'X'),
    Item(10, 60, 'Y'),
    Item(70, 770, 'Z'),
    Item(48, 56, 'AB'),
    Item(34, 56, 'AC'),
    Item(45, 67, 'AD'),
    Item(56, 78, 'AE'),
    Item(34, 23, 'AF'),
    Item(45, 343, 'AG') 
]


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