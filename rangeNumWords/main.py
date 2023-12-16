import os

a = ""
firstnum = int(input("Input number to start from:\n> "))
lastnum = int(input("Input number to end with:\n> "))

for i in range(firstnum, lastnum):
    answer = str(i)
    answer = answer.replace("0", "zero")
    answer = answer.replace("1", "one")
    answer = answer.replace("2", "two")
    answer = answer.replace("3", "three")
    answer = answer.replace("4", "four")
    answer = answer.replace("5", "five")
    answer = answer.replace("6", "six")
    answer = answer.replace("7", "seven")
    answer = answer.replace("8", "eight")
    answer = answer.replace("9", "nine")
    a = a + answer + "\n"

print("Copied to clipboard")
os.system("wl-copy << "+a)
