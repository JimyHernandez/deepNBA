import sqlite3
import pandas
from nba_api.stats.endpoints import leaguedashplayerstats

def create_views(full_player_stats_df):
    player_table = full_player_stats_df[[
        "PLAYER_ID",
        "TEAM_ID",
        "PLAYER_NAME",
        "AGE"
    ]]

    teams_table = full_player_stats_df[[
        "TEAM_ID",
        "TEAM_ABBREVIATION"
    ]]

    player_stats_table = full_player_stats_df[[
        "PLAYER_ID",
        "GP",
        "W",
        "L",
        "W_PCT",
        "MIN",
        "FGM",
        "FGA",
        "FG_PCT",
        "FG3M",
        "FG3A",
        "FG3_PCT",
        "FTM",
        "FTA",
        "FT_PCT",
        "OREB",
        "DREB",
        "REB",
        "AST",
        "TOV",
        "STL",
        "BLK",
        "BLKA",
        "PF",
        "PFD",
        "PTS"
    ]]

    return player_table, teams_table, player_stats_table


def save_to_sql(player_table, teams_table, player_stats_table):
    connection = sqlite3.connect("./database/nba_stats.db")

    player_stats_table.to_sql(
    name = "player_stats",
    con = connection,
    if_exists = "replace",
    index = False
    )

    player_table.to_sql(
        name = "player",
        con = connection,
        if_exists = "replace",
        index = False
    )

    teams_table.to_sql(
        name = "teams",
        con = connection,
        if_exists = "replace",
        index = False
    )
    connection.commit()
    connection.close()

def main():
    stats = leaguedashplayerstats.LeagueDashPlayerStats(season = '2023-24')
    full_df = stats.get_data_frames()[0]
    player_table, teams_table, player_stats_table = create_views(full_df)
    save_to_sql(player_table, teams_table, player_stats_table)

if __name__ == "__main__":
    main()
