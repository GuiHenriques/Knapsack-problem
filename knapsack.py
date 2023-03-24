class Mochila:
    def __init__(self, peso_maximo: float) -> None:
        self.peso_maximo = peso_maximo
    
    def get_peso_max(self):
        return self.peso_maximo

    def set_peso_max(self, x):
        self.peso_maximo = x



class item:
    def __init__(self, etiqueta, peso, preco):
        self.etiqueta = etiqueta
        self.peso_item = peso
        self.preco_item = preco
    
    def get_preco_item(self):
        return self.preco_item
    
    def get_peso_item(self):
        return self.peso_item
    
    def get_etiqueta(self):
        return self.etiqueta
    



        