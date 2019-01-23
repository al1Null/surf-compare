# surf-compare
Compare csgo surf stats
Surf-Compare allows you to compare you csgo surf game stats against another players'

# How does it work?
## 1. Get the Data (Game stats)
You need to retive the game stats of the two players you want to compare.
You'll most likely want to compare your own with another player.
## 2. Enter your Data
Each file needs to be formatted accordingly:
  txt files of both users' data needs to be placed in the raw_data/ folder
where the name of the file is the name of player (and file type is a .txt)
## 3. Run the program
This can be run through the command line
cd into the programs base directory
Ensure that python 3 is installed, and PATH to it is enivronmental variables is there
  you can check this by typing ```python``` into the command line, the interpreture should then open,
  exit and verify the version of python is atleast 3 (preferablly python 3.6) check version by doing ```python --version```
  
to run simply do  ```python Compare.py player1 player2```
the two command line arguments are the names of players (seperated by a space),
these need to match the name of the files (don't include .txt when typing in the command line) 
## 4. Look at the output!


### Example of what the player.txt should look like:
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


# files
### Compare.py
Main file to be run
### Validator.py
Ensures that the data entered is valid
### Formatter.py
Formats the raw data to then be analized
### CompareMaps.py
Compares map stats
### CompareTimes.py
Compares time stats
### CompareRanks.py
Compares rank stats

### Dependancies
python3 (python3.5 or great preferabliy)
sys, os, json, argparse
