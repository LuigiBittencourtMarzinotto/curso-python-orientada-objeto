import os

list_restaurant = []

def back_menu_main():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()


def choosign_option(choosing):
    match choosing:
        case '1':
            create_restaurant()
        case '2':
            get_list_restaurant()
        case '3':
            alterarStatusRestaurante()
        case '4':
            finish_app()
        case _:
            print("opcao invalida")
            back_menu_main()

def alterarStatusRestaurante():
    view_subtitle("Alterar status do restaurante")

    restaurantName = input("Digite o nome do restaurante que será ativado: ")

    for restaurant in list_restaurant:
        if restaurant['nome'] == restaurantName:
            restaurant['ativo'] = not restaurant['ativo']
            status = "Ativado" if restaurant['ativo'] else "Desativado" 
            mensagem = f'\nO restaurante {restaurantName} foi {status} como solicitado'
            print(mensagem)
        else:
            print("Restaurante não foi encontrado.")

    back_menu_main()

    

def view_subtitle(text):
    os.system("cls")
    linha = '*'
    numberLetras = len(text)
    print(f'{linha * numberLetras}')
    print(f"{text} ")
    print(f'{linha * numberLetras}')


def create_restaurant():
    ''' Essa função cria restaurante
        Input:
            - Restaurante
            - Categoria
        Output:
            - Vai implementa na lista de restaurante
    '''
    view_subtitle("Cadastre um restaurante")
    restaurant = input("Digite o nome do seu restaurante: ")
    categoria = input("Digite a categoria do seu restaurante: ")
    dataRestaurant = {
        'nome': restaurant,
        'categoria': categoria,
        'ativo': False
    }

    list_restaurant.append(dataRestaurant)
    print(f"\nO restaurante {restaurant} foi criado com sucesso!")
    back_menu_main()

def get_list_restaurant():
    ''' Essa função lista restaurante'''

    view_subtitle("Lista de restaurante")

    for restaurant in list_restaurant:
        status = "Ativado" if restaurant['ativo'] else "Desativado" 
        print(f"{'Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)} \n")
        total_letras = (len(restaurant['nome']) + len(restaurant['categoria']) + len(status) ) + 5
        linha = '-' * (total_letras * 3)
        print(f'{linha}')
        print(f"{restaurant['nome'].ljust(20)} | {restaurant['categoria'].ljust(20)} | {status.ljust(20)} ")

    back_menu_main()

def finish_app():
    ''' Essa função finaliza a aplicacao'''

    view_subtitle("Finalizando aplicação")

def header_application():
    print("Sabor Express \n")
 
def view_option():

    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alterar status do restaurante")
    print("4. Sair \n")
  
def choose_option():
    choosing = input("Escolha uma opção: ")
    print(f"Você escolheu a opção: {choosing}")
    return choosing

def main():
    os.system("cls")
    header_application()
    view_option()
    choosing = choose_option()
    choosign_option(choosing)

if __name__ == '__main__':
    main()
