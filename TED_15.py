import pandas as pd

escolha = 1
cadastro = {}

while escolha != 0:
    print(
        "\033[1;31m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("""\033[1;31mBEM VINDO AO NOSSO SISTEMA DE CADASTRO.\033[1;30m
\nEscolha uma das opções abaixo:
1 - Cadastrar um funcionário
2 - Alterar um funcionário
3 - Listar (imprimir) todos os funcionários
4 - Excluir um funcionário
5 - Adicionar um aumento de salário
0 - Sair""")
    print("\033[1;31m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[1;30m")

    escolha = int(input("\nDigite um número de acordo com a sua escolha: "))

    if escolha == 1:
        funcionario = input("\nInsira o primeiro nome do funcionário: ")

        cadastro[funcionario] = {}

        cod = input('Insira o código do funcionário: ')
        cadastro[funcionario]['Código do Funcionário'] = []
        cadastro[funcionario]['Código do Funcionário'].append(cod)

        nome = input('Insira o nome completo do funcionário: ')
        cadastro[funcionario]['Nome'] = []
        cadastro[funcionario]['Nome'].append(nome)

        email = input('Insira o e-mail do funcionário: ')
        cadastro[funcionario]['E-mail'] = []
        cadastro[funcionario]['E-mail'].append(email)

        data_de_adms = input('Insira a data de admissão do funcionário: ')
        cadastro[funcionario]['Data de Admissão'] = []
        cadastro[funcionario]['Data de Admissão'].append(data_de_adms)

        salario = int(input('Insira o salário do funcionário: '))
        cadastro[funcionario]['Salário'] = []
        cadastro[funcionario]['Salário'].append(salario)

    if escolha == 2:

        alterar = input("Insira o primeiro nome do funcionário: ")

        if alterar in cadastro:

            cod = input('Insira o código do funcionário: ')

            if cod in cadastro[alterar]['Código do Funcionário']:

                cadastro[alterar] = {}

                cadastro[alterar]['Código do Funcionário'] = []
                cadastro[alterar]['Código do Funcionário'].append(cod)

                nome = input('Insira o nome completo do funcionário: ')
                cadastro[alterar]['Nome'] = []
                cadastro[alterar]['Nome'].append(nome)

                email = input('Insira o e-mail do funcionário: ')
                cadastro[alterar]['E-mail'] = []
                cadastro[alterar]['E-mail'].append(email)

                data_de_adms = input(
                    'Insira a data de admissão do funcionário: ')
                cadastro[alterar]['Data de Admissão'] = []
                cadastro[alterar]['Data de Admissão'].append(data_de_adms)

                salario = int(input('Insira o salário do funcionário: '))
                cadastro[alterar]['Salário'] = []
                cadastro[alterar]['Salário'].append(salario)

            else:
                print("O código do funcionário está incorreto. Digite novamente")
        else:
            print("Esse funcionário não existe ou não foi cadastrado")

    if escolha == 3:
        print(
            "\n\033[1;31m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print('LISTA DE FUNCIONÁRIOS\033[1;30m')
        cadastro_df = pd.DataFrame(cadastro)
        print(cadastro_df)
        print(
            "\033[1;31m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\033[1;30m")

    if escolha == 4:
        remover = input("Insira o primeiro nome do funcionário: ")

        if remover in cadastro:
            del cadastro[remover]
        else:
            print("Esse funcionário não existe ou não foi cadastrado")

    if escolha == 5:
        aumento_salario = input("\nInsira o primeiro nome do funcionário: ")

        if aumento_salario in cadastro:
            aumento = int(
                input("\nInsira o valor do aumento do salário do funcionário: "))
            novo_salario = cadastro[aumento_salario]['Salário'].pop() + aumento
            cadastro[aumento_salario]['Salário'].append(novo_salario)

        else:
            print("Esse funcionário não existe ou não foi cadastrado")

    if escolha == 0:
        print("Obrigado pela interação .")
