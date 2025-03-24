import sys
from colorama import Fore
from logger.logger import log_info, log_warning
from phone_book_service.service import add_contact, change_contact, get_contact_by_phone, list_all_contacts

def cmd_parser(cmd: str) -> str:
    command, *args = cmd.split()
    match command:
        case "exit" | "close":
            print(f"{Fore.BLUE}************** Goodbye! **************{Fore.RESET}")
            sys.exit(0)
        case "hello":
            log_info("Hello! I'm a phone book assistant. How can I help you?")
        case "add":
            add_contact(args)
        case "change":
            change_contact(args)
        case "phone":
            get_contact_by_phone(args)
        case "all":
            list_all_contacts()
        case "help":
            print("Available commands:\n"
            f"{Fore.CYAN}add {Fore.GREEN}[Name] [Phone Number]{Fore.RESET} - create new record\n"
            f"{Fore.CYAN}change {Fore.GREEN}[Name] [New Phone Number]{Fore.RESET} - change phone number by [Name]\n"
            f"{Fore.CYAN}phone {Fore.GREEN}[Phone Number]{Fore.RESET} - display owner name\n"
            f"{Fore.CYAN}all {Fore.RESET}- list all users with their number\n"
            f"{Fore.CYAN}help {Fore.RESET}- display commands list\n"
            f"{Fore.CYAN}exit | close {Fore.RESET}- close the program")
        case _:
            log_warning(f"Unknown command: [{Fore.RED}{command}{Fore.RESET}]. Please, use [{Fore.CYAN}help{Fore.RESET}] to see available commands.")