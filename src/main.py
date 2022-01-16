import requests
from src.model import faceit_player

app_auth_key = "bf8c2a3e-c583-4411-8e6d-dc14aaaa529b"
players_array = []
players_ids = open("players_ids.txt")


def get_user_data(user_id):
    faceit_response = requests.get(f"https://open.faceit.com/data/v4/players/{user_id}",
                                   headers={"Authorization": "Bearer " + app_auth_key,
                                            "Content-Type": "application/json"})
    return faceit_response.json()


def check_elo_difference(player_to_check):
    player_elo_difference = ""
    # getting last saved elo from array (DB)
    player_current_elo = player_to_check.player_elo  # We should get this information from DB on every iteration, right?

    # getting updated user information from faceit
    player_updated_info = get_user_data(player_to_check.player_id)

    # getting update user elo
    player_updated_elo = player_updated_info["games"]["csgo"]["faceit_elo"]

    if player_updated_elo != player_updated_elo:
        player_elo_difference = player_current_elo - player_updated_elo
    else:
        player_elo_difference = 0

    return player_elo_difference


for player in players_ids:
    user_info = get_user_data(player)
    current_player = faceit_player.Player(user_info["nickname"], user_info["player_id"],
                                          user_info["games"]["csgo"]["faceit_elo"])
    players_array.append(current_player)

for player in players_array:
    elo_difference = check_elo_difference(player)

    if elo_difference == 0:
        print(player.player_name + " stays on his level with " + str(player.player_elo) + " elo.")
    elif elo_difference < 0:
        print(player.player_name + " lost " + str(abs(elo_difference)) + " elo in the last game.")
    else:
        print(player.player_name + " gained " + str(elo_difference) + " elo in the last game.")
