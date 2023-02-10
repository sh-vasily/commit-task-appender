import sys
import re
import subprocess

def main():
    messageFile = sys.argv[1]
    commit_msg_filepath = sys.argv[2]

    taskId = messageFile.split('/')[2]
    with open(commit_msg_filepath, 'r+') as fh:
    	commit_msg = fh.read()
    	fh.seek(0, 0)
    	fh.write('#%s %s' % (taskId, commit_msg))
    sys.exit(0)


if __name__ == "__main__":
    main()	