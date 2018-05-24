class Player:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


    def __str__(self):
        return self.lastName + ', ' + self.firstName


class Batter(Player):
    def __init__(self, firstName, lastName, hr):
        super().__init__(firstName, lastName)
        self.hr = hr


class Pitcher(Player):
    def __init__(self, firstName, lastName, era):
        super().__init__(firstName, lastName)
        self.era = era
