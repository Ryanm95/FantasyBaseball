import mlbgame
from player import Pitcher, Batter



def main():     # acts as main method
    cubsPlayers = []
    teams = mlbgame.teams()  # Grabs list of team objects

    for team in teams:      # just to test for now
        if team.club_common_name == 'Cubs':
            id = team.team_id
            # print(id, team.club_common_name, team.division)

    count = 0
    pid = 0
    # for team in teams:
    for i in range(4, 11):
        year = mlbgame.games(2015, i, home='Cubs', away='Cubs')
        games = mlbgame.combine_games(year)
        for game in games:
            try:
                cubsGameStats = mlbgame.player_stats(game.game_id).home_batting
                for p in cubsGameStats:
                    temp = p.name_display_first_last
                    f, l = p.name_display_first_last.split()
                    if not any(x.firstName + ' ' + x.lastName == temp for x in cubsPlayers):
                        if p.pos == 'P':        # is a pitcher
                            #print(p.name_display_first_last, 'pitcher')
                            pid += 1
                            #newPlayer = Pitcher(f, l, p.s_era)

                        else:
                            #print(p.name_display_first_last, p.pos, p.s_hr)
                            pid += 1
                            newPlayer = Batter(f, l, p.s_hr)
                            cubsPlayers.append(newPlayer)

                count += 1
                #print(game, count)
            except ValueError:
                print('No game found')

    for p in cubsPlayers:
        print(p, p.hr)

    print(len(cubsPlayers))



if __name__ == '__main__':      # main method
    main()
