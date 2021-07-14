from tinydb import TinyDB
from model.player import Player
db = TinyDB('db.json')

def save_players(player_list):
    players_table = db.table('players')
    players_table.truncate()
    players_save =[]
    for player in player_list:
        players_save.append({'last_name': player.last_name,
                             'first_name': player.first_name,
                             'birthdate': player.birthdate,
                             'gender': player.gender,
                             'rank': player.rank,
                             'tournament_points': player.tournament_points
                             })
    players_table.insert_multiple(players_save)

def save_tournaments(tournament_list):
    tournaments_table = db.table('tournaments')
    t_players_table = db.table('t_players')
    t_rounds_table = db.table('t_rounds')
    t_matchs_table = db.table('t_matchs')
    tournaments_table.truncate()
    t_players_table.truncate()
    t_rounds_table.truncate()
    t_matchs_table.truncate()
    tournaments_save = []
    t_players_save = []
    t_rounds_save = []
    t_matchs_save = []
    for tournament in tournament_list:
        tournaments_save.append({'name': tournament.name,
                             'place': tournament.place,
                             'date': tournament.date,
                             'time_control': tournament.time_control,
                             'description': tournament.description,
                             'nbtours': tournament.nbtours,
                             'max_players': tournament.max_players,
                             'closed': tournament.closed
                             })
        for player in tournament.players:
            t_players_save.append({'tournament_name': tournament.name,
                                 'last_name': player.last_name,
                                 'first_name': player.first_name,
                                 'birthdate': player.birthdate,
                                 'gender': player.gender,
                                 'rank': player.rank,
                                 'tournament_points': player.tournament_points
                                 })
            for round in tournament.rounds:
                t_rounds_save.append({'tournament_name': tournament.name,
                                    'name': round.name,
                                    'date_begin': round.date_begin,
                                    'date_end': round.date_end})
                for match in round.matchs_round:
                        t_matchs_save.append({'tournament_name': tournament.name,
                                            'match_name': match.name,
                                            'last_name_player_1': match.players[0].last_name,
                                            'first_name_player_1': match.players[0].first_name,
                                            'birthdate_player_1': match.players[0].birthdate,
                                            'gender_player_1': match.players[0].gender,
                                            'rank_player_1': match.players[0].rank,
                                            'tournament_points_player_1': match.players[0].tournament_points,
                                            'score_player_1': match.score[0],
                                            'last_name_player_2': match.players[1].last_name,
                                            'first_name_player_2': match.players[1].first_name,
                                            'birthdate_player_2': match.players[1].birthdate,
                                            'gender_player_2': match.players[1].gender,
                                            'rank_player_2': match.players[1].rank,
                                            'tournament_points_player_2': match.players[1].tournament_points,
                                            'score_player_2': match.score[1],
                                            })
    tournaments_table.insert_multiple(tournaments_save)
    t_players_table.insert_multiple(t_players_save)
    t_rounds_table.insert_multiple(t_rounds_table)
    t_matchs_table.insert_multiple(t_matchs_save)
    print("Données sauvegardées")



def load_players(player_list):
    player_list[:] = []
    players_table = db.table('players')
    players_load = players_table.all()
    for player in players_load:
        player_list.append(Player(player['last_name'],
                             player['first_name'],
                             player['birthdate'],
                             player['gender'],
                             player['rank'],
                             player['tournament_points']))
    print("Données chargées")
    return player_list