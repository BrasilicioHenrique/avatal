from dataclasses import dataclass

while True:
    def mostrar_menu():
        menu = """
        ====================
        SISTEMA ESCOLAR
        ====================
        1. Cadastrar novo estudante
        2. Listar todos os estudantes
        3. Atualizar dados de um estudante
        4. Excluir um estudante
        5. Sair
        ====================
        """
        print(menu)

    mostrar_menu()

    opcao = [1, 2, 3, 4]
    escolha_menu = int(input("Escolha uma opcao: "))

    def opcao_invalida():
        print("Opção inválida, por favor selecione uma opção válida.")

    def main():
        pass

    def cadastrar():
        @dataclass
        class cadastro:
            nome: str = str(input("nome e sobrenome: "))
            matricula: str = int(input("matricula: "))
            dia: int = str(input("dia de nascimento: "))
            mes: int = str(input("mes de nascimento: "))
            ano: int = str(input("ano de nascimento: "))
            data_nascimento = f"{dia}/{mes}/{ano}"
        cadastros = f'''
        {cadastro.nome}
        {cadastro.matricula}
        {cadastro.data_nascimento}'''
        print("Cadastro feito.")

    def listar():
        estudantes = []
        print(estudantes)

    def atualizar():
        atualizar = '''
        Funcao de atualizar
        '''
        print(atualizar)

    def excluir():
        excluir = '''
        Funcao para excluir
        '''
        print(excluir)

    if __name__ == "__main__":
        main()

    if escolha_menu == 1:
        cadastrar()
    elif escolha_menu == 2:
        listar()
        exit()
    elif escolha_menu == 3:
        atualizar()
        exit()
    elif escolha_menu == 4:
        excluir()
        exit()
    elif escolha_menu == 5:
        print("Finalizando...")
        exit()
    else:
        opcao_invalida()
        continue
