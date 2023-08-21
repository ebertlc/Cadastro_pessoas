import os
class System_Cadastro:
    class Pessoa:
        def __init__(self):
            self.usuarios = {}

        def cadastrar(self, nome, idade, sexo, cpf):
            if cpf not in self.usuarios:
                self.usuarios[cpf] = {
                    'nome': nome,
                    'idade': idade,
                    'sexo': sexo
                }
                print("Cadastro realizado com sucesso!")
            else:
                print("CPF já cadastrado.")

        def consultar(self, cpf):
            if cpf in self.usuarios:
                pessoa = self.usuarios[cpf]
                print("Nome:", pessoa['nome'])
                print("Idade:", pessoa['idade'])
                print("Sexo:", pessoa['sexo'])
                print("CPF:", cpf)
            else:
                print("CPF não encontrado.")

        def todas(self):
            if self.usuarios:
                print("Pessoas cadastradas:")
                for cpf, pessoa in self.usuarios.items():
                    print("Nome:", pessoa['nome'])
                    print("Idade:", pessoa['idade'])
                    print("Sexo:", pessoa['sexo'])
                    print("CPF:", cpf)
            else:
                print("Nenhuma pessoa cadastrada.")

    pessoa = Pessoa()  # Criando uma instância da classe Pessoa

    while True:
        try:
            acao = int(input("Informe a ação desejada:\n1 - Cadastrar Pessoa\n2 - Consultar Pessoa\n3 - Sair\n"))
            if acao == 1:
                while True:
                    try:
                        nome = input("Digite o nome da pessoa: ")
                        idade = int(input("Digite a idade da pessoa: "))
                        sexo = input("Digite o sexo da pessoa: ")
                        cpf = input("Digite o CPF: ")

                        pessoa.cadastrar(nome, idade, sexo, cpf)

                        opcao = int(input(
                            "\n\n1 - Voltar ao menu principal\n2 - Cadastrar outro usuário\n"))

                        if opcao == 1:
                            break
                        elif opcao == 2:
                            continue
                        else:
                            print("Opção inválida\n\n")
                            continue
                    except:
                        print("Opção inválida\n\n")
                        continue
            elif acao == 2:
                while True:
                    try:
                        consulta = int(input("\n\n1 - Consultar Todas as Pessoas\n2 - Consultar por CPF\n3 - voltar ao Menu"))
                        if consulta == 1:
                            pessoa.todas()
                        elif consulta == 2:
                            while True:
                                try:
                                    cpf_consultar = input("Digite o CPF: ")
                                    print("Detalhes da pessoa:\n")
                                    pessoa.consultar(cpf_consultar)

                                    opcao = int(input(
                                        "\n\nEscolha uma opção:\n1 - Voltar ao menu principal\n2 - Consultar outro usuário\n"))

                                    if opcao == 1:
                                        break
                                    elif opcao == 2:
                                        continue
                                    else:
                                        print("Opção inválida\n\n")
                                        continue
                                except:
                                    print("Opção inválida\n\n")
                                    continue
                        elif consulta == 3:
                            break
                        else:
                            print("Opção inválida\n\n")
                            continue
                    except:
                        print("Opção inválida\n\n")
                        continue
            elif acao == 3:
                break
            else:
                print("Ação inválida\n\n")
                continue
        except:
            print("Ação inválida\n\n")
            continue

System_Cadastro()


