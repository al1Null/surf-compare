# surf-compare
csgo surf times compare b/w users


How does it work?
.txt files of both users' data needs to be placed in the raw_data/ folder
they need to be formatted accordingly:
  where the name of each file the the name of player followed by .txt
  
  ```
  surf_4head_csgo, Time: 01:07:13, Rank: 42/74
  surf_ace_fix, Time: 00:44:14, Rank: 39/3759
  surf_aether_csgo, Time: 00:50:49, Rank: 32/117
  ...
  ...
  ... 
  surf_water-run_banjo_skill, Time: 00:38:87, Rank: 76/7157
  surf_waterworks, Time: 01:21:52, Rank: 32/658
  surf_year3000, Time: 00:17:56, Rank: 35/1497
  ```
  
### folders ###
raw_data/
formatted_compares/


### files ####
# Compare.py
# Validator.py
# Formatter.py
# CompareMaps.py
# CompareTimes.py
# CompareRanks.py

### Dependancies ###
sys, os, json, argparse
