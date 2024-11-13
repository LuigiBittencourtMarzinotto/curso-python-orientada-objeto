from classes.restaurante import Restaurante
from classes.cardapio.prato import Prato
from classes.cardapio.sobremesa import Sobremesa
from classes.cardapio.bebida import Bebida


import os

def view_option():

    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alterar status do restaurante")
    print("4. Cradastra uma validação de restaurante")
    print("5. Listar Feedbacks")
    print("6. Cadastrar Bebida")
    print("7. Sair \n")

def choose_option():
    choosing = input("Escolha uma opção: ")
    print(f"Você escolheu a opção: {choosing}")
    return choosing

def view_subtitle(text):
    os.system("cls")
    linha = '*'
    numberLetras = len(text)
    print(f'{linha * numberLetras}')
    print(f"{text} ")
    print(f'{linha * numberLetras}')

def create_restaurant():

    view_subtitle("Cadastre um restaurante")
    restaurant = input("Digite o nome do seu restaurante: ")
    categoria = input("Digite a categoria do seu restaurante: ")
    Restaurante(nome=restaurant, categoria=categoria)

    print(f"\nO restaurante {restaurant} foi criado com sucesso!")

def back_menu_main():
    input("\nDigite uma tecla para voltar ao menu principal")

def create_bebida():
    view_subtitle("Seleciona o indice do restaurante para inserir uma bebida")
    Restaurante.get_list_restaurantes()
    try:
        index = int(input("\nIndex do restaurante: "))
        nome = input("\n Nome da bebida: ")
        preco = float(input("\n Preço da bebida: "))
        tamanho = float(input("\n tamanho da bebida: "))
        bebida_criada = Bebida(nome=nome, preco=preco, tamanho=tamanho)
        Restaurante.create_item_cardapio(index, bebida_criada)
        os.system("cls")
        print("Bebida cadastrada com sucesso!")
        Restaurante.list_cardapio(index)

    except ValueError:
        print("Valor inválido. Por favor, insira um número inteiro.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    
    back_menu_main()

def create_feedback():
    view_subtitle("Seleciona o indice do restaurante a avaliado")
    Restaurante.get_list_restaurantes()
    try:
        index = int(input("\nIndex do restaurante: "))
        cliente = input("\n Nome do cliente da avaliacao: ")
        nota = int(input("\n Nota do restaurante: "))
        Restaurante.receber_avaliacao(index, cliente=cliente, nota=nota)
        print("Avaliação criada com sucesso")
    except ValueError:
        print("Valor inválido. Por favor, insira um número inteiro.")
        create_feedback()  
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        create_feedback() 
    
    back_menu_main()


def alterar_status():
    view_subtitle("Seleciona o indice do restaurante a ser trocado")
    Restaurante.get_list_restaurantes()
    try:
        index = int(input("\nIndex do restaurante: "))
        Restaurante.alterar_status(index)
        print("Status alterado com sucesso!")
    except ValueError:
        print("Valor inválido. Por favor, insira um número inteiro.")
        alterar_status()  
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        alterar_status() 
    
    back_menu_main()

def list_feedback():
    view_subtitle("Seleciona o indice do restaurante a ser listado as avaliação")
    Restaurante.get_list_restaurantes()
    try:
        index = int(input("\nIndex do restaurante: "))
        Restaurante.get_list_avaiacao(index)
    except ValueError:
        print("Valor inválido. Por favor, insira um número inteiro.")
        alterar_status()  
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        alterar_status() 
    
    back_menu_main()

def choosign_option(choosing):
    match choosing:
        case '1':
            create_restaurant()
            back_menu_main()
        case '2':
            os.system("cls")
            Restaurante.get_list_restaurantes()
            back_menu_main()
        case '3':
            alterar_status()
        case '4':
            create_feedback()  
        case '5':
            list_feedback() 
        case '6':
            create_bebida() 
        case '7':
            print('Finalizando Aplicação')  
        case _:
            print("opcao invalida")
    return False


def main():
    choosing = '0'
    while(choosing != '7'):
        os.system("cls")
        view_option()
        choosing = choose_option()
        choosign_option(choosing)

if __name__ == '__main__':
    main()
