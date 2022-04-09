import yaml
import json

from helpers import github_helper


def get_token_tg():
    with open('helpers/settings.yaml', encoding='utf-8') as file:
        parameters = yaml.safe_load(file)
        return parameters.get('telegram_api_token')


def save_data(last_info):
    with open('data.json', 'r') as file:
        content = json.load(file)
    content[last_info['name'] + '_' + last_info['author']] = last_info['text']
    with open('data.json', 'w') as file:
        json.dump(content, file)
    github_helper.upload_file_to_git('data.json', str(content).replace('\'', '"'), True)
