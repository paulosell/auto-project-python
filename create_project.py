from github import Github
import sys

folderName = str(sys.argv[1])
token = open("token-git.txt").read()
user = Github(token).get_user()
repo = user.create_repo(folderName)
