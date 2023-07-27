from colorama import init, Fore, Style

# Inicializar a biblioteca Colorama
init()

def home():
    print(f"{Fore.RED}Eyer Of Security Group{Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}Esse script foi feito para fins de estudos e educativos{Style.RESET_ALL}\n")
    print("Opções:")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("4 - Opção 4")
    print("5 - Opção 5")
    print("0 - Sair do script.")

if __name__ == "__main__":
    home()
