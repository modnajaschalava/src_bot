from github import Github
from requests import get


def upload_file_to_git(filename, data_file, update=False):
    g = Github("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")
    repo = None
    for repo_ in g.get_user().get_repos():
        if repo_.name == 'telegram_bot':
            repo = repo_
    path = 'src/' + filename
    if update:
        contents = repo.get_contents(path, ref='main')
        repo.update_file(contents.path, 'add file', data_file, contents.sha, branch='main')
    else:
        try:
            repo.create_file(path, 'add file', data_file, branch='main')
        except:
            pass


def get_file_from_git(filename):
    directory = 'https://raw.githubusercontent.com/modnajaschalava/telegram_bot/main/src/'
    url = directory + filename.replace(' ', '%20')
    rec = get(url)
    return rec.content.strip()
