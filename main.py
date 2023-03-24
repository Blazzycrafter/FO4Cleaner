# file version 0.1 fo4
import subprocess
import winreg
import os
import sys


arguments = sys.argv

start_parameter = arguments[1:]

debugq = start_parameter.count("-debug")


game = ""
data = "\data"
xedit = None

if debugq:
    DEBUG = True
else:
    DEBUG = False


def dprint(string):
    if DEBUG:
        print(string)


CleanFileList = ["DLCRobot.esm", "DLCCoast.esm", "DLCNukaWorld.esm", "DLCworkshop01.esm", "DLCworkshop02.esm", "DLCworkshop03.esm"]





def SSEEDIT():
    global data, xedit
    for ESMFile in CleanFileList:
        print("cleaning " + ESMFile + "...")
        args = f'{xedit} -quickautoclean -autoexit -autoload "{ESMFile}" -D:"{data}"'
        dprint(args)
        subprocess.call(args, shell=False)





def AutoGetPaths():
    global game, data, xedit
    try:
        # open the registry key containing the game path
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\Bethesda Softworks\\Fallout4")
        # read the value of the "InstallLocation" key
        game = winreg.QueryValueEx(key, "Installed Path")[0]
    except WindowsError:
        try:
            # open the registry key containing the game path
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Bethesda Softworks\\Fallout4")
            # read the value of the "InstallLocation" key
            game = winreg.QueryValueEx(key, "Installed Path")[0]
        except WindowsError:
            exit("Could not find game path in registry")
    finally:
        data = game + "data"
        xedit = game + "FO4Edit 4.0.4\FO4Edit.exe"




# Fallout 4\FO4Edit 4.0.4\FO4Edit.exe



if __name__ == '__main__':
    AutoGetPaths()
    print("Game path: ", game)
    print("Data path: ", data)
    print()
    SSEEDIT()
