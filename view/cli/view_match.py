def show_match_current_round(match_list):
    for match in match_list:
        print(f"{match.name}: {match.players[0].last_name} {match.players[0].first_name} "
              f"contre {match.players[1].last_name} {match.players[1].first_name} \n"
              f"Score: {match.score[0]} - {match.score[1]}")
