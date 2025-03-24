from pathlib import Path
from collections import Counter

def parsing_log_line(log_line: str) -> dict:
    logs = log_line.strip().split(" ")
    data, time, level = logs[:3]
    message = " ".join(logs[3:])
    return {
        "date": data,
        "time": time,
        "level": level,
        "message": message
    }

def load_logs(path: Path):
    with open(path, "r") as file:
        for line in file:
            parsed_line = parsing_log_line(line)
            yield parsed_line

def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    if level == "all":
        return logs

    return list(filter(lambda item: item["level"].lower() == level.lower(), logs))

def count_logs_by_level(logs: list[dict]) -> dict:
    return Counter(item["level"] for item in logs)

def display_log_counts(counted_logs: list[dict]):
    print("-" * 23)
    print(f"{'Log level':<12} | {'Quantity':>8}")
    print("-" * 23)
    for key, value in counted_logs.items():
        print(f"{key:<12} | {value:<8}")
    print("-"*23)

def display_provided_level_logs(logs: list[dict], level: str):
    print(f"Detailed logs for '{level}' level:")
    for item in logs:
        print(f"{item["date"] } {item["time"]} - {item["message"]}")

if __name__ == "__main__":
    print("Logs service")