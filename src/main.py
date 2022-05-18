from src.model import faceit_player
import faceit_api

players_array = []
players_ids = open("players_ids.txt")


def check_elo_difference(player_to_check):
    player_elo_difference = ""

    # getting last saved elo from array (DB)
    player_current_elo = player_to_check.elo  # We should get this information from DB on every iteration, right?

    # getting updated user information from faceit
    player_updated_info = faceit_api.get_player_data(player_to_check.id, "")

    # getting update user elo
    player_updated_elo = player_updated_info["games"]["csgo"]["faceit_elo"]

    if player_current_elo != player_updated_elo:
        player_elo_difference = player_updated_elo - player_current_elo
    else:
        player_elo_difference = 0

    return player_elo_difference


for player in players_ids:
    # Getting user information from faceit endpoint (no additional parameters needed)
    user_info = faceit_api.get_player_data(player, "")

    # Getting player match statistics from faceit "/stats/csgo/" endpoint
    user_matches = faceit_api.get_player_data(player, "/stats/csgo")

    # Creating player with parameters: name, ID, ELO, matches
    current_player = faceit_player.Player(user_info["nickname"], user_info["player_id"],
                                          user_info["games"]["csgo"]["faceit_elo"], user_matches["lifetime"]["Matches"])

    players_array.append(current_player)

for player in players_array:
    elo_difference = check_elo_difference(player)

    if elo_difference == 0:
        # I assume, no point to post anything in this case
        print(player.name + " stays on his level with " + str(player.elo) + " elo.")
    elif elo_difference < 0:
        print(player.name + " lost " + str(abs(elo_difference)) + " elo in the last game.")
    else:
        print(player.name + " gained " + str(elo_difference) + " elo in the last game.")
