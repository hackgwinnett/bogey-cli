import rank
import os

root = "database/"

'''
    container[0]: groups
    container[1]: members
    container[2]: scores
'''

def exportAll():

    creativityContainer = rank.getRank("creativity")
    complexityContainer = rank.getRank("complexity")
    efficiencyContainer = rank.getRank("efficiency")
    executionContainer = rank.getRank("execution")
    appearanceContainer = rank.getRank("appearance")
    compositeContainer = rank.getRank("composite")

    print("")
    print("creativity rankings:")
    display(creativityContainer)

    print("")
    print("complexity rankings:")
    display(complexityContainer)

    print("")
    print("efficiency rankings:")
    display(efficiencyContainer)

    print("")
    print("execution rankings:")
    display(executionContainer)

    print("")
    print("appearance rankings:")
    display(appearanceContainer)

    print("")
    print("composite rankings:")
    display(compositeContainer)

    f = open(root + "rankings.csv", "a")
    f.write("group,creativity,complexity,efficiency,execution,appearance,composite\n")
    groups = getGroups()
    for i in range(len(groups)):
        f.write(str(groups[i]) + ",")
        scoreContainer = []
        scoreContainer.append(rank.getScore(groups[i], "creativity"))
        scoreContainer.append(rank.getScore(groups[i], "complexity"))
        scoreContainer.append(rank.getScore(groups[i], "efficiency"))
        scoreContainer.append(rank.getScore(groups[i], "execution"))
        scoreContainer.append(rank.getScore(groups[i], "appearance"))
        scoreContainer.append(rank.getScore(groups[i], "composite"))
        for j in range(len(scoreContainer)):
            f.write(str(scoreContainer[j]))
            if j != len(scoreContainer) - 1:
                f.write(",")
        f.write("\n")

def display(container):

    groups = container[0]
    members = container[1]
    scores = container[2]

    i = 0
    while i < len(groups):
        print(str(groups[i]) + " " + str(members[i]) + " " + str(scores[i]))
        i+=1

def getGroups():

    files = os.listdir(root)
    groups = []

    i = 0
    while i < len(files):
        if ".txt" not in str(files[i]):
            files.pop(i)
        i+=1
    
    i = 0
    while i < len(files):
        name = str(files[i]).replace(".txt", "")
        groups.append(name)
        i+=1
    
    return groups