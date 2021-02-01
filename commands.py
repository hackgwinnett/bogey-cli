commands = []
args = []
descriptions = []

def add(c, a, d):
    commands.append(c)
    args.append(a)
    descriptions.append(d)

def display():
    print("")
    print("commands:")
    i = 0
    while i < len(commands):
        print(commands[i] + " [" + args[i] + "]: " + descriptions[i])
        i+=1

def commandContains(c):
    for i in range(len(commands)):
        if c == commands[i]:
            return True
    return False