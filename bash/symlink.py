#! /bin/python3

import os

if input("This script will delete scripts with same name, Make sure $HOME/.local/bin is in path.\nType \"yes\" to continue: ").upper() != "YES":
    quit()

os.system("mkdir $HOME/.local/bin")

for i in os.listdir():
    if i == "symlink.py": continue
    os.system("ln -sf "+os.getcwd()+"/"+i+" $HOME/.local/bin/"+i.rstrip(".sh"))
    os.system("chmod +x "+i)
    print("Symlinked", i, "to the binary location")

print("Done. You might need to relaunch your shell.")
