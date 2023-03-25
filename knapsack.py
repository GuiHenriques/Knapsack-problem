from operator import itemgetter

class Mochila:
    def __init__(self, peso_maximo: float) -> None:
        self.peso_maximo = peso_maximo
        self.peso_ocupado = 0
        self.itens = list()
        self.valor = 0

    def get_peso_max(self):
        return self.peso_maximo

    def set_peso_max(self, x):
        self.peso_maximo = x

    def get_peso_ocupado(self):
        return self.peso_ocupado
    
    def get_itens(self):
        return self.itens
    
    def get_valor(self):
        return self.valor


class item:
    def __init__(self):
        self.itens = dict()       
        self.Vu = dict()    # Vu = valor utilitário (valor/peso)        

    def get_preco_item(self):
        return self.valor_item

    def get_peso_item(self):
        return self.peso_item

    def get_etiqueta(self):
        return self.etiqueta
    
    def get_itens(self):
        return self.itens
    
    def get_Vu(self):
        return self.Vu
    
    def ordenar_Vu(self):
        return sorted(self.Vu.items(), key=itemgetter(1)) # ordena do menor pro maior
    
    def add_item(self, etiqueta, peso, valor):
        self.itens[etiqueta] = [peso, valor]
        self.Vu[etiqueta] = valor/peso

    
    
    



    