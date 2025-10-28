import os
from datetime import datetime

ARQUIVO = "dados/registros.txt"
LOG = "dados/log.txt"
dados = []

def registrar_log(acao):
    with open(LOG, "a", encoding="utf-8") as f:
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"[{agora}] {acao}\n")

def carregar_dados():
    os.makedirs("dados", exist_ok=True)
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                if ";" in linha:
                    nome, curso, media = linha.strip().split(";")
                    dados.append({"nome": nome, "curso": curso, "media": media})
    registrar_log("Sistema iniciado")

def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for item in dados:
            f.write(f"{item['nome']};{item['curso']};{item['media']}\n")
    registrar_log("Dados salvos no arquivo")

def cadastrar():
    nome = input("Nome: ")
    curso = input("Curso: ")
    while True:
    media = input("Média final (0 a 10): ")
    try:
        m = float(media)
        if 0 <= m <= 10:
            media = str(m)
            break
        else:
            print("Informe um valor entre 0 e 10.")
    except ValueError:
        print("Digite um número válido.")
    dados.append({"nome": nome, "curso": curso, "media": media})
    salvar_dados()
    registrar_log(f"Cadastro de aluno: {nome}")
    print("Cadastro realizado com sucesso!")

def listar():
    if not dados:
        print("Nenhum registro encontrado.")
        return
    print("\n--- LISTA DE ALUNOS ---")
    for i, item in enumerate(dados, 1):
        print(f"{i}. {item['nome']} | {item['curso']} | Média: {item['media']}")
    registrar_log("Listagem de alunos")

def editar():
    listar()
    try:
        idx = int(input("Número do registro a editar: ")) - 1
        if 0 <= idx < len(dados):
            dados[idx]["nome"] = input("Novo nome: ")
            dados[idx]["curso"] = input("Novo curso: ")
            dados[idx]["media"] = input("Nova média: ")
            salvar_dados()
            registrar_log(f"Edição de registro: {dados[idx]['nome']}")
            print("Registro atualizado com sucesso!")
        else:
            print("Registro não encontrado.")
    except ValueError:
        print("Entrada inválida.")
        registrar_log("Erro ao editar registro")

def excluir():
    listar()
    try:
        idx = int(input("Número do registro a excluir: ")) - 1
        if 0 <= idx < len(dados):
            nome = dados[idx]['nome']
            del dados[idx]
            salvar_dados()
            registrar_log(f"Exclusão de registro: {nome}")
            print("Registro excluído com sucesso!")
        else:
            print("Registro não encontrado.")
    except ValueError:
        print("Entrada inválida.")
        registrar_log("Erro ao excluir registro")
