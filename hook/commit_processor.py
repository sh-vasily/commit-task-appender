import sys
import re


def try_parse_task_id(branch_name):
    numbers = re.findall(r'\d+', branch_name)
    return numbers[0] if len(numbers) > 0 else None

def insert_task_number(file_handler, task_id):
    commit_msg = file_handler.read()
    file_handler.seek(0, 0)
    file_handler.write(f'#{task_id} {commit_msg}')

def process_commit(branch_name, commit_msg_filepath):
    task_id = try_parse_task_id(branch_name)
    if task_id is None:
        return

    with open(commit_msg_filepath, 'r+') as fh:
        insert_task_number(fh, task_id)

def main():
    branch_name = sys.argv[1]
    commit_msg_filepath = sys.argv[2]

    process_commit(branch_name, commit_msg_filepath)
    sys.exit(0)

if __name__ == "__main__":
    main()
