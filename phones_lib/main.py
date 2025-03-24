from colorama import Fore
from cmd_handler.cmd_controller import cmd_parser

def main():
    print(f"{Fore.BLUE}**** Welcome to the assistant bot! ****{Fore.RESET}")
    while True:
        command = input("Enter a command: ").strip().lower()
        cmd_parser(command)

if __name__ == "__main__":
    main()
