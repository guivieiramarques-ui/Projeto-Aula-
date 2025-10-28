from funcoes import *

def menu():
    while True:
        print("\n=== SISTEMA DE CADASTRO DE ALUNOS ===")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("5. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                cadastrar()
            elif opcao == 2:
                listar()
            elif opcao == 3:
                editar()
            elif opcao == 4:
                excluir()
            elif opcao == 5:
                registrar_log("Encerramento do programa")
                print("Saindo... até mais!")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")
            registrar_log("Erro: entrada inválida no menu")

if __name__ == "__main__":
    carregar_dados()
    menu()
