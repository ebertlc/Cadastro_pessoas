class Pessoa:
    def __init__(self):
        self.usuarios = {}  # Dicionário para armazenar os dados das pessoas

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

    def listar_todas(self):
        if self.usuarios:
            print("Pessoas cadastradas:")
            for cpf, pessoa in self.usuarios.items():
                self._print_pessoa_info(pessoa, cpf)  # Utiliza método auxiliar para imprimir informações
        else:
            print("Nenhuma pessoa cadastrada.")

    def _print_pessoa_info(self, pessoa, cpf):
        print("Nome:", pessoa['nome'])
        print("Idade:", pessoa['idade'])
        print("Sexo:", pessoa['sexo'])
        print("CPF:", cpf)


class SistemaCadastro:
    def __init__(self):
        self.pessoa = Pessoa()  # Cria uma instância da classe Pessoa para lidar com as informações

    def menu_principal(self):
        while True:
            try:
                acao = int(input("Informe a ação desejada:\n1 - Cadastrar Pessoa\n2 - Consultar Pessoa\n3 - Sair\n"))
                if acao == 1:
                    self.cadastrar_pessoa()  # Chama o método para cadastrar uma pessoa
                elif acao == 2:
                    self.consultar_pessoa()  # Chama o método para consultar uma pessoa
                elif acao == 3:
                    break
                else:
                    print("Ação inválida\n\n")
            except ValueError:
                print("Ação inválida\n\n")

    def cadastrar_pessoa(self):
        while True:
            try:
                nome = input("Digite o nome da pessoa: ")
                idade = int(input("Digite a idade da pessoa: "))
                sexo = input("Digite o sexo da pessoa: ")
                cpf = input("Digite o CPF: ")

                self.pessoa.cadastrar(nome, idade, sexo, cpf)  # Chama o método cadastrar da classe Pessoa

                opcao = int(input("\n1 - Voltar ao menu principal\n2 - Cadastrar outro usuário\n"))

                if opcao == 1:
                    break
                elif opcao != 2:
                    print("Opção inválida\n\n")
            except ValueError:
                print("Opção inválida\n\n")

    def consultar_pessoa(self):
        while True:
            try:
                consulta = int(input("\n1 - Consultar Todas as Pessoas\n2 - Consultar por CPF\n3 - Voltar ao Menu\n"))
                if consulta == 1:
                    self.pessoa.listar_todas()  # Chama o método listar_todas da classe Pessoa
                elif consulta == 2:
                    cpf_consultar = input("Digite o CPF: ")
                    print("Detalhes da pessoa:\n")
                    self.pessoa.consultar(cpf_consultar)  # Chama o método consultar da classe Pessoa

                    opcao = int(input("\n1 - Voltar ao menu principal\n2 - Consultar outro usuário\n"))

                    if opcao == 1:
                        break
                    elif opcao != 2:
                        print("Opção inválida\n\n")
                elif consulta == 3:
                    break
                else:
                    print("Opção inválida\n\n")
            except ValueError:
                print("Opção inválida\n\n")


if __name__ == "__main__":
    sistema = SistemaCadastro()  # Cria uma instância do sistema de cadastro
    sistema.menu_principal()  # Inicia o menu principal
