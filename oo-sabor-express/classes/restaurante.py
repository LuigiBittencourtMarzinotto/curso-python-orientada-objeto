from classes.avaliacao import Avaliacao
from classes.cardapio.item_cardapio import ItemCardapio
from classes.cardapio.bebida import Bebida



class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, ativo = False): 
        ''' MEtodo construtor da classe, assim que a classe é gerada essa função e chamada'''
        self._nome = nome
        self._categoria = categoria
        self._ativo = ativo
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    @classmethod
    def get_list_restaurantes(cls):
        if cls.restaurantes: 
            for index, restaurante in enumerate(cls.restaurantes):
                print(f'\nÍndice: {index} | Restaurante: {restaurante._nome} | Categoria: {restaurante._categoria} | Ativo: {restaurante.ativo}  | Media: {cls.media_avaliacoes(restaurante)}\n')
        else:
            print("\n Nenhum restaurante cadastrado \n")

    @classmethod
    def alterar_status(cls, index):
        cls.restaurantes[index]._ativo = not cls.restaurantes[index]._ativo
    
    @classmethod
    def get_list_avaiacao(cls, index):
        if cls.restaurantes[index]._avaliacao: 
            for avaliacao in cls.restaurantes[index]._avaliacao:
                print(f'\nCliente: {avaliacao._cliente} | Nota: {avaliacao._nota}')
        else:
            print("\n Nenhum avaliacao cadastrado \n")
    
    @property
    def ativo(self):
        return f'Verdadeiro' if self._ativo else 'Falso'

    @classmethod
    def receber_avaliacao(cls, index, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        cls.restaurantes[index]._avaliacao.append(avaliacao)

    @classmethod
    def create_item_cardapio(cls, index, item):
        if isinstance(item, ItemCardapio):
            cls.restaurantes[index]._cardapio.append(item)

    @classmethod
    def list_cardapio(cls, index):
        if cls.restaurantes[index]._cardapio: 
            for i, item in enumerate(cls.restaurantes[index]._cardapio, start=1):
                if isinstance(item, Bebida):
                    linha = '*'
                    numberLetras = len("Bebidas".ljust(40).rjust(40))
                    print(f'{linha * numberLetras}')
                    print("Bebidas".rjust(20))
                    print(f'{linha * numberLetras}')
                    mensagem = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}"
                    print(f'\n  {mensagem}')
        else:
            print("\n Nenhum bebida cadastrada \n")
    @classmethod
    def media_avaliacoes(cls, restaurante):
        if not restaurante._avaliacao:
            return '-'
        soma_das_notas = round(sum(avaliacao._nota for avaliacao in restaurante._avaliacao) / 2)
        quantidade_de_notas = len(restaurante._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    
