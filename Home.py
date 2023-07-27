from colorama import init, Fore, Style
import os
import subprocess

# Inicializar a biblioteca Colorama
init()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def home():
    while True:
        clear_screen()
        print(f"{Fore.RED}Eyer Of Security Group{Style.RESET_ALL}\n")
        print(f"{Fore.GREEN}Esse script foi feito para fins de estudos e educativos{Style.RESET_ALL}\n")
        print("Opções:")
        print("1 - Executar ferramenta1.py")
        print("2 - Opção 2")
        print("3 - Opção 3")
        print("4 - Opção 4")
        print("5 - Opção 5")
        print("0 - Sair do script.")
        choice = input("Digite o número da opção desejada: ")

        if choice == '1':
            try:
                subprocess.run(['python', 'ferramenta1.py'], check=True)
                input("Pressione Enter para continuar...")
            except FileNotFoundError:
                input("Arquivo 'ferramenta1.py' não encontrado. Pressione Enter para continuar...")
            except subprocess.CalledProcessError:
                input("Erro ao executar 'ferramenta1.py'. Pressione Enter para continuar...")
        elif choice == '2':
            # Lógica da opção 2
            input("Você escolheu a Opção 2. Pressione Enter para continuar...")
        elif choice == '3':
            # Lógica da opção 3
            input("Você escolheu a Opção 3. Pressione Enter para continuar...")
        elif choice == '4':
            # Lógica da opção 4
            input("Você escolheu a Opção 4. Pressione Enter para continuar...")
        elif choice == '5':
            # Lógica da opção 5
            input("Você escolheu a Opção 5. Pressione Enter para continuar...")
        elif choice == '0':
            print("Saindo do script...")
            break
        else:
            input("Opção inválida. Pressione Enter para continuar...")

if __name__ == "__main__":
    home()
