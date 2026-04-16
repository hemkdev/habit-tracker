import json # Para salvar e carregar dados
from datetime import date # Para registrar a data de conclusão
import os # Para verificar se o arquivo existe
import time # Para pausar a tela e dar feedback visual

# -- FUNÇÕES AUXILIARES -- #

def print_sucesso(mensagem):
    print(f"\033[92m{mensagem}\033[0m")

def print_erro(mensagem):
    print(f"\033[91m{mensagem}\033[0m")

def carregar_dados():
    if os.path.exists("habitos.json"):
        with open("habitos.json", "r") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}
    return {}

def adicionar_habito(habitos, nome):
    if nome not in habitos:
        habitos[nome] = []
        print_sucesso(f"Hábito '{nome}' adicionado e salvo com sucesso!")
        with open("habitos.json", "w") as arquivo:
            json.dump(habitos, arquivo)
        time.sleep(1.5) 
        os.system('cls' if os.name == 'nt' else 'clear')   
    else:
        print_erro("Esse hábito já existe!")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')

def listar_habitos(habitos):
    if not habitos:
        print("Nenhum hábito cadastrado!")
        input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    for nome, dias in habitos.items():
        print(f"- {nome} | Dias concluídos: {len(dias)}")
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def marcar_habitos(habitos, nome):
    hoje = str(date.today())
    if nome in habitos:
        if hoje not in habitos[nome]:
            habitos[nome].append(hoje)
            print_sucesso(f"Hábito '{nome}' marcado como concluído para hoje!")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print_erro(f"Hábito '{nome}' já foi marcado como concluído hoje!")
            input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
            print_erro("Hábito não encontrado!")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

def excluir_habito(habitos, nome):
    if nome in habitos:
        del habitos[nome]
        print_sucesso(f"Hábito '{nome}' excluído com sucesso!")
        input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print_erro("Hábito não encontrado!")
        input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

def salvar_dados(habitos):
    with open("habitos.json", "w") as arquivo:
        json.dump(habitos, arquivo)

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
        print("5. Limpar tela")
        print("6. Sair")
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
                os.system('cls')
            elif escolha == 6:
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