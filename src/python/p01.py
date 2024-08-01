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

    if __name__ == "__main__":
        main()

    if escolha_menu in opcao:
        continue
    elif escolha_menu > 5:
        opcao_invalida()
        continue
    elif escolha_menu == 5:
        print("Finalizando...")
        exit()
