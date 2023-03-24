from operator import itemgetter

class Mochila:
    def __init__(self, peso_maximo: float) -> None:
        self.peso_maximo = peso_maximo
        self.itens = dict()
        self.peso_ocupado = 0

    def get_peso_max(self):
        return self.peso_maximo

    def set_peso_max(self, x):
        self.peso_maximo = x

    def get_peso_ocupado(self):
        return self.peso_ocupado
    
    def get_itens(self):
        return self.itens



class item:
    def __init__(self, etiqueta, peso, valor):
        self.itens = dict()
        self.itens[etiqueta] = [peso, valor]
        self.Vu = dict()    # Vu = valor utilitário (valor/peso)
        self.Vu[etiqueta] = valor/peso

    def get_preco_item(self):
        return self.valor_item

    def get_peso_item(self):
        return self.peso_item

    def get_etiqueta(self):
        return self.etiqueta
    
    def ordenar_Vu(self):
        return sorted(self.Vu.items(), key=itemgetter(1))
    
    
    
    
    



    