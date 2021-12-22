import requests
import json
import os
import yaml
from config import Config

with open("config.yaml", "r") as f:
    conf = Config(yaml.safe_load(f))


def get_token():
    res = requests.post(conf.auth_path, json=conf.credentials).json()
    return res.get("access_token")


def get_data(date, token):
    payload = {"date": date}
    headers = {'Authorization': f'JWT {token}'}
    return requests.get(conf.service_path, headers=headers, json=payload).json()


def save_data(jsn, filename: str):
    main_dir = 'storage'
    path = f'{main_dir}/{filename}'

    if not os.path.exists(path):
        os.makedirs(path)

    with open(f'{path}/{filename}.json', 'w') as file:
        json.dump(jsn, file, indent=6)


if __name__ == '__main__':
    d = '2021-12-16'
    jwt = get_token()
    response = get_data(d, jwt)
    save_data(response, d)
