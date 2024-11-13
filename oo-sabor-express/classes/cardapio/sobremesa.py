from classes.cardapio.item_cardapio import ItemCardapio
class Sobremesa(ItemCardapio):
    def __init__(self, nome, tipo, preco):
        super().__init__(nome, preco)
        self._nome = nome
        self._preco = preco
        self._tipo = tipo

    def aplicar_desconto(self, desconto):
        return super().aplicar_desconto(self._preco, desconto)