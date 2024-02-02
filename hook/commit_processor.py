import sys
import re
import os.path

class InsertTaskCodeProcessor:
    @staticmethod
    def get_prefix(branch_name):
        numbers = re.findall(r'\d+', branch_name)
        return numbers[0] if len(numbers) > 0 else None

class InsertBranchNameProcessor:
    @staticmethod
    def get_prefix(branch_name):
        return f"[{branch_name}]"

def insert_prefix(file_handler, prefix):
    commit_msg = file_handler.read()
    file_handler.seek(0, 0)
    file_handler.write(f'{prefix} {commit_msg}')

def get_processor(strategy):
    match strategy:
        case "insert_task_code":
            return InsertTaskCodeProcessor()
        case _:
            return InsertBranchNameProcessor()
        

def process_commit(strategy, branch_name, commit_msg_filepath):
    processor = get_processor(strategy)
    prefix= processor.get_prefix(branch_name)
    if prefix is None:
        return

    with open(commit_msg_filepath, 'r+') as fh:
        insert_prefix(fh, prefix)

def main():
    branch_name = sys.argv[1]
    commit_msg_filepath = sys.argv[2]

    conf_filename='proccessor.conf'
    strategy=""

    if os.path.exists(conf_filename):
        with open(conf_filename, 'r') as processor_conf:
            strategy=processor_conf.read()

    process_commit(strategy, branch_name, commit_msg_filepath)
    sys.exit(0)

if __name__ == "__main__":
    main()
