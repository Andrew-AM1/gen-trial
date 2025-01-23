import os
import subprocess


def git_commit(repo_path, commit_message):
    os.chdir(repo_path)
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])


if __name__ == "__main__":
    repo_path = '/Users/andrew/trial'  # Change this to your repository path
    # Change this to your commit message
    commit_message = 'Automated commit message'
    git_commit(repo_path, commit_message)

# script to commit and push to git
# run this script in the terminal
# python test.py
# it will commit and push to the git
