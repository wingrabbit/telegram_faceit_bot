class Player:
    def __init__(self, name, id, elo):
        self.player_name = name
        self.player_id = id
        self.player_elo = elo

    def __str__(self):
        return 'Id: '+ self.player_id + ', Name: '+self.player_name+', Elo:' + str(self.player_elo)