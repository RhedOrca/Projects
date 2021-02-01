from os import listdir
from shutil import copyfile

directory = r'C:\Users\traci\PycharmProjects'
repoDir = r'C:\Users\traci\PycharmProjects\pythonOnly'

for folder in listdir(directory):
    if "pythonOnly" in folder:
        continue
    newDir = (str(directory) + '\\' + str(folder))
    for file in listdir(newDir):
        counter = 1
        if file.endswith(".py"):
            FileLoc = str(newDir + '\\' + str(file))
            copyfile(FileLoc, (str(repoDir) + '\\' + str(folder) + '-' + str(counter) + ".py"))
            counter += 1
            print(str(file) + " relocated.")

print("\n\n\n---Task Complete---")
input("Press any key to close.")