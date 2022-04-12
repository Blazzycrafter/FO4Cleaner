# file version 0.1 fo4
import subprocess
import os
import configparser as cp







CleanFileList = []



def loadTxt():
    with open('masterlist.txt', "r") as file:
        for line in file:
            CleanFileList.append(line.strip())


def SSEEDIT():
    global data, xedit
    for ESMFile in CleanFileList:
        print("cleaning "+ESMFile+"...")
        args = f'{xedit} -quickautoclean -autoexit -autoload "{ESMFile}" -D:{data}'
        print(args)
        subprocess.call(args, shell=False)


def cleanNames(CleanFileList):
    x = []
    for ESMFile in CleanFileList:
        if ESMFile.find(" ") != -1:
          x.append(f'\"{ESMFile}\"')
        else:
          x.append(ESMFile)
    return x


def loadConfig(path, data, xedit):
    config = cp.ConfigParser()
    try:
        config.read("settings.ini")
    except FileNotFoundError:
        print("settings.ini not found. please create it and run the script again.")

        exit()

    path = config.get("settings", "path-to-Fallout4")
    data = config.get("settings", "path-to-Fallout4-Data")
    xedit = config.get("settings", "path-of-xedit")
    return path, data, xedit


if __name__ == '__main__':
    path, data, xedit = loadConfig(path, data, xedit)
    loadTxt()
    print(CleanFileList)
    print(path)

    CleanFileList = cleanNames(CleanFileList)
    print(CleanFileList)
    SSEEDIT()
