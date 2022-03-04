'''
Given is an array with team names that are competing. 
i represent mathch_i and i[0] team is home team. i[1] team is away team
Another array is given for winner of each match.

if winner[i] = 0, Away team is won.
if winner[i] = 1, Home team is won

'''

def tournamentWinner(competitions, results):
    teams = {key[0] : 0 for key in competitions}
    teams.update({key[1] : 0 for key in competitions})
    for i in range(len(results)) :
        res = results[i]
        comp = competitions[i]
        teams[comp[res ^ 1]] += 1
    maximum = 0
    res=''
    for k,v in teams.items():
        if v > maximum :
            maximum = v
            res = k
            
    return res