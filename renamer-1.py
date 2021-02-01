import os
from shutil import copyfile

directory = r'C:\Users\traci\PycharmProjects'
repoDir = r'C:\Users\traci\PycharmProjects\pythonOnly'

for folder in os.listdir(directory):
    if "pythonOnly" in folder:
        continue
    newDir = (str(directory) + '\\' + str(folder))
    for file in os.listdir(newDir):
        counter = 1
        if file.endswith(".py"):
            FileLoc = str(newDir + '\\' + str(file))
            copyfile(FileLoc, (str(repoDir) + '\\' + str(folder) + '-' + str(counter) + ".py"))
            counter += 1
            print(str(file) + " relocated.")
