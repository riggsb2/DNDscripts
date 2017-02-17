# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:58:47 2017

@author: Riggs
"""

import numpy as np


roster = np.genfromtxt('Full Roster.csv',dtype = str, delimiter = ",")
army_stats = np.genfromtxt('Enemy unit stats.csv',dtype = str, delimiter = ",")

army_summary = np.array(['Number','Type','HP','AC','Hit B.', 'Dmg.B', 'Dmg.Rng.','Crit'])

summary ={}
unique, counts = np.unique(roster[1:,0], return_counts = True)
result = dict(zip(unique,counts))
summary = np.array([(key,val) for (key,val) in result.items()],dtype=str)

for i in range(1,len(army_stats)):
    for j in range(len(summary)):               
        if summary[j][0] == army_stats[i][0]:
            temp = [summary[j][1]]
            temp = np.hstack((temp,army_stats[i]))
            army_summary = np.vstack((army_summary,temp))

print(roster)
soldiers_killed = 5
for i in range(soldiers_killed):
    for j in range(1,len(roster)):
        if roster[j][0]=='Sold1':
            roster = np.delete(roster,j,axis = 0)
            break
deadlist = ['Sold1', 'Sold1', 'Sold1', 'Sold1', 'Sold1', 'Sold1', 'Sold1']
for i in range(len(deadlist)):
   for j in range(1,len(roster)):
       if deadlist[i]==roster[j][0]:
           roster = np.delete(roster,j,axis=0)  
           print(roster)
print(roster)