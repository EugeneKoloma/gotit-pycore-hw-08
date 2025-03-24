from functools import wraps
from colorama import Fore, Style
from colorama import Fore, Style
from colorama import Fore, Style

def error_logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f"{Fore.RED}Missing name or phone number.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Wrong arguments values.{Style.RESET_ALL}")
        except IndexError:
            print(f"{Fore.RED}Some arguments was not provided. {Fore.RESET}Please provide {Fore.CYAN}[name]{Fore.RESET} and {Fore.CYAN}[phone]{Fore.RESET}. Example: " \
                  f"{Fore.CYAN}add John +380112223344{Style.RESET_ALL}")
    
    return wrap