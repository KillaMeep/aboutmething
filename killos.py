import time
import os
import sys
import platform
from termcolor import *
import random
import cursor
import socket
import datetime
import time
#version info
version='1.0.3'

build='1.26.2022'




#setups


start_time = int(time.time())
if os.name == 'nt':
    os.system("cls")
    os.system("color")
    os.system("echo off")
    os.system("title KillOS")
else:
    os.system('clear')
print(colored(f'KillOS {version}', 'red'))
print(colored(f'Release ver. {build}','red'))
systemname = colored(platform.system(),'green')
systemversion = colored(platform.release(),'green')
print(colored(f'Currently running on {systemname} {systemversion}'))
print('\n')
userat = colored('user@','blue')
name=colored(socket.gethostname(),'blue')
sysname = userat+name
discordid=colored('KillaMeep#6288','yellow',attrs=['bold'])
email =colored('killerpenguin729@gmail.com','yellow',attrs=['bold'])
cursor.hide()
def clearscreen(continueon):
    if os.name=='nt':
        os.system('cls')
        if continueon==True:
            userinput_command = input(f'({sysname})Input a command>')
    else:
        os.system('clear')
        if continueon==True:    
            userinput_command = input(f'({sysname})Input a command>')
def timern():
    #print out the time for the repromt/time command stuffs
    return(colored(datetime.datetime.now().strftime("%X"),'cyan',attrs=['bold']))
def reprompt():
    #run the reprompt after commands
    print('\n')
    checkinput(input(f'({sysname} | {timern()})Input a command>'))

for x in range(0,random.randint(2,4)):
    time.sleep(1)
    if (x % 2) == 0:
        print('\rLoading..', end='\r',flush=True)
    else:
        print('Loading...',end='\r',flush=True)
print(colored('Welcome   \b' + '\b','green',attrs=['bold']))
tempdt = datetime.datetime.now()
print(f'It is {tempdt.strftime("%A")}, {tempdt.strftime("%B")}, {tempdt.strftime("%d")} {tempdt.strftime("%Y")} at {tempdt.strftime("%X")}')
time.sleep(0.2)
cursor.show()
#setup end

def openurl(url):
    #modularly open urls in native browser
    if os.name == 'nt':
        os.system(f'start {url}')
    else:
        os.system(f'open {url}')
def checkinput(command):
    #check commands, define what they do
    if command.lower() == 'exit':
        print('Shutting down.')
        time.sleep(.5)
        clearscreen(continueon=False)
        exit()
    
    
    elif command.lower() == 'info':
        print('Developed by KillaMeep as an about me type of thing.')
        print('Basically I got bored, and this was the outcome!')
        reprompt()
    elif command.lower() == 'github' or command.lower() == 'git':
        gitcheck = input("Check me out on github! Should we go there now (y/n): ").lower()
        if gitcheck == 'yes' or gitcheck == 'y':
            print(colored('Sending you there now!','green'))
            time.sleep(1)
            openurl('https://github.com/KillaMeep')
            reprompt()
        else:
            print('Ok. Returning back.')
            reprompt()
    elif command.lower() == 'discord':
        print(f'You can find him on discord at {discordid}')
        knowmore = input('Want to know more (y/n): ').lower()
        if knowmore == 'y' or knowmore == 'yes':
            openurl('https://discords.com/bio/p/killameep')
            reprompt()
        else:
            reprompt()
    elif command.lower() == 'email':
        print(f'You can contact me at {email}')
        reprompt()


    elif command.lower() == 'rr' or command.lower() == 'rick':
        openurl('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        reprompt()
    elif command.lower() == 'hello':
        print('World!')
        reprompt()
    elif command.lower() == 'steam':
        print('Feel free to shoot me a friend request and let me know you found this command!')
        openurl('https://steamcommunity.com/id/KillaMeep')
        reprompt()
    elif command.lower() == 'moar':
        disc=colored('disord','green',attrs=['bold'])
        print('If you found this one, add me on discord and give me some suggestions! (I may even add a command of your request <: )')
        print('Do the command {disc}!')
        reprompt()
    elif command.lower() == 'version' or command.lower() == 'ver':
        now = int(time.time())
        ut = str(datetime.timedelta(seconds=now-start_time))
        uptime = colored(ut,'blue')
        kos = colored('KillOS','red')
        print(f'"{kos}"')
        print(colored(f'Version {version} / Build {build}','red'))
        print(f'Being hosted on {systemname} {systemversion}')
        print(f'System uptime: {uptime}')
        print(colored('Made with <3 by KillaMeep','magenta'))
        reprompt()
    elif command.lower() == '':
        reprompt()
    elif command.lower() == '42':
        print("They know the answer")
        reprompt()
    elif command.lower() == 'snek':
        ifsnek = input('Would you like to play snake (y/n): ').lower()
        if ifsnek == 'y' or ifsnek == 'yes':
            print('OK! Lets play!')
            print('Please wait...')
            if os.name == 'nt':
                os.system('curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/snake.bat -O')
            else:
                error = colored('Error!', 'red')
                print(f'{error} Running {systemname} {systemversion}')
                print('Unable to play snake on linux. Sorry -_-')
                reprompt()
            print('Install complete. Launching now!')
            os.system('snake.bat')
            os.system('del snake.bat')

    elif command.lower() == 'time' or command.lower() == 'date' or command.lower() == 'dt':
        print(f'It is {datetime.datetime.now().strftime("%A")}, {datetime.datetime.now().strftime("%B")}, {datetime.datetime.now().strftime("%d")} {datetime.datetime.now().strftime("%Y")} at {datetime.datetime.now().strftime("%X")}')

        reprompt()
    elif command.lower() == '?help' or command.lower() == 'help' or command.lower() == '?':
        print('List of commands: ')
        print('\n')
        print('Info    | Displays basic info on the program')
        print('Github  | Allows you to get a link to my github')
        print('Discord | Shows my discord usertag, and allows you to check for more details')
        print('Email   | Lets you get his email')
        print('Time    | Shows the current time at the users location')
        print('Snek    | Lets you play a (pretty bad) game of snake')
        print('Rick    | You know what it does...')
        print('Version | Displays version info')
        print('Exit    | Exits KillOS')
        print(colored('(Theres a few easter eggs too)','cyan'))
        reprompt()
    else:
        help = (colored('help','green',attrs=['bold']))
        print(f'Command "{command.lower()}" not recognised. Please try again or do {help} for a list of commands.')
        reprompt()
checkinput(input(f'({sysname} | {timern()})Input a command>'))
