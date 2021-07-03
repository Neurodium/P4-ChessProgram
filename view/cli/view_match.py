def show_match_current_round(match_list):
    for match in range(len(match_list)):
        print(f"Match {match+1}: {match_list[match][0].last_name} {match_list[match][0].first_name} contre {match_list[match][1].last_name} {match_list[match][1].first_name}")