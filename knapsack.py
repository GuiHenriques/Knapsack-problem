from operator import itemgetter

class Mochila:
    def __init__(self, peso_maximo: float) -> None:
        self.peso_maximo = peso_maximo
        self.peso_ocupado = 0
        self.itens = list()
        self.valor_acumulado = 0

    def adicionar_item(self, item):
        if self.peso_ocupado + item.peso > self.peso_maximo:
            return False
        self.itens.append(item)
        self.peso_ocupado += item.peso
        self.valor_acumulado += item.valor
        return True

    def get_peso_max(self):
        return self.peso_maximo

    def get_peso_ocupado(self):
        return self.peso_ocupado
    
    def get_itens(self):
        return self.itens
    
    def get_valor(self):
        return self.valor

class Item:
    def __init__(self, peso, valor, etiqueta) -> None:
        self.peso = peso
        self.valor = valor
        self.etiqueta = etiqueta
        self.vu = valor/peso

    def get_preco_item(self):
        return self.valor_item

    def get_peso_item(self):
        return self.peso_item

    def get_etiqueta(self):
        return self.etiqueta

    def get_vu(self):
        return self.vu


class ManejadorItem:
    def __init__(self):
        self.itens = list()      

    def get_itens(self):
        return self.itens
        
    def ordenar_Vu(self):
        self.itens =  sorted(self.get_itens(), key=lambda item: item.get_vu(), reverse=True) # ordena do menor pro maior
    
    def get_by_etiqueta(self, etiqueta):
        for item in self.itens:
            if item.etiqueta == etiqueta:
                return item
        return "Item não encontrado"

    def add_item(self, item):
        self.itens.append(item)
