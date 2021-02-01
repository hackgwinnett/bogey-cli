import os

root = "database/"
memberIndex = 0
creativityIndex = 1
complexityIndex = 2
efficiencyIndex = 3
executionIndex = 4
appearanceIndex = 5
compositeIndex = 6

def rank(category):

    groups = []
    members = []
    scores = []
    files = os.listdir(root)

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
    
    i = 0
    while i < len(groups):
        members.append(getMembers(groups[i]))
        i+=1

    i = 0
    while i < len(groups):
        scores.append(getScore(groups[i], category))
        i += 1

    for i in range(len(scores)):
        for j in range(i + 1, len(scores)):
            if scores[i] > scores[j]:
                scores[i], scores[j] = scores[j], scores[i]
                groups[i], groups[j] = groups[j], groups[i]
                members[i], members[j] = members[j], members[i]
    
    reversedGroups = []
    reversedMembers = []
    reversedScores = []

    i = len(groups) - 1
    while i >= 0:
        reversedGroups.append(groups[i])
        reversedMembers.append(members[i])
        reversedScores.append(scores[i])
        i-=1

    print("")
    print(category + " rankings:")
    i = 0
    while i < len(reversedGroups):
        print(str(reversedGroups[i]) + " " + str(reversedMembers[i]) + " " + str(reversedScores[i]))
        i+=1

def getRank(category):

    groups = []
    members = []
    scores = []
    container = []
    files = os.listdir(root)

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
    
    i = 0
    while i < len(groups):
        members.append(getMembers(groups[i]))
        i+=1

    i = 0
    while i < len(groups):
        scores.append(getScore(groups[i], category))
        i += 1

    for i in range(len(scores)):
        for j in range(i + 1, len(scores)):
            if scores[i] > scores[j]:
                scores[i], scores[j] = scores[j], scores[i]
                groups[i], groups[j] = groups[j], groups[i]
                members[i], members[j] = members[j], members[i]
    
    reversedGroups = []
    reversedMembers = []
    reversedScores = []

    i = len(groups) - 1
    while i >= 0:
        reversedGroups.append(groups[i])
        reversedMembers.append(members[i])
        reversedScores.append(scores[i])
        i-=1
    
    container.append(reversedGroups)
    container.append(reversedMembers)
    container.append(reversedScores)

    return container

def read(name):
    filepath = root + name + ".txt"
    f = open(filepath, "r")
    lines = []
    for x in f:
        line = x.replace("\n", "")
        lines.append(line)
    return lines

def getMembers(name):
    lines = read(name)
    raw = lines[memberIndex].split(": ")
    members = raw[1].split(",")
    return members

def getScore(name, category):
    lines = read(name)
    if category == "creativity":
        raw = lines[creativityIndex].split(": ")
        return float(raw[1])
    if category == "complexity":
        raw = lines[complexityIndex].split(": ")
        return float(raw[1])
    if category == "efficiency":
        raw = lines[efficiencyIndex].split(": ")
        return float(raw[1])
    if category == "execution":
        raw = lines[executionIndex].split(": ")
        return float(raw[1])
    if category == "appearance":
        raw = lines[appearanceIndex].split(": ")
        return float(raw[1])
    if category == "composite":
        raw = lines[compositeIndex].split(": ")
        return float(raw[1])