# file version 0.1 fo4
import subprocess
import winreg
import os
import sys
import re


DEBUG = "-debug" in sys.argv

game = ""
data = "\data"
xedit = None



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






def find_highest_version_folder(search_folder):
    # Define the regular expression pattern to match the version number
    pattern = re.compile(r'\d+\.\d+\.\d+')

    # Set the initial highest version number to 0 and the corresponding folder name to None
    highest_version = '0.0.0'
    highest_folder = None

    # Loop through all subdirectories in the search folder
    for subdir in os.listdir(search_folder):
        # Check if the subdirectory name starts with "FO4Edit"
        if os.path.isdir(os.path.join(search_folder, subdir)) and subdir.startswith('FO4Edit'):
            # Check if the subdirectory name contains a version number
            match = pattern.search(subdir)
            if match:
                # Get the version number and compare it to the highest version so far
                version = match.group()
                if version > highest_version:
                    highest_version = version
                    highest_folder = os.path.join(search_folder, subdir)

    # Return the absolute path of the folder with the highest version number found (or None if no matching folders were found)
    return highest_folder


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
        f = find_highest_version_folder(game)
        xedit = f + "\FO4Edit.exe"




# Fallout 4\FO4Edit 4.0.4\FO4Edit.exe



if __name__ == '__main__':
    AutoGetPaths()
    print("Game path: ", game)
    print("Data path: ", data)

    print()
    SSEEDIT()