import os
import re

apps = open("apps")
uiList = []
appList = {}

for i in apps:
    action = re.findall("\[(.*)]", i)
    name = re.findall("\[.*] (.*) ::", i)
    cmd = re.findall("\[.*] .* :: (.*)", i)
    uiList.append("[" + action[0] + "] " + name[0])
    appList[str(action[0])] = cmd

while True:
    print("Welcome " + os.getlogin() + "\nSelect an option from the list below:\n")
    for i in uiList:
        print(i)
    option = input("\n> ")

    if option in appList:
        print("Starting " + option)
        os.system(appList[option][0])

    elif "!" in option:
        option = option.strip("!")
        os.system(option)
        input("Press enter to continue.")

    os.system("clear")
