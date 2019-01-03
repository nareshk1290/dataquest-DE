################ I/O Bound Programs ################

## Mission 2

import cProfile
import sqlite3

query = "SELECT DISTINCT teamID from Teams inner join TeamsFranchises on Teams.franchID == TeamsFranchises.franchID where TeamsFranchises.active = 'Y';"
conn = sqlite3.connect("lahman2015.sqlite")

cur = conn.cursor()
teams = [row[0] for row in cur.execute(query).fetchall()]
query = "SELECT sum(HR) from Batting where teamId = ?"

def func_teams(teams):
    home_runs = []
    for team in teams:
        runs = cur.execute(query, [team]).fetchall()
        runs = runs[0][0]
        home_runs.append(runs)
    return home_runs

profile_string = "home_runs = func_teams(teams)"
cProfile.run(profile_string)

## Mission 3

import sqlite3

memory = sqlite3.connect(':memory:') # create a memory database
disk = sqlite3.connect('lahman2015.sqlite')

dump = "".join([line for line in disk.iterdump() if "Batting" in line])
memory.executescript(dump)

cur = memory.cursor()
query = "SELECT sum(HR) from Batting where teamId = ?"

def func_teams(teams):
    home_runs = []
    for team in teams:
        runs = cur.execute(query, [team]).fetchall()
        runs = runs[0][0]
        home_runs.append(runs)
    return home_runs

profile_string = "home_runs = func_teams(teams)"
cProfile.run(profile_string)

## Mission 4

import threading

def task(team):
    print(team)
    
for i, team in enumerate(teams):
    thread = threading.Thread(target = task, args=(team,))
    thread.start()
    print("Started task {}".format(i))
    
print(teams)

## Mission 5

import threading
import time

def task(team):
    time.sleep(3)
    print(team)
    
for i, team in enumerate(teams):
    thread = threading.Thread(target = task, args=(team,))
    thread.start()
    print("Started task {}".format(i))
	
## Mission 7

import threading
import time

def task(team):
    print(team)
    
for i in range(11):
    team_names = teams[i*5 : (i+1)*5]
    threads = []
    for team in team_names:
        thread = threading.Thread(target = task, args=(team,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print("Finished batch {}".format(i))
	
## Mission 9

import threading
import time
import sys

lock = threading.Lock()

def task(team):
    lock.acquire()
    print(team)
    sys.stdout.flush()
    lock.release()
    
for i in range(11):
    team_names = teams[i*5 : (i+1)*5]
    threads = []
    for team in team_names:
        thread = threading.Thread(target = task, args=(team,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print("Finished batch {}".format(i))

## Mission 10

import cProfile
import sqlite3
import threading
import sys

query = "SELECT DISTINCT teamID from Teams inner join TeamsFranchises on Teams.franchID == TeamsFranchises.franchID where TeamsFranchises.active = 'Y';"
conn = sqlite3.connect("lahman2015.sqlite", check_same_thread=False)
cur = conn.cursor()
teams = [row[0] for row in cur.execute(query).fetchall()]

query = "SELECT SUM(HR) FROM Batting WHERE teamId=?"
lock = threading.Lock()

def calculate_runs(team):
    cur = conn.cursor()
    runs = cur.execute(query, [team]).fetchall()
    runs = runs[0][0]
    lock.acquire()
    print(team)
    print(runs)
    sys.stdout.flush()
    lock.release()
    return runs

threads = []
for team in teams:
        thread = threading.Thread(target = calculate_runs, args=(team,))
        thread.start()
        threads.append(thread)
        
for thread in threads:
    thread.join()
	
## Mission 12

import threading

conn = sqlite3.connect("lahman2015.sqlite", check_same_thread=False)
best = {}
lock = threading.Lock()

def best_batter():
    cur = conn.cursor()
    query = """
    SELECT 
        ((CAST(H AS FLOAT) + BB + HBP) / (AB + BB + HBP + SF)) + ((H + "2B" + 2*"3B" + 3*HR) / AB) as OBP,  
        playerID
    FROM Batting
    GROUP BY Batting.playerID
    HAVING AB > 100
    ORDER BY OBP desc
    LIMIT 20;
    """
    players = cur.execute(query).fetchall()
    names = [p[1] for p in players]
    best["batter"] = names
    lock.acquire()
    print("Done finding best batters.")
    lock.release()
    
    
def best_pitcher():
    cur = conn.cursor()
    query = """
    SELECT 
        ((13*CAST(HR AS FLOAT) + 3*BB - 2*SO) / IPOuts) + 3.2 as FIP,  
        playerID
    FROM Pitching
    GROUP BY Pitching.playerID
    HAVING IPOuts > 100
    ORDER BY FIP asc
    LIMIT 20;
    """
    players = cur.execute(query).fetchall()
    names = [p[1] for p in players]
    best["pitcher"] = names
    lock.acquire()
    print("Done finding best pitchers.")
    lock.release()

def best_fielder():
    cur = conn.cursor()
    query = """
    SELECT 
        (CAST(A AS FLOAT) + PO) / G as RF,  
        playerID
    FROM Fielding
    GROUP BY Fielding.playerID
    HAVING G > 100
    ORDER BY RF desc
    LIMIT 20;
    """
    players = cur.execute(query).fetchall()
    names = [p[1] for p in players]
    best["fielder"] = names
    lock.acquire()
    print("Done finding best fielders.")
    lock.release()

threads = []
for func in [best_fielder, best_batter, best_pitcher]:
    thread = threading.Thread(target=func)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(best)