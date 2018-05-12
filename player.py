class Player:
    def __init__(self, firstName, lastName, teamID, teamName):
        self.firstName = firstName
        self.lastName = lastName
        self.teamID = teamID
        self.teamName = teamName

    def __str__(self):
        return self.lastName + ', ' + self.firstName


class Batter(Player):
    def __init__(self, firstName, lastName, avg):
        super().__init__(firstName, lastName)
        self.avg = avg


class Pitcher(Player):
    def __init__(self, firstName, lastName, era):
        super().__init__(firstName, lastName)
        self.era = era
