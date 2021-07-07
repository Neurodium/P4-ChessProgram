def show_match_current_round(match_list):
    for match in range(len(match_list)):
        print(f"Match {match+1}: {match_list[match].players[0].last_name} {match_list[match].players[0].first_name} "
              f"contre {match_list[match].players[1].last_name} {match_list[match].players[1].first_name} \n"
              f"Score: {match_list[match].score[0]} - {match_list[match].score[1]}")