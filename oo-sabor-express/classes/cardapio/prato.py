from classes.cardapio.item_cardapio import ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._nome = nome
        self._preco = preco
        self._descricao = descricao
    
    def aplicar_desconto(self, desconto):
        return super().aplicar_desconto(self._preco, desconto)