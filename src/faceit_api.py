import requests
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / 'faceit_auth.env'
load_dotenv(dotenv_path=env_path)

FACEIT_API_URL = f"https://open.faceit.com/data/v4/players/"


def get_player_data(user_id, params):
    request_string = FACEIT_API_URL + user_id + params

    faceit_response = requests.get(request_string,
                                   headers={"Authorization": "Bearer " + os.environ['APP_AUTH_KEY'],
                                            "Content-Type": "application/json"})

    return faceit_response.json()
