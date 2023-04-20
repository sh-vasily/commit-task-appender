import sys
import re


def parse_task_id(commit_message):
    return re.findall(r'\d+', commit_message)[0]

def insert_task_number(file_handler, task_id):
    commit_msg = file_handler.read()
    file_handler.seek(0, 0)
    file_handler.write(f'#{task_id} {commit_msg}')

def main():
    message_file = sys.argv[1]
    commit_msg_filepath = sys.argv[2]

    task_id = parse_task_id(message_file)
    with open(commit_msg_filepath, 'r+') as fh:
        insert_task_number(fh, task_id)
    sys.exit(0)


if __name__ == "__main__":
    main()
