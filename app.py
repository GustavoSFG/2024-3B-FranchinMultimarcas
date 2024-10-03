import os

# Usaremos um dicionário para armazenar o nome do carro e seu status
carros = {}

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu principal...')
    main()

def mostra_titulo():
    print("""
𝑭𝑹𝑨𝑵𝑪𝑯𝑰𝑵 𝑴𝑼𝑳𝑻𝑰𝑴𝑨𝑹𝑪𝑨𝑺
    """)

def mostra_escolha():
    print('1. Cadastro de carros')
    print('2. Listar carros')
    print('3. Ativar/desativar carros')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção:', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_carros()
        elif opcao_escolhida == 2:
            mostrar_carros()
        elif opcao_escolhida == 3:
            ativar_desativar_carro()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def cadastrar_carros():
    exibir_subtitulo('Cadastrar carros')

    nome_carro = input('Digite o nome do carro: ').strip()
    if nome_carro:
        carros[nome_carro] = True  # O carro é adicionado como ativo por padrão
        print(f'{nome_carro} foi adicionado à lista de carros.')
    else:
        print('Nome do carro não pode ser vazio.')

    retorna_menu_principal()

def mostrar_carros():
    exibir_subtitulo('Listar carros')
    
    if carros:
        for carro, ativo in carros.items():
            status = 'Ativo' if ativo else 'Inativo'
            print(f' - {carro} ({status})')
    else:
        print('Nenhum carro cadastrado.')

    retorna_menu_principal()

def ativar_desativar_carro():
    exibir_subtitulo('Ativar/desativar carros')

    nome_carro = input('Digite o nome do carro para ativar/desativar: ').strip()
    if nome_carro in carros:
        carros[nome_carro] = not carros[nome_carro]  # Troca o status do carro
        status = 'ativado' if carros[nome_carro] else 'desativado'
        print(f'{nome_carro} foi {status}.')
    else:
        print('Carro não encontrado.')

    retorna_menu_principal()

def finalizar_programa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando programa...')
    exit()

def opcao_invalida():
    print('Esta opção não é válida. Tente novamente.')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolha()
    escolhe_opcao()

if __name__ == '__main__':
    main()

