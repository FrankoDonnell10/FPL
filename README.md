# FPL
Fantasy Premier League public API to get team and league data.

fpl_h2h files target head to head league data and saves it to an Excel file.
The only thing that requires change is the league code in he URL's for the league you are targetting. 

fpl_h2h_league_stats returns results from each game week frommy uor head to head mini league. Substitue your head to head league code into the URL in line 8 to return data related to your won league. This can be found on Fanatsy Premier League website. when you open you head to head league, the code should be in the URL e.g https://fantasy.premierleague.com/leagues/556449/matches/h

fpl_h2h_fixtures does teh same as teh above bu the output inot excel has a different format.

F1 FPL assigns a formula 1 scoing system based on points scored per gameweek.
Credit: Guillaume Weingertner
towards data science article: https://towardsdatascience.com/fantasy-premier-league-an-alternative-points-system-with-python-b0773e2217ad

FPLStats file targets specific team statistics such as captain points, poins per position and rank evolution.
Credit: Guillaume Weingertner
towards data science article: https://towardsdatascience.com/an-analysis-of-your-fantasy-premier-league-team-with-python-de4acf77e444

