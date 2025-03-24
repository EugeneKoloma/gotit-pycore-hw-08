from pathlib import Path
from functools import wraps

def write_log_to_file(func):
    log_file = Path("./my_loggs.log")
    if not log_file.exists():
        log_file.touch()

    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(log_file, "a") as file:
            result = func(*args, **kwargs)
            file.write(f"{result}\n")

    return wrapper

if __name__ == "__main__":
    pass