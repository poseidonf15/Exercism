"""
Module to tally the results of a small football competition
"""
POINTS_INDEXING = {"MP": 0, "W": 1, "D": 2, "L": 3, "P": 4}
def tally(rows):
    """Function returns a table with football teams and their stats.

    Args:
        rows (list): List of matches played and their result.

    Returns:
        list: Table of results
    """
    table = ['Team                           | MP |  W |  D |  L |  P']
    teams = {}
    space_length = 31

    for row in rows:
        current_teams, match_result = row.split(";")[0:2], row.split(";")[2]
        for team in current_teams:
            if team not in teams:
                teams[team] = [0] * 5

            teams[team][POINTS_INDEXING["MP"]] += 1
        if match_result != "draw":
            winning_team_index = int(match_result == "loss")
            losing_team_index = int(match_result == "win")
            teams[current_teams[winning_team_index]][POINTS_INDEXING["W"]] += 1
            teams[current_teams[winning_team_index]][POINTS_INDEXING["P"]] += 3
            teams[current_teams[losing_team_index]][POINTS_INDEXING["L"]] += 1
        else:
            for team in current_teams:
                teams[team][POINTS_INDEXING["D"]] += 1
                teams[team][POINTS_INDEXING["P"]] += 1

    sorted_teams = sorted(teams.items(), key = lambda item: (-item[1][POINTS_INDEXING["P"]], item[0]))

    for team_name, team in sorted_teams:
        table.append(" |".join([f"{team_name:<{space_length - 1}}"] + [f"{stat:>3}" for stat in team]))

    return table