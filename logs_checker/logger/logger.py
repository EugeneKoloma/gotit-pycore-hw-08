from datetime import datetime as dt
from colorama import Fore
from decorators.write_log import write_log_to_file

time_output_pttrn = "%Y-%m-%d %H:%M:%S"

def logger() -> dict[str, callable]:
    time = dt.now().strftime(time_output_pttrn)
    
    @write_log_to_file
    def log_info(msg: str) -> None:
        print(f"{Fore.CYAN}{time} {Fore.GREEN}INFO {Fore.RESET}{msg}")
        return f"{time} INFO {msg}"
    
    @write_log_to_file
    def log_warning(msg: str) -> None:
        print(f"{Fore.CYAN}{time} {Fore.YELLOW}WARNING {Fore.RESET}{msg}")
        return f"{time} WARNING {msg}"
    
    @write_log_to_file
    def log_error(error_type: str, msg: str) -> None:
        print(f"{Fore.CYAN}{time} {Fore.RED}ERROR {Fore.RESET}{error_type}: {msg}")
        return f"{time} ERROR {error_type} {msg}"

    loggers = {
        "info": log_info,
        "warning": log_warning,
        "error": log_error
    }

    return loggers

LOG = logger()

if __name__ == "__main__":
    LOG["info"]("Starting process")
    LOG["warning"]("Something might be off...")
    LOG["error"]("SomeError", "Error message here")