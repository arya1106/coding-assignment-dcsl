def getTeams(rankings):
    rankings.sort()
    teamCombinations = []
    i = 0
    while (i+3) <= len(rankings):
        teamCombinations.append(rankings[i:i+3])
        i+=1
    return teamCombinations

def calcHetero(teamCombinations):
    heterogeneityDict = {}
    for index, team in enumerate(teamCombinations):
        heterogeneity = max(team) - min(team)
        if heterogeneity in heterogeneityDict.keys():
            heterogeneityDict[heterogeneity].append(team)
        else:
            heterogeneityDict[heterogeneity] = [team]
    return heterogeneityDict

firstLine = input().split()
p = int(firstLine[0])
k = int(firstLine[1])
ranks = [int(i) for i in input().split()]

finalHeteros = []
for i in range(k):
    teamCombos = getTeams(ranks)
    heteroDict = calcHetero(teamCombos)
	# I know this is incorrect, but I was not able to find a solution with a reasonable time and space complexity for larger values of P that was always accurate
    team = heteroDict[min(heteroDict.keys())][0] # greedy heuristic
    finalHeteros.append(max(team) - min(team))
    for rank in team:
        ranks.remove(rank)
print(max(finalHeteros))
