import sys
from argparse import ArgumentParser
from logger import logger
from pathlib import Path
from colorama import Fore, Style

def validate(file_path: Path, log_level: str) -> tuple[Path, str]:
    if not file_path.exists():
        logger["error"]("FileNotFound", f"File not found: {file_path}")
        sys.exit(1)

    valid_levels = ["debug", "info", "warning", "error", "all"]
    if log_level not in valid_levels:
        logger["warning"](f"Invalid log level: {log_level}. Defaulting to 'all'.")
        log_level = "all"

    return file_path, log_level

def cmd_parser() -> tuple[Path, str]:
    parser = ArgumentParser(
        description=f"{Fore.CYAN}CLI tool that takes a file path and log level.{Style.RESET_ALL}",
        epilog=f"{Fore.GREEN}Example: python main.py ./logs.log warning{Style.RESET_ALL}"
    )
    parser.add_argument(
        "file_path", 
        type=Path, 
        help=f"{Fore.YELLOW}Path to the input file{Style.RESET_ALL}"
    )
    parser.add_argument(
        "log_level", 
        nargs="?", 
        default="all", 
        help=f"{Fore.YELLOW}Log level (default: all){Style.RESET_ALL}"
    )

    args = parser.parse_args()
    file_path, log_level = validate(args.file_path, args.log_level.lower())

    logger["info"](f"Using file: {file_path}")
    logger["info"](f"Log level set to: {log_level}")

    return file_path, log_level


if __name__ == "__main__":
    try:
        file_path, log_level = cmd_parser()

    except FileNotFoundError as e:
        logger["error"]("FileNotFound", str(e))
        exit(1)

    except Exception as e:
        logger["error"](type(e).__name__, str(e))
        exit(1)