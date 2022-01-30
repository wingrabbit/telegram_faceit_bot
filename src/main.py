#test comment
import requests
from src.model import faceit_player

app_auth_key = "bf8c2a3e-c583-4411-8e6d-dc14aaaa529b"
players_array = []
players_ids = open("conf/players_ids.txt")


def get_user_data(user_id):
    faceit_response = requests.get(f"https://open.faceit.com/data/v4/players/{user_id}",
                                   headers={"Authorization": "Bearer " + app_auth_key,
                                            "Content-Type": "application/json"})
    return faceit_response.json()


for player in players_ids:
    user_info = get_user_data(player)
    current_player = faceit_player.Player(user_info["nickname"], user_info["player_id"],
                                          user_info["games"]["csgo"]["faceit_elo"])
    players_array.append(current_player)

for player in players_array:
    print(str(player))
