print('Franchin Multimarcas')

print('1. Cadastro de Veiculos')
print('2. Listar Renavam e Chassi')
print('3. Ativar Anuncios de Veiculos')
print('4. Sair da Aplicação')

opcao_escolhida = int(input('Escolha uma opção: '))
print('Você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1: 
    print('Cadastro de Veiculo')
elif opcao_escolhida == 2:
    print('Listar  Renavam e Chassi')
elif opcao_escolhida == 3:
    print('Ativar Anuncios de Veiculos')
else:
    print('Saindo da Aplicação')
    