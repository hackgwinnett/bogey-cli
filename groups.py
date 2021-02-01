root = "database/"

def add(name, members):
    f = open(root + name + ".txt", "a")
    f.write("members: " + members + "\n")
    f.close()
    groups.add(name)

def rank(name):

    f = open(root + name + ".txt", "a")
    creativity = input("creativity: ")
    complexity = input("complexity: ")
    efficiency = input("efficiency: ")
    execution = input("execution: ")
    appearance = input("appearance: ")
    f.write("creativity: " + creativity + "\n")
    f.write("complexity: " + complexity + "\n")
    f.write("efficiency: " + efficiency + "\n")
    f.write("execution: " + execution + "\n")
    f.write("appearance: " + appearance + "\n")

    numCreativity = float(creativity)
    numComplexity = float(complexity)
    numEfficiency = float(efficiency)
    numExecution = float(execution)
    numAppearance = float(appearance)
    composite = (0.05 * numCreativity) + (0.3 * numComplexity) + (0.3 * numEfficiency) + (0.3 * numExecution) + (0.05 * numAppearance)
    f.write("composite: " + str(composite) + "\n")