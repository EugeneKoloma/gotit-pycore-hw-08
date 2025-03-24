from colorama import Fore
from logger.logger import log_warning, log_info
from decorators.error_logger import error_logger
import re

phone_lib = {}

def number_validator(phone: str) -> bool:
    phone_pattern = re.compile(r"^\+?3?8?(0\d{9})$|^0\d{9}$")
    return bool(phone_pattern.match(phone))

@error_logger
def add_contact(args: list[str]) -> None:
    name, phone = args[0], args[1]
    if (name in phone_lib):
        log_warning(f"Contact with name {Fore.RED}{name.capitalize()}{Fore.RESET} already exists. Use [{Fore.CYAN}change{Fore.RESET}] command to edit it.")
        return
    if not number_validator(phone):
        log_warning(f"Phone number [{Fore.RED}{phone}{Fore.RESET}] is not valid.")
        return
    phone_lib[name] = phone
    log_info(f"Contact {Fore.GREEN}{name.capitalize()}{Fore.RESET} with phone number {Fore.GREEN}{phone}{Fore.RESET} has been added.")

@error_logger
def change_contact(args) -> None:
    name, phone = args[0], args[1]
    phone_lib[name] = phone
    log_info(f"Contact {Fore.GREEN}{name.capitalize()}{Fore.RESET} has been updated with new phone number {Fore.GREEN}{phone}{Fore.RESET}.")

@error_logger
def get_contact_by_phone(args) -> None:
    phone = args[0]
    for name, number in phone_lib.items():
        if number == phone:
            log_info(f"Contact with phone number {Fore.GREEN}{phone}{Fore.RESET} belongs to {Fore.GREEN}{name.capitalize()}{Fore.RESET}.")
            return
    log_warning(f"No contact with phone number {Fore.RED}{phone}{Fore.RESET} found.")

def list_all_contacts() -> None:
    if not phone_lib:
        log_info(f"{Fore.RED}Phone book is empty.")
        return
    for name, phone in phone_lib.items():
        print(f"{Fore.GREEN}{name.capitalize()}{Fore.RESET}: {Fore.GREEN}{phone}{Fore.RESET}")
    
if __name__ == "__main__":
    print("This module is for phone book CRU operations.")