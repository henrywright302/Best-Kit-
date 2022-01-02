# Whats the best kit?
# Need:
#   List of top 1000 players -> read into list off plancke
    # Also need their UUIDs
#   Read in wins, losses, and kills for each kit -> API? otherwise plancke also

#   Most used kit (num of total games played)
#   Best overall W/L, K/D
import requests
import xlwt
from xlwt import Workbook


def getData(ign, uuid):
    data = requests.get(
        url = "https://api.hypixel.net/player",
        params = {
          "key": "1cf1453f-fa64-4700-8ee8-25645431eec3", #24118s API key UUID: 6edc2962-6755-4f93-8945-9af0e8010b99
          "uuid": uuid
        }
    ).json()


    try:
        player_arachnologist_kills = data["player"]["stats"]["HungerGames"]["kills_arachnologist"]
    except KeyError:
        player_arachnologist_kills = 0
    try:
        player_arachnologist_wins_solo = data["player"]["stats"]["HungerGames"]["wins_arachnologist"]
    except KeyError:
        player_arachnologist_wins_solo = 0
    try:
        player_arachnologist_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_arachnologist"]
    except KeyError:
        player_arachnologist_wins_teams = 0
    player_arach_wins = int(player_arachnologist_wins_solo) + int(player_arachnologist_wins_teams)
    try:
        player_arach_games = data["player"]["stats"]["HungerGames"]["games_played_arachnologist"]
    except KeyError:
        player_arach_games = 0
    
    try:
        player_archer_kills = data["player"]["stats"]["HungerGames"]["kills_archer"]
    except KeyError:
        player_archer_kills = 0
    try:
        player_archer_wins_solo = data["player"]["stats"]["HungerGames"]["wins_archer"]
    except KeyError:
        player_archer_wins_solo = 0
    try:
        player_archer_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_archer"]
    except KeyError:
        player_archer_wins_teams = 0
    player_archer_wins = int(player_archer_wins_solo) + int(player_archer_wins_teams)
    try:
        player_archer_games = data["player"]["stats"]["HungerGames"]["games_played_archer"]
    except KeyError:
        player_archer_games = 0
    
    try:
        player_armorer_kills = data["player"]["stats"]["HungerGames"]["kills_armorer"]
    except KeyError:
        player_armorer_kills = 0
    try:
        player_armorer_wins_solo = data["player"]["stats"]["HungerGames"]["wins_armorer"]
    except KeyError:
        player_armorer_wins_solo = 0
    try:
        player_armorer_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_armorer"]
    except KeyError:
        player_armorer_wins_teams = 0
    player_armorer_wins = int(player_armorer_wins_solo) + int(player_armorer_wins_teams)
    try:
        player_armorer_games = data["player"]["stats"]["HungerGames"]["games_played_armorer"]
    except KeyError:
        player_armorer_games = 0
    
    try:
        player_astro_kills = data["player"]["stats"]["HungerGames"]["kills_astronaut"]
    except KeyError:
        player_astro_kills = 0
    try:
        player_astro_wins_solo = data["player"]["stats"]["HungerGames"]["wins_astronaut"]
    except KeyError:
        player_astro_wins_solo = 0
    try:
        player_astro_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_astronaut"]
    except KeyError:
        player_astro_wins_teams = 0
    player_astro_wins = int(player_astro_wins_solo) + int(player_astro_wins_teams)
    try:
        player_astro_games = data["player"]["stats"]["HungerGames"]["games_played_astronaut"]
    except KeyError:
        player_astro_games = 0
    
    try:
        player_baker_kills = data["player"]["stats"]["HungerGames"]["kills_baker"]
    except KeyError:
        player_baker_kills = 0
    try:
        player_baker_wins_solo = data["player"]["stats"]["HungerGames"]["wins_baker"]
    except KeyError:
        player_baker_wins_solo = 0
    try:
        player_baker_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_baker"]
    except KeyError:
        player_baker_wins_teams = 0
    player_baker_wins = int(player_baker_wins_solo) + int(player_baker_wins_teams)
    try:
        player_baker_games = data["player"]["stats"]["HungerGames"]["games_played_baker"]
    except KeyError:
        player_baker_games = 0
    
    try:
        player_blaze_kills = data["player"]["stats"]["HungerGames"]["kills_blaze"]
    except KeyError:
        player_blaze_kills = 0
    try:
        player_blaze_wins_solo = data["player"]["stats"]["HungerGames"]["wins_blaze"]
    except KeyError:
        player_blaze_wins_solo = 0
    try:
        player_blaze_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_blaze"]
    except KeyError:
        player_blaze_wins_teams = 0
    player_blaze_wins = int(player_blaze_wins_solo) + int(player_blaze_wins_teams)
    try:
        player_blaze_games = data["player"]["stats"]["HungerGames"]["games_played_blaze"]
    except KeyError:
        player_blaze_games = 0
    
    try:
        player_creepertamer_kills = data["player"]["stats"]["HungerGames"]["kills_creepertamer"]
    except KeyError:
        player_creepertamer_kills = 0
    try:
        player_creepertamer_wins_solo = data["player"]["stats"]["HungerGames"]["wins_creepertamer"]
    except KeyError:
        player_creepertamer_wins_solo = 0
    try:
        player_creepertamer_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_creepertamer"]
    except KeyError:
        player_creepertamer_wins_teams = 0
    player_creepertamer_wins = int(player_creepertamer_wins_solo) + int(player_creepertamer_wins_teams)
    try:
        player_creepertamer_games = data["player"]["stats"]["HungerGames"]["games_played_creepertamer"]
    except KeyError:
        player_creepertamer_games = 0
   
    try:
        player_diver_kills = data["player"]["stats"]["HungerGames"]["kills_diver"]
    except KeyError:
        player_diver_kills = 0
    try:
        player_diver_wins_solo = data["player"]["stats"]["HungerGames"]["wins_diver"]
    except KeyError:
        player_diver_wins_solo = 0
    try:
        player_diver_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_diver"]
    except KeyError:
        player_diver_wins_teams = 0
    player_diver_wins = int(player_diver_wins_solo) + int(player_diver_wins_teams)
    try:
        player_diver_games = data["player"]["stats"]["HungerGames"]["games_played_diver"]
    except KeyError:
        player_diver_games = 0
    
    try:
        player_donkey_kills = data["player"]["stats"]["HungerGames"]["kills_donkeytamer"]
    except KeyError:
        player_donkey_kills = 0
    try:
        player_donkey_wins_solo = data["player"]["stats"]["HungerGames"]["wins_donkeytamer"]
    except KeyError:
        player_donkey_wins_solo = 0
    try:
        player_donkey_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_donkeytamer"]
    except KeyError:
        player_donkey_wins_teams = 0
    player_donkey_wins = int(player_donkey_wins_solo) + int(player_donkey_wins_teams)
    try:
        player_donkey_games = data["player"]["stats"]["HungerGames"]["games_played_donkeytamer"]
    except KeyError:
        player_donkey_games = 0
    
    try:
        player_farmer_kills = data["player"]["stats"]["HungerGames"]["kills_farmer"]
    except KeyError:
        player_farmer_kills = 0
    try:
        player_farmer_wins_solo = data["player"]["stats"]["HungerGames"]["wins_farmer"]
    except KeyError:
        player_farmer_wins_solo = 0
    try:
        player_farmer_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_farmer"]
    except KeyError:
        player_farmer_wins_teams = 0
    player_farmer_wins = int(player_farmer_wins_solo) + int(player_farmer_wins_teams)
    try:
        player_farmer_games = data["player"]["stats"]["HungerGames"]["games_played_farmer"]
    except KeyError:
        player_farmer_games = 0
    
    try:
        player_fish_kills = data["player"]["stats"]["HungerGames"]["kills_fisherman"]
    except KeyError:
        player_fish_kills = 0
    try:
        player_fish_wins_solo = data["player"]["stats"]["HungerGames"]["wins_fisherman"]
    except KeyError:
        player_fish_wins_solo = 0
    try:
        player_fish_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_fisherman"]
    except KeyError:
        player_fish_wins_teams = 0
    player_fish_wins = int(player_fish_wins_solo) + int(player_fish_wins_teams)
    try:
        player_fish_games = data["player"]["stats"]["HungerGames"]["games_played_fisherman"]
    except KeyError:
        player_fish_games = 0
    
    try:
        player_florist_kills = data["player"]["stats"]["HungerGames"]["kills_florist"]
    except KeyError:
        player_florist_kills = 0
    try:
        player_florist_wins_solo = data["player"]["stats"]["HungerGames"]["wins_florist"]
    except KeyError:
        player_florist_wins_solo = 0
    try:
        player_florist_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_florist"]
    except KeyError:
        player_florist_wins_teams = 0
    player_florist_wins = int(player_florist_wins_solo) + int(player_florist_wins_teams)
    try:
        player_florist_games = data["player"]["stats"]["HungerGames"]["games_played_florist"]
    except KeyError:
        player_florist_games = 0
    
    try:
        player_golem_kills = data["player"]["stats"]["HungerGames"]["kills_golem"]
    except KeyError:
        player_golem_kills = 0
    try:
        player_golem_wins_solo = data["player"]["stats"]["HungerGames"]["wins_golem"]
    except KeyError:
        player_golem_wins_solo = 0
    try:
        player_golem_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_golem"]
    except KeyError:
        player_golem_wins_teams = 0
    player_golem_wins = int(player_golem_wins_solo) + int(player_golem_wins_teams)
    try:
        player_golem_games = data["player"]["stats"]["HungerGames"]["games_played_golem"]
    except KeyError:
        player_golem_games = 0
    
    try:
        player_guardian_kills = data["player"]["stats"]["HungerGames"]["kills_guardian"]
    except KeyError:
        player_guardian_kills = 0
    try:
        player_guardian_wins_solo = data["player"]["stats"]["HungerGames"]["wins_guardian"]
    except KeyError:
        player_guardian_wins_solo = 0
    try:
        player_guardian_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_guardian"]
    except KeyError:
        player_guardian_wins_teams = 0
    player_guardian_wins = int(player_guardian_wins_solo) + int(player_guardian_wins_teams)
    try:
        player_guardian_games = data["player"]["stats"]["HungerGames"]["games_played_guardian"]
    except KeyError:
        player_guardian_games = 0
    
    try:
        player_horse_kills = data["player"]["stats"]["HungerGames"]["kills_horsetamer"]
    except KeyError:
        player_horse_kills = 0
    try:
        player_horse_wins_solo = data["player"]["stats"]["HungerGames"]["wins_horsetamer"]
    except KeyError:
        player_horse_wins_solo = 0
    try:
        player_horse_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_horsetamer"]
    except KeyError:
        player_horse_wins_teams = 0
    player_horse_wins = int(player_horse_wins_solo) + int(player_horse_wins_teams)
    try:
        player_horse_games = data["player"]["stats"]["HungerGames"]["games_played_horsetamer"]
    except KeyError:
        player_horse_games = 0
    
  
    try:
        player_hunter_kills = data["player"]["stats"]["HungerGames"]["kills_hunter"]
    except KeyError:
        player_hunter_kills = 0
    try:
        player_hunter_wins_solo = data["player"]["stats"]["HungerGames"]["wins_hunter"]
    except KeyError:
        player_hunter_wins_solo = 0
    try:
        player_hunter_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_hunter"]
    except KeyError:
        player_hunter_wins_teams = 0
    player_hunter_wins = int(player_hunter_wins_solo) + int(player_hunter_wins_teams)
    try:  
        player_hunter_games = data["player"]["stats"]["HungerGames"]["games_played_hunter"]
    except KeyError:
        player_hunter_games = 0
    
    try:
        player_hype_kills = data["player"]["stats"]["HungerGames"]["kills_hype train"]
    except KeyError:
        player_hype_kills = 0
    try:
        player_hype_wins_solo = data["player"]["stats"]["HungerGames"]["wins_hype train"]
    except KeyError:
        player_hype_wins_solo = 0
    try:
        player_hype_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_hype train"]
    except KeyError:
        player_hype_wins_teams = 0
    player_hype_wins = int(player_hype_wins_solo) + int(player_hype_wins_teams)
    try:
        player_hype_games = data["player"]["stats"]["HungerGames"]["games_played_hype train"]
    except KeyError:
        player_hype_games = 0
    
    try:
        player_jockey_kills = data["player"]["stats"]["HungerGames"]["kills_jockey"]
    except KeyError:
        player_jockey_kills = 0
    try:
        player_jockey_wins_solo = data["player"]["stats"]["HungerGames"]["wins_jockey"]
    except KeyError:
        player_jockey_wins_solo = 0
    try:
        player_jockey_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_jockey"]
    except KeyError:
        player_jockey_wins_teams = 0
    player_jockey_wins = int(player_jockey_wins_solo) + int(player_jockey_wins_teams)
    try:
        player_jockey_games = data["player"]["stats"]["HungerGames"]["games_played_jockey"]
    except KeyError:
        player_jockey_games = 0
    
    try:
        player_knight_kills = data["player"]["stats"]["HungerGames"]["kills_knight"]
    except KeyError:
        player_knight_kills = 0
    try:
        player_knight_wins_solo = data["player"]["stats"]["HungerGames"]["wins_knight"]
    except KeyError:
        player_knight_wins_solo = 0
    try:
        player_knight_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_knight"]
    except KeyError:
        player_knight_wins_teams = 0
    player_knight_wins = int(player_knight_wins_solo) + int(player_knight_wins_teams)
    try:
        player_knight_games = data["player"]["stats"]["HungerGames"]["games_played_knight"]
    except KeyError:
        player_knight_games = 0
    
    try:
        player_meat_kills = data["player"]["stats"]["HungerGames"]["kills_meatmaster"]
    except KeyError:
        player_meat_kills = 0
    try:
        player_meat_wins_solo = data["player"]["stats"]["HungerGames"]["wins_meatmaster"]
    except KeyError:
        player_meat_wins_solo = 0
    try:
        player_meat_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_meatmaster"]
    except KeyError:
        player_meat_wins_teams = 0
    player_meat_wins = int(player_meat_wins_solo) + int(player_meat_wins_teams)
    try:
        player_meat_games = data["player"]["stats"]["HungerGames"]["games_played_meatmaster"]
    except KeyError:
        player_meat_games = 0
    
    try:
        player_necromancer_kills = data["player"]["stats"]["HungerGames"]["kills_necromancer"]
    except KeyError:
        player_necromancer_kills = 0
    try:
        player_necromancer_wins_solo = data["player"]["stats"]["HungerGames"]["wins_necromancer"]
    except KeyError:
        player_necromancer_wins_solo = 0
    try:
        player_necromancer_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_necromancer"]
    except KeyError:
        player_necromancer_wins_teams = 0
    player_necromancer_wins = int(player_necromancer_wins_solo) + int(player_necromancer_wins_teams)
    try:
        player_necromancer_games = data["player"]["stats"]["HungerGames"]["games_played_necromancer"]
    except KeyError:
        player_necromancer_games = 0
    
    try:
        player_paladin_kills = data["player"]["stats"]["HungerGames"]["kills_paladin"]
    except KeyError:
        player_paladin_kills = 0
    try:
        player_paladin_wins_solo = data["player"]["stats"]["HungerGames"]["wins_paladin"]
    except KeyError:
        player_paladin_wins_solo = 0
    try:
        player_paladin_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_paladin"]
    except KeyError:
        player_paladin_wins_teams = 0
    player_paladin_wins = int(player_paladin_wins_solo) + int(player_paladin_wins_teams)
    try:
        player_paladin_games = data["player"]["stats"]["HungerGames"]["games_played_paladin"]
    except KeyError:
        player_paladin_games = 0 
    
    try:
        player_phoenix_kills = data["player"]["stats"]["HungerGames"]["kills_phoenix"]
    except KeyError:
        player_phoenix_kills = 0
    try:
        player_phoenix_wins_solo = data["player"]["stats"]["HungerGames"]["wins_phoenix"]
    except KeyError:
        player_phoenix_wins_solo = 0
    try:
        player_phoenix_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_phoenix"]
    except KeyError:
        player_phoenix_wins_teams = 0
    player_phoenix_wins = int(player_phoenix_wins_solo) + int(player_phoenix_wins_teams)
    try:
        player_phoenix_games = data["player"]["stats"]["HungerGames"]["games_played_phoenix"]
    except KeyError:
        player_phoenix_games = 0
    
    try:
        player_pigman_kills = data["player"]["stats"]["HungerGames"]["kills_pigman"]
    except KeyError:
        player_pigman_kills = 0
    try:
        player_pigman_wins_solo = data["player"]["stats"]["HungerGames"]["wins_pigman"]
    except KeyError:
        player_pigman_wins_solo = 0
    try:
        player_pigman_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_pigman"]
    except KeyError:
        player_pigman_wins_teams = 0
    player_pigman_wins = int(player_pigman_wins_solo) + int(player_pigman_wins_teams)
    try:
        player_pigman_games = data["player"]["stats"]["HungerGames"]["games_played_pigman"]
    except KeyError:
        player_pigman_games = 0

    try:
        player_ranger_kills = data["player"]["stats"]["HungerGames"]["kills_ranger"]
    except KeyError:
        player_ranger_kills = 0
    try:
        player_ranger_wins_solo = data["player"]["stats"]["HungerGames"]["wins_ranger"]
    except KeyError:
        player_ranger_wins_solo = 0
    try:
        player_ranger_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_ranger"]
    except KeyError:
        player_ranger_wins_teams = 0
    player_ranger_wins = int(player_ranger_wins_solo) + int(player_ranger_wins_teams)
    try:
        player_ranger_games = data["player"]["stats"]["HungerGames"]["games_played_ranger"]
    except KeyError:
        player_ranger_games = 0
    
    try:
        player_reaper_kills = data["player"]["stats"]["HungerGames"]["kills_reaper"]
    except KeyError:
        player_reaper_kills = 0
    try:
        player_reaper_wins_solo = data["player"]["stats"]["HungerGames"]["wins_reaper"]
    except KeyError:
        player_reaper_wins_solo = 0
    try:
        player_reaper_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_reaper"]
    except KeyError:
        player_reaper_wins_teams = 0
    player_reaper_wins = int(player_reaper_wins_solo) + int(player_reaper_wins_teams)
    try:
        player_reaper_games = data["player"]["stats"]["HungerGames"]["games_played_reaper"]
    except KeyError:
        player_reaper_games = 0
        
    try:
        player_reddragon_kills = data["player"]["stats"]["HungerGames"]["kills_reddragon"]
    except KeyError:
        player_reddragon_kills = 0
    try:
        player_reddragon_wins_solo = data["player"]["stats"]["HungerGames"]["wins_reddragon"]
    except KeyError:
        player_reddragon_wins_solo = 0
    try:
        player_reddragon_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_reddragon"]
    except KeyError:
        player_reddragon_wins_teams = 0
    player_reddragon_wins = int(player_reddragon_wins_solo) + int(player_reddragon_wins_teams)
    try:
        player_reddragon_games = data["player"]["stats"]["HungerGames"]["games_played_reddragon"]
    except KeyError:
        player_reddragon_games = 0
    
    try:
        player_rogue_kills = data["player"]["stats"]["HungerGames"]["kills_rogue"]
    except KeyError:
        player_rogue_kills = 0
    try:
        player_rogue_wins_solo = data["player"]["stats"]["HungerGames"]["wins_rogue"]
    except KeyError:
        player_rogue_wins_solo = 0
    try:
        player_rogue_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_rogue"]
    except KeyError:
        player_rogue_wins_teams = 0
    player_rogue_wins = int(player_rogue_wins_solo) + int(player_rogue_wins_teams)
    try:
        player_rogue_games = data["player"]["stats"]["HungerGames"]["games_played_rogue"]
    except KeyError:
        player_rogue_games = 0
    
    try:
        player_scout_kills = data["player"]["stats"]["HungerGames"]["kills_scout"]
    except KeyError:
        player_scout_kills = 0
    try:
        player_scout_wins_solo = data["player"]["stats"]["HungerGames"]["wins_scout"]
    except KeyError:
        player_scout_wins_solo = 0
    try:
        player_scout_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_scout"]
    except KeyError:
        player_scout_wins_teams = 0
    player_scout_wins = int(player_scout_wins_solo) + int(player_scout_wins_teams)
    try:
        player_scout_games = data["player"]["stats"]["HungerGames"]["games_played_scout"]
    except KeyError:
        player_scout_games = 0
    
    try:
        player_sk_kills = data["player"]["stats"]["HungerGames"]["kills_shadow knight"]
    except KeyError:
        player_sk_kills = 0
    try:
        player_sk_wins_solo = data["player"]["stats"]["HungerGames"]["wins_shadow knight"]
    except KeyError:
        player_sk_wins_solo = 0
    try:
        player_sk_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_shadow knight"]
    except KeyError:
        player_sk_wins_teams = 0
    player_sk_wins = int(player_sk_wins_solo) + int(player_sk_wins_teams)
    try:
        player_sk_games = data["player"]["stats"]["HungerGames"]["games_played_shadow knight"]
    except KeyError:
        player_sk_games = 0
    
    try:
        player_slime_kills = data["player"]["stats"]["HungerGames"]["kills_slimeyslime"]
    except KeyError:
        player_slime_kills = 0
    try:
        player_slime_wins_solo = data["player"]["stats"]["HungerGames"]["wins_slimeyslime"]
    except KeyError:
        player_slime_wins_solo = 0
    try:
        player_slime_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_slimeyslime"]
    except KeyError:
        player_slime_wins_teams = 0
    player_slime_wins = int(player_slime_wins_solo) + int(player_slime_wins_teams)
    try:
        player_slime_games = data["player"]["stats"]["HungerGames"]["games_played_slimeyslime"]
    except KeyError:
        player_slime_games = 0
    
    try:
        player_snowman_kills = data["player"]["stats"]["HungerGames"]["kills_snowman"]
    except KeyError:
        player_snowman_kills = 0
    try:
        player_snowman_wins_solo = data["player"]["stats"]["HungerGames"]["wins_snowman"]
    except KeyError:
        player_snowman_wins_solo = 0
    try:
        player_snowman_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_snowman"]
    except KeyError:
        player_snowman_wins_teams = 0
    player_snowman_wins = int(player_snowman_wins_solo) + int(player_snowman_wins_teams)
    try:
        player_snowman_games = data["player"]["stats"]["HungerGames"]["games_played_snowman"]
    except KeyError:
        player_snowman_games = 0
    
    try:
        player_speleologist_kills = data["player"]["stats"]["HungerGames"]["kills_speleologist"]
    except KeyError:
        player_speleologist_kills = 0
    try:
        player_speleologist_wins_solo = data["player"]["stats"]["HungerGames"]["wins_speleologist"]
    except KeyError:
        player_speleologist_wins_solo = 0
    try:
        player_speleologist_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_speleologist"]
    except KeyError:
        player_speleologist_wins_teams = 0
    player_speleologist_wins = int(player_speleologist_wins_solo) + int(player_speleologist_wins_teams)
    try:
        player_speleologist_games = data["player"]["stats"]["HungerGames"]["games_played_speleologist"]
    except KeyError:
        player_speleologist_games = 0
    
    try:
        player_tim_kills = data["player"]["stats"]["HungerGames"]["kills_tim"]
    except KeyError:
        player_tim_kills = 0
    try:
        player_tim_wins_solo = data["player"]["stats"]["HungerGames"]["wins_tim"]
    except KeyError:
        player_tim_wins_solo = 0
    try:
        player_tim_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_tim"]
    except KeyError:
        player_tim_wins_teams = 0
    player_tim_wins = int(player_tim_wins_solo) + int(player_tim_wins_teams)
    try:
        player_tim_games = data["player"]["stats"]["HungerGames"]["games_played_tim"]
    except KeyError:
        player_tim_games = 0
    
    try:
        player_toxicologist_kills = data["player"]["stats"]["HungerGames"]["kills_toxicologist"]
    except KeyError:
        player_toxicologist_kills = 0
    try:
        player_toxicologist_wins_solo = data["player"]["stats"]["HungerGames"]["wins_toxicologist"]
    except KeyError:
        player_toxicologist_wins_solo = 0
    try:
        player_toxicologist_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_toxicologist"]
    except KeyError:
        player_toxicologist_wins_teams = 0
    player_toxicologist_wins = int(player_toxicologist_wins_solo) + int(player_toxicologist_wins_teams)
    try:
        player_toxicologist_games = data["player"]["stats"]["HungerGames"]["games_played_toxicologist"]
    except KeyError:
        player_toxicologist_games = 0

    try:
        player_troll_kills = data["player"]["stats"]["HungerGames"]["kills_troll"]
    except KeyError:
        player_troll_kills = 0
    try:
        player_troll_wins_solo = data["player"]["stats"]["HungerGames"]["wins_troll"]
    except KeyError:
        player_troll_wins_solo = 0
    try:
        player_troll_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_troll"]
    except KeyError:
        player_troll_wins_teams = 0
    player_troll_wins = int(player_troll_wins_solo) + int(player_troll_wins_teams)
    try:
        player_troll_games = data["player"]["stats"]["HungerGames"]["games_played_troll"]
    except KeyError:
        player_troll_games = 0

    try:
        player_viking_kills = data["player"]["stats"]["HungerGames"]["kills_viking"]
    except KeyError:
        player_viking_kills = 0
    try:
        player_viking_wins_solo = data["player"]["stats"]["HungerGames"]["wins_viking"]
    except KeyError:
        player_viking_wins_solo = 0
    try:
        player_viking_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_viking"]
    except KeyError:
        player_viking_wins_teams = 0
    player_viking_wins = int(player_viking_wins_solo) + int(player_viking_wins_teams)
    try:
        player_viking_games = data["player"]["stats"]["HungerGames"]["games_played_viking"]
    except KeyError:
        player_viking_games = 0
    
    try:
        player_warlock_kills = data["player"]["stats"]["HungerGames"]["kills_warlock"]
    except KeyError:
        player_warlock_kills = 0
    try:
        player_warlock_wins_solo = data["player"]["stats"]["HungerGames"]["wins_warlock"]
    except KeyError:
        player_warlock_wins_solo = 0
    try:
        player_warlock_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_warlock"]
    except KeyError:
        player_warlock_wins_teams = 0
    player_warlock_wins = int(player_warlock_wins_solo) + int(player_warlock_wins_teams)
    try:
        player_warlock_games = data["player"]["stats"]["HungerGames"]["games_played_warlock"]
    except KeyError:
        player_warlock_games = 0
    
    try:
        player_warrior_kills = data["player"]["stats"]["HungerGames"]["kills_warrior"]
    except KeyError:
        player_warrior_kills = 0
    try:
        player_warrior_wins_solo = data["player"]["stats"]["HungerGames"]["wins_warrior"]
    except KeyError:
        player_warrior_wins_solo = 0
    try:
        player_warrior_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_warrior"]
    except KeyError:
        player_warrior_wins_teams = 0
    player_warrior_wins = int(player_warrior_wins_solo) + int(player_warrior_wins_teams)
    try:
        player_warrior_games = data["player"]["stats"]["HungerGames"]["games_played_warrior"]
    except KeyError:
        player_warrior_games = 0
    
    try:
        player_wolftamer_kills = data["player"]["stats"]["HungerGames"]["kills_wolftamer"]
    except KeyError:
        player_wolftamer_kills = 0
    try:
        player_wolftamer_wins_solo = data["player"]["stats"]["HungerGames"]["wins_wolftamer"]
    except KeyError:
        player_wolftamer_wins_solo = 0
    try:
        player_wolftamer_wins_teams = data["player"]["stats"]["HungerGames"]["wins_teams_wolftamer"]
    except KeyError:
        player_wolftamer_wins_teams = 0
    player_wolftamer_wins = int(player_wolftamer_wins_solo) + int(player_wolftamer_wins_teams)
    try:
        player_wolftamer_games = data["player"]["stats"]["HungerGames"]["games_played_wolftamer"]
    except KeyError:
        player_wolftamer_games = 0
    
    
    return [
            player_arachnologist_kills, player_arach_wins, player_arach_games,
            player_archer_kills, player_archer_wins, player_archer_games,
            player_armorer_kills, player_armorer_wins, player_armorer_games,
            player_astro_kills, player_astro_wins, player_astro_games,
            player_baker_kills, player_baker_wins, player_baker_games,
            player_blaze_kills, player_blaze_wins, player_blaze_games,
            player_creepertamer_kills, player_creepertamer_wins, player_creepertamer_games,
            player_diver_kills, player_diver_wins, player_diver_games,
            player_donkey_kills, player_donkey_wins, player_donkey_games,
            player_farmer_kills, player_farmer_wins, player_farmer_games,
            player_fish_kills,player_fish_wins, player_fish_games,
            player_florist_kills,player_florist_wins, player_florist_games,
            player_golem_kills, player_golem_wins, player_golem_games,
            player_guardian_kills, player_guardian_wins, player_guardian_games,
            player_horse_kills, player_horse_wins, player_horse_games,
            player_hunter_kills, player_hunter_wins, player_hunter_games,
            player_hype_kills, player_hype_wins, player_hype_games,
            player_jockey_kills, player_jockey_wins, player_jockey_games,
            player_knight_kills, player_knight_wins, player_knight_games,
            player_meat_kills, player_meat_wins, player_meat_games,
            player_necromancer_kills, player_necromancer_wins, player_necromancer_games,
            player_paladin_kills, player_paladin_wins, player_paladin_games,
            player_phoenix_kills, player_phoenix_wins, player_phoenix_games,
            player_pigman_kills, player_pigman_wins, player_pigman_games,
            player_ranger_kills, player_ranger_wins, player_ranger_games,
            player_reaper_kills, player_reaper_wins, player_reaper_games,
            player_reddragon_kills, player_reddragon_wins, player_reddragon_games,
            player_rogue_kills, player_rogue_wins, player_rogue_games,
            player_scout_kills, player_scout_wins, player_scout_games,
            player_sk_kills, player_sk_wins, player_sk_games,
            player_slime_kills, player_slime_wins, player_slime_games,
            player_snowman_kills, player_snowman_wins, player_snowman_games,
            player_speleologist_kills, player_speleologist_wins, player_speleologist_games,
            player_tim_kills, player_tim_wins, player_tim_games,
            player_toxicologist_kills, player_toxicologist_wins, player_toxicologist_games,
            player_troll_kills, player_troll_wins, player_troll_games,
            player_viking_kills, player_viking_wins, player_viking_games,
            player_warlock_kills, player_warlock_wins, player_warlock_games,
            player_warrior_kills, player_warrior_wins, player_warrior_games,
            player_wolftamer_kills, player_wolftamer_wins, player_wolftamer_games,
            ]



def main():
    file = open("/Users/henrywright/Desktop/8k_bsg_uuids.txt", "r", encoding='utf-8-sig')
    
        

    ##
    

    #data = requests.get(
    #    url = "https://api.hypixel.net/leaderboards",
    #    params = {
    #      "key": "1cf1453f-fa64-4700-8ee8-25645431eec3", #24118s API key UUID: 6edc2962-6755-4f93-8945-9af0e8010b99
    #    }
    #).json()

    #top100 = data["leaderboards"]["SURVIVAL_GAMES"][0]["leaders"]
    

    arach_kills = 0
    arach_wins = 0
    arach_games = 0
    
    archer_kills = 0
    archer_wins = 0
    archer_games = 0

    armorer_kills = 0
    armorer_wins = 0
    armorer_games = 0

    astro_kills = 0
    astro_wins = 0
    astro_games = 0

    baker_kills = 0
    baker_wins = 0
    baker_games = 0
    
    blaze_kills = 0
    blaze_wins = 0
    blaze_games = 0

    creep_kills = 0
    creep_wins = 0
    creep_games = 0

    diver_kills = 0
    diver_wins = 0
    diver_games = 0

    donkey_kills = 0
    donkey_wins = 0
    donkey_games = 0
    
    farmer_kills = 0
    farmer_wins = 0
    farmer_games = 0

    fish_kills = 0
    fish_wins = 0
    fish_games = 0
    
    florist_kills = 0
    florist_wins = 0
    florist_games = 0

    golem_kills = 0
    golem_wins = 0
    golem_games = 0
    
    guardian_kills = 0
    guardian_wins = 0
    guardian_games = 0

    horse_kills = 0
    horse_wins = 0
    horse_games = 0

    hunter_kills = 0
    hunter_wins = 0
    hunter_games = 0

    hype_kills = 0
    hype_wins = 0
    hype_games = 0

    jockey_kills = 0
    jockey_wins = 0
    jockey_games = 0

    knight_kills = 0
    knight_wins = 0
    knight_games = 0

    meat_kills = 0
    meat_wins = 0
    meat_games = 0
    
    necro_kills = 0
    necro_wins = 0
    necro_games = 0

    pal_kills = 0
    pal_wins = 0
    pal_games = 0

    phoenix_kills = 0
    phoenix_wins = 0
    phoenix_games = 0

    pigman_kills = 0
    pigman_wins = 0
    pigman_games = 0
    
    ranger_kills = 0
    ranger_wins = 0
    ranger_games = 0

    reaper_kills = 0
    reaper_wins = 0
    reaper_games = 0

    red_kills = 0
    red_wins = 0
    red_games = 0

    rogue_kills = 0
    rogue_wins = 0
    rogue_games = 0

    scout_kills = 0
    scout_wins = 0
    scout_games = 0

    sk_kills = 0
    sk_wins = 0
    sk_games = 0

    slime_kills = 0
    slime_wins = 0
    slime_games = 0

    snow_kills = 0
    snow_wins = 0
    snow_games = 0

    spel_kills = 0
    spel_wins = 0
    spel_games = 0
    
    tim_kills = 0
    tim_wins = 0
    tim_games = 0

    tox_kills = 0
    tox_wins = 0
    tox_games = 0

    troll_kills = 0
    troll_wins = 0
    troll_games = 0

    viking_kills = 0
    viking_wins = 0
    viking_games = 0

    warlock_kills = 0
    warlock_wins = 0
    warlock_games = 0

    warrior_kills = 0
    warrior_wins = 0
    warrior_games = 0

    wolf_kills = 0
    wolf_wins = 0
    wolf_games = 0

    #for i in range(100):
        #list = getData("useless", top100[i])
        
   
    for line in file:
        
        #fname = line.rstrip().split(',')
        list = getData("useless", line.rstrip())
        
        arach_kills += list[0]
        arach_wins += list[1]
        arach_games += list[2]

        archer_kills += list[3]
        archer_wins += list[4]
        archer_games += list[5]

        armorer_kills += list[6]
        armorer_wins += list[7]
        armorer_games += list[8]

        astro_kills += list[9]
        astro_wins += list[10]
        astro_games += list[11]

        baker_kills += list[12]
        baker_wins += list[13]
        baker_games += list[14]
    
        blaze_kills += list[15]
        blaze_wins += list[16]
        blaze_games += list[17]

        creep_kills += list[18]
        creep_wins += list[19]
        creep_games += list[20]

        diver_kills += list[21]
        diver_wins += list[22]
        diver_games += list[23]

        donkey_kills += list[24]
        donkey_wins += list[25]
        donkey_games += list[26]
    
        farmer_kills += list[27]
        farmer_wins += list[28]
        farmer_games += list[29]

        fish_kills += list[30]
        fish_wins += list[31]
        fish_games += list[32]
    
        florist_kills += list[33]
        florist_wins += list[34]
        florist_games += list[35]

        golem_kills += list[36]
        golem_wins += list[37]
        golem_games += list[38]
    
        guardian_kills += list[39]
        guardian_wins += list[40]
        guardian_games += list[41]

        horse_kills += list[42]
        horse_wins += list[43]
        horse_games += list[44]

        hunter_kills += list[45]
        hunter_wins += list[46]
        hunter_games += list[47]

        hype_kills += list[48]
        hype_wins += list[49]
        hype_games += list[50]

        jockey_kills += list[51]
        jockey_wins += list[52]
        jockey_games += list[53]
    
        knight_kills += list[54]
        knight_wins += list[55]
        knight_games += list[56]

        meat_kills += list[57]
        meat_wins += list[58]
        meat_games += list[59]
    
        necro_kills += list[60]
        necro_wins += list[61]
        necro_games += list[62]

        pal_kills += list[63]
        pal_wins += list[64]
        pal_games += list[65]
    
        phoenix_kills += list[66]
        phoenix_wins += list[67]
        phoenix_games += list[68]

        pigman_kills += list[69]
        pigman_wins += list[70]
        pigman_games += list[71]
        
        ranger_kills += list[72]
        ranger_wins += list[73]
        ranger_games += list[74]

        reaper_kills += list[75]
        reaper_wins += list[76]
        reaper_games += list[77]
    
        red_kills += list[78]
        red_wins += list[79]
        red_games += list[80]

        rogue_kills += list[81]
        rogue_wins += list[82]
        rogue_games += list[83]
    
        scout_kills += list[84]
        scout_wins += list[85]
        scout_games += list[86]

        sk_kills += list[87]
        sk_wins += list[88]
        sk_games += list[89]
    
        slime_kills += list[90]
        slime_wins += list[91]
        slime_games += list[92]

        snow_kills += list[93]
        snow_wins += list[94]
        snow_games += list[95]

        spel_kills += list[96]
        spel_wins += list[97]
        spel_games += list[98]

        tim_kills += list[99]
        tim_wins += list[100]
        tim_games += list[101]
    
        tox_kills += list[102]
        tox_wins += list[103]
        tox_games += list[104]

        troll_kills += list[105]
        troll_wins += list[106]
        troll_games += list[107]
    
        viking_kills += list[108]
        viking_wins += list[109]
        viking_games += list[110]

        warlock_kills += list[111]
        warlock_wins += list[112]
        warlock_games += list[113]
    
        warrior_kills += list[114]
        warrior_wins += list[115]
        warrior_games += list[116]

        wolf_kills += list[117]
        wolf_wins += list[118]
        wolf_games += list[119]

    wb = Workbook()

    sheet1 = wb.add_sheet('Sheet 1')
    style0 = xlwt.easyxf('font: bold on')

    sheet1.write(0, 0, "Kit Name", style0)
    sheet1.write(0, 1, "Total Games Played", style0)
    sheet1.write(0, 2, "Total Kills", style0)
    sheet1.write(0, 3, "Total Wins", style0)
    sheet1.write(0, 4, "Total Wins/Total Losses", style0)
    
    i = 1
    

    arach_WL = float(arach_wins/(arach_games - arach_wins))

    sheet1.write(i, 0, "Arachnologist")
    sheet1.write(i, 1, arach_games)
    sheet1.write(i, 2, arach_kills)
    sheet1.write(i, 3, arach_wins)
    sheet1.write(i, 4, arach_WL)

    i += 1

    archer_WL = float(archer_wins/(archer_games - archer_wins))

    sheet1.write(i, 0, "Archer")
    sheet1.write(i, 1, archer_games)
    sheet1.write(i, 2, archer_kills)
    sheet1.write(i, 3, archer_wins)
    sheet1.write(i, 4, archer_WL)

    i += 1

    armorer_WL = float(armorer_wins/(armorer_games - armorer_wins))

    sheet1.write(i, 0, "Armorer")
    sheet1.write(i, 1, armorer_games)
    sheet1.write(i, 2, armorer_kills)
    sheet1.write(i, 3, armorer_wins)
    sheet1.write(i, 4, armorer_WL)

    i += 1

    astro_WL = float(astro_wins/(astro_games - astro_wins))

    sheet1.write(i, 0, "Astronaut")
    sheet1.write(i, 1, astro_games)
    sheet1.write(i, 2, astro_kills)
    sheet1.write(i, 3, astro_wins)
    sheet1.write(i, 4, astro_WL)

    i += 1

    baker_WL = float(baker_wins/(baker_games - baker_wins))

    sheet1.write(i, 0, "Baker")
    sheet1.write(i, 1, baker_games)
    sheet1.write(i, 2, baker_kills)
    sheet1.write(i, 3, baker_wins)
    sheet1.write(i, 4, baker_WL)

    i += 1

    blaze_WL = float(blaze_wins/(blaze_games - blaze_wins))

    sheet1.write(i, 0, "Blaze")
    sheet1.write(i, 1, blaze_games)
    sheet1.write(i, 2, blaze_kills)
    sheet1.write(i, 3, blaze_wins)
    sheet1.write(i, 4, blaze_WL)

    i += 1

    creep_WL = float(creep_wins/(creep_games - creep_wins))

    sheet1.write(i, 0, "Creepertamer")
    sheet1.write(i, 1, creep_games)
    sheet1.write(i, 2, creep_kills)
    sheet1.write(i, 3, creep_wins)
    sheet1.write(i, 4, creep_WL)

    i += 1

    diver_WL = float(diver_wins/(diver_games - diver_wins))

    sheet1.write(i, 0, "Diver")
    sheet1.write(i, 1, diver_games)
    sheet1.write(i, 2, diver_kills)
    sheet1.write(i, 3, diver_wins)
    sheet1.write(i, 4, diver_WL)

    i += 1

    donkey_WL = float(donkey_wins/(donkey_games - donkey_wins))

    sheet1.write(i, 0, "Donkeytamer")
    sheet1.write(i, 1, donkey_games)
    sheet1.write(i, 2, donkey_kills)
    sheet1.write(i, 3, donkey_wins)
    sheet1.write(i, 4, donkey_WL)

    i += 1

    farmer_WL = float(farmer_wins/(farmer_games - farmer_wins))

    sheet1.write(i, 0, "Farmer")
    sheet1.write(i, 1, farmer_games)
    sheet1.write(i, 2, farmer_kills)
    sheet1.write(i, 3, farmer_wins)
    sheet1.write(i, 4, farmer_WL)

    i += 1

    fish_WL = float(fish_wins/(fish_games - fish_wins))

    sheet1.write(i, 0, "Fishtamer")
    sheet1.write(i, 1, fish_games)
    sheet1.write(i, 2, fish_kills)
    sheet1.write(i, 3, fish_wins)
    sheet1.write(i, 4, fish_WL)

    i += 1

    florist_WL = float(florist_wins/(florist_games - florist_wins))

    sheet1.write(i, 0, "Florist")
    sheet1.write(i, 1, florist_games)
    sheet1.write(i, 2, florist_kills)
    sheet1.write(i, 3, florist_wins)
    sheet1.write(i, 4, florist_WL)

    i += 1

    golem_WL = float(golem_wins/(golem_games - golem_wins))

    sheet1.write(i, 0, "Golem")
    sheet1.write(i, 1, golem_games)
    sheet1.write(i, 2, golem_kills)
    sheet1.write(i, 3, golem_wins)
    sheet1.write(i, 4, golem_WL)

    i += 1

    guardian_WL = float(guardian_wins/(guardian_games - guardian_wins))

    sheet1.write(i, 0, "Guardian")
    sheet1.write(i, 1, guardian_games)
    sheet1.write(i, 2, guardian_kills)
    sheet1.write(i, 3, guardian_wins)
    sheet1.write(i, 4, guardian_WL)

    i += 1
    
    horse_WL = float(horse_wins/(horse_games - horse_wins))

    sheet1.write(i, 0, "Horse")
    sheet1.write(i, 1, horse_games)
    sheet1.write(i, 2, horse_kills)
    sheet1.write(i, 3, horse_wins)
    sheet1.write(i, 4, horse_WL)

    i += 1

    hunter_WL = float(hunter_wins/(hunter_games - hunter_wins))

    sheet1.write(i, 0, "Hunter")
    sheet1.write(i, 1, hunter_games)
    sheet1.write(i, 2, hunter_kills)
    sheet1.write(i, 3, hunter_wins)
    sheet1.write(i, 4, hunter_WL)

    i += 1

    hype_WL = float(hype_wins/(hype_games - hype_wins))

    sheet1.write(i, 0, "Hype")
    sheet1.write(i, 1, hype_games)
    sheet1.write(i, 2, hype_kills)
    sheet1.write(i, 3, hype_wins)
    sheet1.write(i, 4, hype_WL)

    i += 1

    jockey_WL = float(jockey_wins/(jockey_games - jockey_wins))

    sheet1.write(i, 0, "Jockey")
    sheet1.write(i, 1, jockey_games)
    sheet1.write(i, 2, jockey_kills)
    sheet1.write(i, 3, jockey_wins)
    sheet1.write(i, 4, jockey_WL)

    i += 1

    knight_WL = float(knight_wins/(knight_games - knight_wins))

    sheet1.write(i, 0, "Knight")
    sheet1.write(i, 1, knight_games)
    sheet1.write(i, 2, knight_kills)
    sheet1.write(i, 3, knight_wins)
    sheet1.write(i, 4, knight_WL)

    i += 1

    meat_WL = float(meat_wins/(meat_games - meat_wins))

    sheet1.write(i, 0, "Meatmaster")
    sheet1.write(i, 1, meat_games)
    sheet1.write(i, 2, meat_kills)
    sheet1.write(i, 3, meat_wins)
    sheet1.write(i, 4, meat_WL)

    i += 1

    necro_WL = float(necro_wins/(necro_games - necro_wins))

    sheet1.write(i, 0, "Necromancer")
    sheet1.write(i, 1, necro_games)
    sheet1.write(i, 2, necro_kills)
    sheet1.write(i, 3, necro_wins)
    sheet1.write(i, 4, necro_WL)

    i += 1

    pal_WL = float(pal_wins/(pal_games - pal_wins))

    sheet1.write(i, 0, "Paladin")
    sheet1.write(i, 1, pal_games)
    sheet1.write(i, 2, pal_kills)
    sheet1.write(i, 3, pal_wins)
    sheet1.write(i, 4, pal_WL)

    i += 1

    phoenix_WL = float(phoenix_wins/(phoenix_games - phoenix_wins))

    sheet1.write(i, 0, "Phoenix")
    sheet1.write(i, 1, phoenix_games)
    sheet1.write(i, 2, phoenix_kills)
    sheet1.write(i, 3, phoenix_wins)
    sheet1.write(i, 4, phoenix_WL)

    i += 1

    pigman_WL = float(pigman_wins/(pigman_games - pigman_wins))

    sheet1.write(i, 0, "Pigman")
    sheet1.write(i, 1, pigman_games)
    sheet1.write(i, 2, pigman_kills)
    sheet1.write(i, 3, pigman_wins)
    sheet1.write(i, 4, pigman_WL)

    i += 1

    ranger_WL = float(ranger_wins/(ranger_games - ranger_wins))

    sheet1.write(i, 0, "Ranger")
    sheet1.write(i, 1, ranger_games)
    sheet1.write(i, 2, ranger_kills)
    sheet1.write(i, 3, ranger_wins)
    sheet1.write(i, 4, ranger_WL)

    i += 1

    reaper_WL = float(reaper_wins/(reaper_games - reaper_wins))

    sheet1.write(i, 0, "Reaper")
    sheet1.write(i, 1, reaper_games)
    sheet1.write(i, 2, reaper_kills)
    sheet1.write(i, 3, reaper_wins)
    sheet1.write(i, 4, reaper_WL)

    i += 1

    red_WL = float(red_wins/(red_games - red_wins))

    sheet1.write(i, 0, "Red Dragon")
    sheet1.write(i, 1, red_games)
    sheet1.write(i, 2, red_kills)
    sheet1.write(i, 3, red_wins)
    sheet1.write(i, 4, red_WL)

    i += 1

    rogue_WL = float(rogue_wins/(rogue_games - rogue_wins))

    sheet1.write(i, 0, "Rogue")
    sheet1.write(i, 1, rogue_games)
    sheet1.write(i, 2, rogue_kills)
    sheet1.write(i, 3, rogue_wins)
    sheet1.write(i, 4, rogue_WL)

    i += 1

    scout_WL = float(scout_wins/(scout_games - scout_wins))

    sheet1.write(i, 0, "Scout")
    sheet1.write(i, 1, scout_games)
    sheet1.write(i, 2, scout_kills)
    sheet1.write(i, 3, scout_wins)
    sheet1.write(i, 4, scout_WL)

    i += 1

    slime_WL = float(slime_wins/(slime_games - slime_wins))

    sheet1.write(i, 0, "Slimey Slime")
    sheet1.write(i, 1, slime_games)
    sheet1.write(i, 2, slime_kills)
    sheet1.write(i, 3, slime_wins)
    sheet1.write(i, 4, slime_WL)

    i += 1

    sk_WL = float(sk_wins/(sk_games - sk_wins))

    sheet1.write(i, 0, "Shadow Knight")
    sheet1.write(i, 1, sk_games)
    sheet1.write(i, 2, sk_kills)
    sheet1.write(i, 3, sk_wins)
    sheet1.write(i, 4, sk_WL)

    i += 1

    snow_WL = float(snow_wins/(snow_games - snow_wins))

    sheet1.write(i, 0, "Snowman")
    sheet1.write(i, 1, snow_games)
    sheet1.write(i, 2, snow_kills)
    sheet1.write(i, 3, snow_wins)
    sheet1.write(i, 4, snow_WL)

    i += 1

    spel_WL = float(spel_wins/(spel_games - spel_wins))

    sheet1.write(i, 0, "Speleologist")
    sheet1.write(i, 1, spel_games)
    sheet1.write(i, 2, spel_kills)
    sheet1.write(i, 3, spel_wins)
    sheet1.write(i, 4, spel_WL)

    i += 1

    tim_WL = float(tim_wins/(tim_games - tim_wins))

    sheet1.write(i, 0, "Tim")
    sheet1.write(i, 1, tim_games)
    sheet1.write(i, 2, tim_kills)
    sheet1.write(i, 3, tim_wins)
    sheet1.write(i, 4, tim_WL)

    i += 1

    tox_WL = float(tox_wins/(tox_games - tox_wins))

    sheet1.write(i, 0, "Toxicologist")
    sheet1.write(i, 1, tox_games)
    sheet1.write(i, 2, tox_kills)
    sheet1.write(i, 3, tox_wins)
    sheet1.write(i, 4, tox_WL)

    i += 1

    troll_WL = float(troll_wins/(troll_games - troll_wins))

    sheet1.write(i, 0, "Troll")
    sheet1.write(i, 1, troll_games)
    sheet1.write(i, 2, troll_kills)
    sheet1.write(i, 3, troll_wins)
    sheet1.write(i, 4, troll_WL)

    i += 1
    
    viking_WL = float(viking_wins/(viking_games - viking_wins))

    sheet1.write(i, 0, "Viking")
    sheet1.write(i, 1, viking_games)
    sheet1.write(i, 2, viking_kills)
    sheet1.write(i, 3, viking_wins)
    sheet1.write(i, 4, viking_WL)

    i += 1

    warlock_WL = float(warlock_wins/(warlock_games - warlock_wins))

    sheet1.write(i, 0, "Warlock")
    sheet1.write(i, 1, warlock_games)
    sheet1.write(i, 2, warlock_kills)
    sheet1.write(i, 3, warlock_wins)
    sheet1.write(i, 4, warlock_WL)

    i += 1

    warrior_WL = float(warrior_wins/(warrior_games - warrior_wins))

    sheet1.write(i, 0, "Warrior")
    sheet1.write(i, 1, warrior_games)
    sheet1.write(i, 2, warrior_kills)
    sheet1.write(i, 3, warrior_wins)
    sheet1.write(i, 4, warrior_WL)

    i += 1

    wolf_WL = float(warlock_wins/(warlock_games - warlock_wins))

    sheet1.write(i, 0, "Wolf")
    sheet1.write(i, 1, wolf_games)
    sheet1.write(i, 2, wolf_kills)
    sheet1.write(i, 3, wolf_wins)
    sheet1.write(i, 4, wolf_WL)

    wb.save('bestkittest1.xls')

    #print("Total arach kills: " + str(arach_kills))
    #print("Total arach wins: " + str(arach_wins))
    #arach_WL = float(arach_wins/(arach_games - arach_wins))
    #print("Overall W/L: " + str(arach_WL))
    #print("--------------------")
    
    #print("Total archer kills: " + str(archer_kills))
    #print("Total archer wins: " + str(archer_wins))
    #archer_WL = float(archer_wins/(archer_games - archer_wins))
    #print("Overall W/L: " + str(archer_WL))
    #print("--------------------")

    #print("Total armorer kills: " + str(armorer_kills))
    #print("Total armorer wins: " + str(armorer_wins))
    #armorer_WL = float(armorer_wins/(armorer_games - armorer_wins))
    #print("Overall W/L: " + str(armorer_WL))
    #print("--------------------")
    
    #print("Total astro kills: " + str(astro_kills))
    #print("Total astro wins: " + str(astro_wins))
    #astro_WL = float(astro_wins/(astro_games - astro_wins))
    #print("Overall W/L: " + str(astro_WL))
    #print("--------------------")

    #print("Total baker kills: " + str(baker_kills))
    #print("Total baker wins: " + str(baker_wins))
    #baker_WL = float(baker_wins/(baker_games - baker_wins))
    #print("Overall W/L: " + str(baker_WL))
    #print("--------------------")

    #print("Total blaze kills: " + str(blaze_kills))
    #print("Total blaze wins: " + str(blaze_wins))
    #blaze_WL = float(blaze_wins/(blaze_games - blaze_wins))
    #print("Overall W/L: " + str(blaze_WL))
    #print("--------------------")
    
    #print("Total creep kills: " + str(creep_kills))
    #print("Total creep wins: " + str(creep_wins))
    #creep_WL = float(creep_wins/(creep_games - creep_wins))
    #print("Overall W/L: " + str(creep_WL))
    #print("--------------------")

    #print("Total diver kills: " + str(diver_kills))
    #print("Total diver wins: " + str(diver_wins))
    #diver_WL = float(diver_wins/(diver_games - diver_wins))
    #print("Overall W/L: " + str(diver_WL))
    #print("--------------------")
    
    #print("Total donkey kills: " + str(donkey_kills))
    #print("Total donkey wins: " + str(donkey_wins))
    #donkey_WL = float(donkey_wins/(donkey_games - donkey_wins))
    #print("Overall W/L: " + str(donkey_WL))
    #print("--------------------")

    #print("Total farmer kills: " + str(farmer_kills))
    #print("Total farmer wins: " + str(farmer_wins))
    #farmer_WL = float(farmer_wins/(farmer_games - farmer_wins))
    #print("Overall W/L: " + str(farmer_WL))
    #print("--------------------")
    
    #print("Total fish kills: " + str(fish_kills))
    #print("Total fish wins: " + str(fish_wins))
    #fish_WL = float(fish_wins/(fish_games - fish_wins))
    #print("Overall W/L: " + str(fish_WL))
    #print("--------------------")

    #print("Total florist kills: " + str(florist_kills))
    #print("Total florist wins: " + str(florist_wins))
    #florist_WL = float(florist_wins/(florist_games - florist_wins))
    #print("Overall W/L: " + str(florist_WL))
    #print("--------------------")

    #print("Total golem kills: " + str(golem_kills))
    #print("Total golem wins: " + str(golem_wins))
    #golem_WL = float(golem_wins/(golem_games - golem_wins))
    #print("Overall W/L: " + str(golem_WL))
    #print("--------------------")
    
    #print("Total guardian kills: " + str(guardian_kills))
    #print("Total guardian wins: " + str(guardian_wins))
    #guardian_WL = float(guardian_wins/(guardian_games - guardian_wins))
    #print("Overall W/L: " + str(guardian_WL))
    #print("--------------------")

    #print("Total horse kills: " + str(horse_kills))
    #print("Total horse wins: " + str(horse_wins))
    #horse_WL = float(horse_wins/(horse_games - horse_wins))
    #print("Overall W/L: " + str(horse_WL))
    #print("--------------------")

    #print("Total hunter kills: " + str(hunter_kills))
    #print("Total hype wins: " + str(hunter_wins))
    #hunter_WL = float(hunter_wins/(hunter_games - hunter_wins))
    #print("Overall W/L: " + str(hunter_WL))
    #print("--------------------")

    #print("Total hype kills: " + str(hype_kills))
    #print("Total hype wins: " + str(hype_wins))
    #hype_WL = float(hype_wins/(hype_games - hype_wins))
    #print("Overall W/L: " + str(hype_WL))
    #print("--------------------")
    
    #print("Total jockey kills: " + str(jockey_kills))
    #print("Total jockey wins: " + str(jockey_wins))
    #jockey_WL = float(jockey_wins/(jockey_games - jockey_wins))
    #print("Overall W/L: " + str(jockey_WL))
    #print("--------------------")
    
    #print("Total knight kills: " + str(knight_kills))
    #print("Total knight wins: " + str(knight_wins))
    #knight_WL = float(knight_wins/(knight_games - knight_wins))
    #print("Overall W/L: " + str(knight_WL))
    #print("--------------------")
    
    #print("Total meat kills: " + str(meat_kills))
    #print("Total meat wins: " + str(meat_wins))
    #meat_WL = float(meat_wins/(meat_games - meat_wins))
    #print("Overall W/L: " + str(meat_WL))
    #print("--------------------")
    
    #print("Total necromancer kills: " + str(necro_kills))
    #print("Total necromancer wins: " + str(necro_wins))
    #necro_WL = float(necro_wins/(necro_games - necro_wins))
    #print("Overall W/L: " + str(necro_WL))
    #print("--------------------")

    #print("Total paladin kills: " + str(pal_kills))
    #print("Total paladin wins: " + str(pal_wins))
    #pal_WL = float(pal_wins/(pal_games - pal_wins))
    #print("Overall W/L: " + str(pal_WL))
    #print("--------------------")
    
    #print("Total phoenix kills: " + str(phoenix_kills))
    #print("Total phoenix wins: " + str(phoenix_wins))
    #phoenix_WL = float(phoenix_wins/(phoenix_games - phoenix_wins))
    #print("Overall W/L: " + str(phoenix_WL))
    #print("--------------------")
    
    #print("Total pigman kills: " + str(pigman_kills))
    #print("Total pigman wins: " + str(pigman_wins))
    #pigman_WL = float(pigman_wins/(pigman_games - pigman_wins))
    #print("Overall W/L: " + str(pigman_WL))
    #print("--------------------")
    
    #print("Total ranger kills: " + str(ranger_kills))
    #print("Total ranger wins: " + str(ranger_wins))
    #ranger_WL = float(ranger_wins/(ranger_games - ranger_wins))
    #print("Overall W/L: " + str(ranger_WL))
    #print("--------------------")
    
    #print("Total reaper kills: " + str(reaper_kills))
    #print("Total reaper wins: " + str(reaper_wins))
    #reaper_WL = float(reaper_wins/(reaper_games - reaper_wins))
    #print("Overall W/L: " + str(reaper_WL))
    #print("--------------------")
    
    #print("Total reddragon kills: " + str(red_kills))
    #print("Total reddragon wins: " + str(red_wins))
    #red_WL = float(red_wins/(red_games - red_wins))
    #print("Overall W/L: " + str(red_WL))
    #print("--------------------")
    
    #print("Total rogue kills: " + str(rogue_kills))
    #print("Total rogue wins: " + str(rogue_wins))
    #rogue_WL = float(rogue_wins/(rogue_games - rogue_wins))
    #print("Overall W/L: " + str(rogue_WL))
    #print("--------------------")
    
    #print("Total scout kills: " + str(scout_kills))
    #print("Total scout wins: " + str(scout_wins))
    #scout_WL = float(scout_wins/(scout_games - scout_wins))
    #print("Overall W/L: " + str(scout_WL))
    #print("--------------------")

    #print("Total slime kills: " + str(slime_kills))
    #print("Total slime wins: " + str(slime_wins))
    #slime_WL = float(slime_wins/(slime_games - slime_wins))
    #print("Overall W/L: " + str(slime_WL))
    #print("--------------------")
    
    #print("Total shadow knight kills: " + str(sk_kills))
    #print("Total shadow knight wins: " + str(sk_wins))
    #sk_WL = float(sk_wins/(sk_games - sk_wins))
    #print("Overall W/L: " + str(sk_WL))
    #print("--------------------")
    
    #print("Total snowman kills: " + str(snow_kills))
    #print("Total snowman wins: " + str(snow_wins))
    #snow_WL = float(snow_wins/(snow_games - snow_wins))
    #print("Overall W/L: " + str(snow_WL))
    #print("--------------------")

    #print("Total speleologist kills: " + str(spel_kills))
    #print("Total speleologist wins: " + str(spel_wins))
    #spel_WL = float(spel_wins/(spel_games - spel_wins))
    #print("Overall W/L: " + str(spel_WL))
    #print("--------------------")
    
    #print("Total tim kills: " + str(tim_kills))
    #print("Total tim wins: " + str(tim_wins))
    #tim_WL = float(tim_wins/(tim_games - tim_wins))
    #print("Overall W/L: " + str(tim_WL))
    #print("--------------------")
    
    #print("Total toxicologist kills: " + str(tox_kills))
    #print("Total toxicologist wins: " + str(tox_wins))
    #tox_WL = float(tox_wins/(tox_games - tox_wins))
    #print("Overall W/L: " + str(tox_WL))
    #print("--------------------")
    
    #print("Total troll kills: " + str(troll_kills))
    #print("Total troll wins: " + str(troll_wins))
    #troll_WL = float(troll_wins/(troll_games - troll_wins))
    #print("Overall W/L: " + str(troll_WL))
    #print("--------------------")
    
    #print("Total viking kills: " + str(viking_kills))
    #print("Total viking wins: " + str(viking_wins))
    #viking_WL = float(viking_wins/(viking_games - viking_wins))
    #print("Overall W/L: " + str(viking_WL))
    #print("--------------------")

    #print("Total warlock kills: " + str(warlock_kills))
    #print("Total warlock wins: " + str(warlock_wins))
    #warlock_WL = float(warlock_wins/(warlock_games - warlock_wins))
    #print("Overall W/L: " + str(warlock_WL))
    #print("--------------------")
    
    #print("Total warrior kills: " + str(warrior_kills))
    #print("Total warrior wins: " + str(warrior_wins))
    #warrior_WL = float(warrior_wins/(warrior_games - warrior_wins))
    #print("Overall W/L: " + str(warrior_WL))
    #print("--------------------")
    
    #print("Total wolftamer kills: " + str(wolf_kills))
    #print("Total wolftamer wins: " + str(wolf_wins))
    #wolf_WL = float(wolf_wins/(wolf_games - wolf_wins))
    #print("Overall W/L: " + str(wolf_WL))
    #print("--------------------")


main()    





 
