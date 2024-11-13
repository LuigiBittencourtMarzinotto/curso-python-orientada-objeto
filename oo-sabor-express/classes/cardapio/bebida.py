from classes.cardapio.item_cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._nome = nome
        self._preco = preco
        self._tamanho = tamanho
    
    def aplicar_desconto(self, desconto):
        return super().aplicar_desconto(self._preco, desconto)