class Player:
    def __init__(self, name, id, elo, matches_count):
        self.name = name
        self.id = id
        self.elo = elo
        self.matches_count = matches_count

    def __str__(self):
        return 'Id: ' + self.id + ', Name: ' + self.name + ', Elo:' + str(
            self.elo) + ', Matches: ' + self.matches_count
