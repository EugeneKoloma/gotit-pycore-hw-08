from service_cmd import cmd_parser
from service_logs import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts, display_provided_level_logs

if __name__ == "__main__":
    file_path, log_level = cmd_parser()
    
    logs = [log for log in load_logs(file_path)]
    filtered_logs = filter_logs_by_level(logs, log_level)
    logs_counts_by_level = count_logs_by_level(logs)

    display_log_counts(logs_counts_by_level)
    if log_level and log_level != "all":
        display_provided_level_logs(filtered_logs, log_level)