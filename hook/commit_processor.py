import sys
import re
import os.path


def insert_prefix(file_handler, prefix):
    commit_msg = file_handler.read()
    file_handler.seek(0, 0)
    file_handler.write(f'{prefix} {commit_msg}')


def get_prefix(strategy, branch_name):
    match strategy:
        case "insert_task_code":
            numbers = re.findall(r'\d+', branch_name)
            return f"#{numbers[0]}" if len(numbers) > 0 else None
        case _:
            return f"[{branch_name}]"


def process_commit(strategy, branch_name, commit_msg_filepath):
    prefix = get_prefix(strategy, branch_name)
    if prefix is None:
        return

    with open(commit_msg_filepath, 'r+') as fh:
        insert_prefix(fh, prefix)


def main():
    branch_name = sys.argv[1]
    commit_msg_filepath = sys.argv[2]

    conf_filename = os.path.join(os.getcwd(), ".git", "hooks", "processor.conf")
    strategy = ""

    if os.path.exists(conf_filename):
        with open(conf_filename, 'r') as processor_conf:
            strategy = processor_conf.read().strip()

    process_commit(strategy, branch_name, commit_msg_filepath)
    sys.exit(0)


if __name__ == "__main__":
    main()
