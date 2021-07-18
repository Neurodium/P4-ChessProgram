from model.match import Match
from controller.controller_player import find_player_previous_match


# Create first round match sequences
def match_first_round(tournament_list, round_list, match_list):
    # check if it is the first round
    if len(match_list) == 0 and len(round_list) == 1:
        players_match = tournament_list[-1].players
        players_match = sorted(players_match,
                               key=lambda player: player.rank)
        half_list = int(len(players_match)/2)
        for player in range(half_list):
            match_list.append(Match(f"Match {player+1}",
                                    (players_match[player],
                                     players_match[player + half_list])))
    else:
        pass


# generates matches for new round
def match_next_round(tournament_list, round_list, match_list):
    # check if all matches of previous round have been played
    if len(match_list) == 0:
        players_match = tournament_list[-1].players
        players_match = sorted(players_match,
                               key=lambda player:
                               (player.tournament_points,
                                player.rank),
                               reverse=True)
        # check if player had already played against the other-
        if find_player_previous_match(players_match, round_list) is False:
            player = 0
            nb_match = 1
            while player < len(players_match):
                match_list.append(Match(f"Match {nb_match}",
                                        (players_match[player],
                                         players_match[player + 1])))
                player += 2
                nb_match += 1
        else:
            match_list.append(Match("Match 1",
                                    (players_match[0],
                                     players_match[2])))
            match_list.append(Match("Match 2",
                                    (players_match[1],
                                     players_match[3])))
            player = 4
            nb_match = 3
            while player < len(players_match):
                match_list.append(Match(f"Match {nb_match}",
                                        (players_match[player],
                                         players_match[player+1])))
                player += 2
                nb_match += 1
    else:
        pass


# add score to a match
def enter_match_score(match_list):
    # prompt if match's score need to be entered
    for match in match_list:
        answer = (input(f"Voulez-vous entrer les scores pour le {match.name} ? O/N")).capitalize()
        while answer not in ["O", "N"]:
            answer = (input("Veuillez choisir O ou N")).capitalize()
        if answer == "O":
            score_1 = 0
            score_2 = 0
            while score_1 + score_2 != 1.0:
                while True:
                    try:
                        score_1 = float(input(f"Score de {match.players[0].last_name} "
                                              f"{match.players[0].first_name} (0 / 0.5 / 1): "))
                        if score_1 in [0, 0.5, 1]:
                            break
                    except ValueError:
                        print("Veuillez choisir un chiffre entre 0 / 0.5 / 1")
                while True:
                    try:
                        score_2 = float(input(f"Score de {match.players[1].last_name} "
                                              f"{match.players[1].first_name} (0 / 0.5 / 1): "))
                        if score_2 in [0, 0.5, 1]:
                            break
                    except ValueError:
                        print("Veuillez choisir un chiffre entre 0 / 0.5 / 1")
                if score_1 + score_2 == 1.0:
                    match.score = [score_1, score_2]
                    break
                else:
                    print("Le score est incorrect")
    return match_list
