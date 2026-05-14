import os
import time

print("Welcome To MultiTool")

time.sleep(1)
print("What Do You Want To Do?")

print("1. Show Past Wifi Networks")
print("2. Open CMD As Admin")
print("3. Open PowerShell As Admin")

userchoice = input("Please Enter Your Choice:")

if userchoice == "1":
    os.system("netsh wlan show profiles")
elif userchoice == "2":
    os.system("powershell Start-Process cmd -Verb runAs")
elif userchoice == "3":
    os.system("powershell Start-Process powershell -Verb runAs")

print("Thank You For Using MultiTool")
time.sleep(0.5)
goagain = input("Do You Want To Re-Run The Tool? (Y/N)")

if goagain.upper() == "Y":
    os.system("cls")
    os.system("python MultiTool.py")