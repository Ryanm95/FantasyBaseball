import mlbgame

'''play = mlbgame.players(mlbgame.day(2015, 4, 12, home='Royals', away='Royals')[0].game_id)
a = mlbgame.box_score(mlbgame.day(2015, 4, 12, home='Royals', away='Royals')[0].game_id)
print(a.print_scoreboard())'''

'''for p in play.home_players:
    #if p.first == 'Albert':
    print(p.first, p.last, p.rbi)'''

teams = mlbgame.teams()         # Grabs list of team objects
pCount = 0

for team in teams:
    print(team)
    rost = mlbgame.roster(team.team_id).players

    for p in rost:
        pCount += 1
        print(p.name_display_first_last, pCount)
    #print("\n")

    '''for player in teams:
        print(player.name_display_first_last)'''