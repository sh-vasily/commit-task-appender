import sys
import re


def parse_task_id(commit_message):
    return re.findall(r'\d+', commit_message)[0]


def main():
    message_file = sys.argv[1]
    commit_msg_filepath = sys.argv[2]

    task_id = parse_task_id(message_file)
    with open(commit_msg_filepath, 'r+') as fh:
        commit_msg = fh.read()
        fh.seek(0, 0)
        fh.write('#%s %s' % (task_id, commit_msg))
    sys.exit(0)


if __name__ == "__main__":
    main()
