import mlbgame
from player import *


def main():     # acts as main method
    cubsPlayers = []
    teams = mlbgame.teams()  # Grabs list of team objects

    for team in teams:
        if team.club_common_name == 'Cubs':
            id = team.team_id
            # print(id, team.club_common_name, team.division)

    count = 0
    # for team in teams:
    for i in range(3, 9):
        year = mlbgame.games(2015, i, home='Cubs', away='Cubs')
        games = mlbgame.combine_games(year)
        for game in games:
            try:
                cubsGameStats = mlbgame.player_stats(game.game_id)
                count += 1
                print(game, count)
            except ValueError:
                print('No game found')


if __name__ == '__main__':      # main method
    main()
