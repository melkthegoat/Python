import os
import subprocess
import platform
import time

presets = {
    "1": "Preset 1: Test Preset", # Change these to whatever you want, just make sure to change the apps variables as well
    "2": "Preset 2: Test Preset",
    "3": "Preset 3: Test Preset"
}

apps = {
    "1": ["cmd.exe"], # Again, test presets just opening cmd, notepad, and calc, change these to whatever you want, just make sure to change the presets variables as well
    "2": ["calc.exe"],
    "3": ["notepad.exe"]
}


print("Automated Preset Manager:")
time.sleep(1)
print("This program will automatically manage your presets for you, Which preset would you like to open?:")

choice = input("Enter the preset number (1, 2, or 3): ") # Here you can explain what the presets are, however as this is a test I have just used 1, 2 and 3

if choice in presets:
    print("Opening Preset", choice)

    for app in apps[choice]:
        try:
            subprocess.Popen(app)
        except FileNotFoundError as e:
            print("Error opening", app, ":", e)
