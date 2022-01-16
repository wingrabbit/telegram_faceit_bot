class Player:
    def __init__(self, name, id, elo, matches_count):
        self.player_name = name
        self.player_id = id
        self.player_elo = elo
        self.player_matches_count = matches_count

    def __str__(self):
        return 'Id: ' + self.player_id + ', Name: ' + self.player_name + ', Elo:' + str(
            self.player_elo) + ', Matches: ' + self.player_matches_count
