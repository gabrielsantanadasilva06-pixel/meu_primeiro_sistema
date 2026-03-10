print("Olá matriculado acadêmico, tenha um bom dia! (; :)")

import json
import os

# ==============================
# FUNÇÕES DE ARQUIVO
# ==============================

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


# ==============================
# CARREGAMENTO
# ==============================

professores = carregar_dados("professores.json")
alunos = carregar_dados("alunos.json")
cursos = carregar_dados("cursos.json")
materias = carregar_dados("materias.json")


# ==============================
# LOGIN
# ==============================
while True:

    senha_admin = "admin123"
    tipo_acesso = None
    professor_logado = None
    nome_aluno_logado = None

    print("\nTIPO DE LOGIN")
    print("1 - Aluno")
    print("2 - Professor")
    print("3 - Administrador")
    print("4 - Encerrar sistema")

    tipo_login = input("Escolha: ")

    # ENCERRAR SISTEMA
    if tipo_login == "4":
        print("Sistema encerrado com sucesso.")
        break

    # ADMIN
    elif tipo_login == "3":
        senha = input("Digite a senha do administrador: ")
        if senha == senha_admin:
            tipo_acesso = "admin"
            print("Acesso ADMINISTRADOR liberado!")
        else:
            print("Senha incorreta.")
            continue

    # PROFESSOR
    elif tipo_login == "2":
        usuario = input("Usuário do professor: ")
        senha = input("Senha: ")

        for prof in professores:
            if prof["usuario"] == usuario and prof["senha"] == senha:
                professor_logado = prof
                tipo_acesso = "professor"
                print("Login realizado com sucesso!")
                break

        if not professor_logado:
            print("Login inválido.")
            continue

    # ALUNO
    elif tipo_login == "1":
        nome_aluno_logado = input("Digite seu nome: ")
        tipo_acesso = "aluno"
        print("Login realizado!")

    else:
        print("Opção inválida.")
        continue

# ==============================
# MENU ADMIN
# ==============================

    if tipo_acesso == "admin":
    
        while True:
            print("\n===== MENU ADMIN =====")
            print("1 - Cadastrar aluno")
            print("2 - Listar alunos")
            print("3 - Excluir aluno")
            print("4 - Cadastrar professor")
            print("5 - Vincular matéria a professor")
            print("6 - Listar professores")
            print("7 - Adicionar curso")
            print("8 - Listar cursos")
            print("9 - Adicionar matéria")
            print("10 - Listar matérias")
            print("11 - Sair")
    
            opcao = input("Escolha: ")
    
            # CADASTRAR ALUNO
            if opcao == "1":
                nome = input("Nome do aluno: ")
                curso = input("Curso: ")
                materia = input("Matéria: ")
    
                try:
                    nota1 = float(input("Nota 1: "))
                    nota2 = float(input("Nota 2: "))
                    nota3 = float(input("Nota 3: "))
                except ValueError:
                    print("Digite apenas números.")
                    continue
    
                media = (nota1 + nota2 + nota3) / 3
    
                situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    
                aluno = {
                    "nome": nome,
                    "curso": curso,
                    "materia": materia,
                    "media": round(media, 1),
                    "situacao": situacao,
                    "frequencia": [],
                    "conteudos": []
                }
    
                alunos.append(aluno)
                salvar_dados("alunos.json", alunos)
                print("Aluno cadastrado!")
    
            # LISTAR ALUNOS
            elif opcao == "2":
                if not alunos:
                    print("Nenhum aluno cadastrado.")
                else:
                        
                    for aluno in alunos:
                        print(f"Nome: {aluno['nome']}")
                        print(f"Curso: {aluno['curso']}")
                        print(f"Matéria: {aluno['materia']}")
                        print(f"Média: {aluno['media']}")
                        print(f"Situação: {aluno['situacao']}")
                        print("-" * 30)
    
            # EXCLUIR ALUNO
            elif opcao == "3":
                nome = input("Nome do aluno: ").lower()
                alunos[:] = [a for a in alunos if a["nome"].lower() != nome]
                salvar_dados("alunos.json", alunos)
                print("Aluno removido se existia.")
    
            # CADASTRAR PROFESSOR
            elif opcao == "4":
                usuario = input("Usuário: ")
                senha = input("Senha: ")
    
                professores.append({
                    "usuario": usuario,
                    "senha": senha,
                    "materias": []
                })
    
                salvar_dados("professores.json", professores)
                print("Professor cadastrado!")
    
            # VINCULAR MATÉRIA
            elif opcao == "5":
                usuario = input("Usuário do professor: ")
                materia = input("Matéria: ")
    
                for prof in professores:
                    if prof["usuario"] == usuario:
                        if materia not in prof["materias"]:
                            prof["materias"].append(materia)
                            salvar_dados("professores.json", professores)
                            print("Matéria vinculada!")
                        break
    
            # LISTAR PROFESSORES
            elif opcao == "6":
                for prof in professores:
                    print("Usuário:", prof["usuario"])
                    print("Matérias:", prof["materias"])
                    print("-" * 20)
    
            # ADICIONAR CURSO
            elif opcao == "7":
                nome = input("Nome do curso: ")
                cursos.append({"nome": nome})
                salvar_dados("cursos.json", cursos)
    
            # LISTAR CURSOS
            elif opcao == "8":
                for curso in cursos:
                    print(curso["nome"])
    
            # ADICIONAR MATÉRIA
            elif opcao == "9":
                nome = input("Nome da matéria: ")
                materias.append({"nome": nome})
                salvar_dados("materias.json", materias)
    
            # LISTAR MATÉRIAS
            elif opcao == "10":
                for m in materias:
                    print(m["nome"])
    
            elif opcao == "11":
                break
    
            else:
                print("Opção inválida.")
    
    
    # ==============================
    # MENU PROFESSOR
    # ==============================
    
    elif tipo_acesso == "professor":
    
        while True:
            print("\n===== MENU PROFESSOR =====")
            print("1 - Ver minhas matérias")
            print("2 - Alterar nota")
            print("3 - Lançar frequência")
            print("4 - Adicionar conteúdo")
            print("5 - Sair")
    
            opcao = input("Escolha: ")
    
            if opcao == "1":
                print("Suas matérias:", professor_logado["materias"])
    
            elif opcao == "2":
                nome = input("Nome do aluno: ")
                materia = input("Matéria: ")
    
                if materia not in professor_logado["materias"]:
                    print("Você não pode alterar essa matéria.")
                    continue
    
                for aluno in alunos:
                    if aluno["nome"] == nome and aluno["materia"] == materia:
                        nova_nota = float(input("Nova média: "))
                        aluno["media"] = round(nova_nota, 1)
                        salvar_dados("alunos.json", alunos)
                        print("Nota atualizada!")
                        break
    
            elif opcao == "3":
                nome = input("Nome do aluno: ")
                materia = input("Matéria: ")
    
                if materia not in professor_logado["materias"]:
                    print("Sem permissão.")
                    continue
    
                for aluno in alunos:
                    if aluno["nome"] == nome and aluno["materia"] == materia:
                        presenca = input("P ou F: ").upper()
                        aluno["frequencia"].append(presenca)
                        salvar_dados("alunos.json", alunos)
                        print("Frequência registrada!")
                        break
    
            elif opcao == "4":
                materia = input("Matéria: ")
    
                if materia not in professor_logado["materias"]:
                    print("Sem permissão.")
                    continue
    
                conteudo = input("Conteúdo: ")
    
                for aluno in alunos:
                    if aluno["materia"] == materia:
                        aluno["conteudos"].append(conteudo)
    
                salvar_dados("alunos.json", alunos)
                print("Conteúdo registrado!")
    
            elif opcao == "5":
                break
    
    
    # ==============================
    # MENU ALUNO
    # ==============================
    
    elif tipo_acesso == "aluno":
    
        while True:
            print("\n===== MENU ALUNO =====")
            print("1 - Ver notas")
            print("2 - Ver frequência")
            print("3 - Sair")
    
            opcao = input("Escolha: ")
    
            if opcao == "1":
                for aluno in alunos:
                    if aluno["nome"] == nome_aluno_logado:
                        print(aluno)
    
            elif opcao == "2":
                for aluno in alunos:
                    if aluno["nome"] == nome_aluno_logado:
                        print("Frequência:", aluno["frequencia"])
    
            elif opcao == "3":
                break
    
    else:
        print("Sistema bloqueado.")
    
