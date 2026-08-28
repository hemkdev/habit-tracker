import json # Manipulação de dados em json
from datetime import date # Data e hora atual
import os # Interação com sistema operacional
import time # pausas

ARQUIVO_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "habitos.json")

# -- FUNÇÕES AUXILIARES -- #

def print_sucesso(mensagem):
    print(f"\033[92m{mensagem}\033[0m")

def print_erro(mensagem):
    print(f"\033[91m{mensagem}\033[0m")

def pausar():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}
    return {}

def salvar_dados(habitos):
    with open(ARQUIVO_DADOS, "w") as arquivo:
        json.dump(habitos, arquivo)

def adicionar_habito(habitos, nome):
    if nome not in habitos:
        habitos[nome] = []
        salvar_dados(habitos)
        print_sucesso(f"Hábito '{nome}' adicionado e salvo com sucesso!")
    else:
        print_erro("Esse hábito já existe!")
    pausar()

def listar_habitos(habitos):
    if not habitos:
        print("Nenhum hábito cadastrado!")
        pausar()
        return
    for nome, dias in habitos.items():
        print(f"- {nome} | Dias concluídos: {len(dias)}")
    pausar()

def marcar_habitos(habitos, nome):
    hoje = str(date.today())
    if nome not in habitos:
        print_erro("Hábito não encontrado!")
    elif hoje in habitos[nome]:
        print_erro(f"Hábito '{nome}' já foi marcado como concluído hoje!")
    else:
        habitos[nome].append(hoje)
        salvar_dados(habitos)
        print_sucesso(f"Hábito '{nome}' marcado como concluído para hoje!")
    pausar()

def excluir_habito(habitos, nome):
    if nome in habitos:
        del habitos[nome]
        salvar_dados(habitos)
        print_sucesso(f"Hábito '{nome}' excluído com sucesso!")
    else:
        print_erro("Hábito não encontrado!")
    pausar()

# -- PROGRAMA PRINCIPAL -- 
def main():
    habitos = carregar_dados()  # Carrega os hábitos do arquivo JSON ou inicializa um dicionário vazio
    while True: 
        print("\033[94m ------------------------------------------------")
        print(" Bem-vindo ao Rastreador de Hábitos!")
        print(" ------------------------------------------------ \033[0m")
        print("1. Adicionar hábito")
        print("2. Listar hábitos") 
        print("3. Marcar hábito como concluído")
        print("4. Excluir hábito")
        print("5. Sair")
        try:
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                nome = str(input("Digite o nome do hábito que deseja adicionar: "))
                adicionar_habito(habitos, nome)
            elif escolha == 2:
                listar_habitos(habitos)
            elif escolha == 3:
                nome = input("Digite o nome do hábito que deseja marcar como concluido: ")
                marcar_habitos(habitos, nome)
            elif escolha == 4:
                nome = input("Digite o nome do hábito que deseja excluir: ")
                excluir_habito(habitos, nome)
            elif escolha == 5:
                salvar_dados(habitos)
                print_sucesso("Progresso salvo. Até mais!")
                break
            else:
                print_erro("Opção inválida, tente novamente!")
                
        except ValueError:
            print_erro("Entrada inválida, por favor insira um número correspondente às opções.")
            input("Pressione Enter para tentar novamente...")
            os.system('cls' if os.name == 'nt' else 'clear')

        
if __name__ == "__main__":
    main()
