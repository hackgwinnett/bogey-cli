import commands
import groups
import rank
import sys
import export
import clear

commands.add("help", "", "displays all cli commands")
commands.add("addgroup", "name, members", "adds a group file to the local database")
commands.add("score", "name", "enters ranking sequence for a given group")
commands.add("rank", "category", "lists groups from highest to lowest score in the given category")
commands.add("export", "", "exports rankings for all categories into a CSV file")
commands.add("clear", "", "clears filetree")


args = sys.argv
if len(args) < 2:
    commands.display()
    exit()

c = args[1].lower()

if c == "help":
    commands.display()

if c == "addgroup":
    name = args[2]
    members = args[3]
    groups.add(name, members)

if c == "score":
    name = args[2]
    groups.rank(name)

if c == "rank":
    category = args[2].lower()
    rank.rank(category)

if c == "export":
    export.exportAll()

if c == "clear":
    clear.clear()

if not commands.commandContains(c):
    print("invalid command: " + c)
    exit()
