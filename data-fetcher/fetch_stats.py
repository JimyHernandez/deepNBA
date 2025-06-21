import sqlite3
import pandas
from nba_api.stats.endpoints import leaguedashplayerstats

def get_league_stats(season='2023-24'):
    stats = leaguedashplayerstats.LeagueDashPlayerStats(season)
    return stats.get_data_frames()[0]

def create_views(df):
    player_table = df[[
        "PLAYER_ID",
        "PLAYER_NAME",
        "TEAM_ID",
        "AGE"
    ]]

    teams_table = df[[
        "TEAM_ID",
        "TEAM_ABBREVIATION"
    ]]

    player_stats_table = df[[
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

    return player_table, player_stats_table, teams_table

def save_to_sql(teams_df, player_df, stats_df, db_path = "./database/nba_stats.db"):
    conn = sqlite3.connect(db_path)

    stats_df.to_sql(
        name = "player_stats",
        con = conn,
        if_exists = "replace",
        index = False
    )

    player_df.to_sql(
        name = "player",
        con = conn,
        if_exists = "replace",
        index = False
    )

    teams_df.to_sql(
        name = "teams",
        con = conn,
        if_exists = "replace",
        index = False
    )

    conn.commit()
    conn.close()

def main():
    full_df = get_league_stats()
    player_df, team_df, stats_df = create_views(full_df)
    save_to_sql(player_df, team_df, stats_df)


if __name__ == "__main__":
    main()