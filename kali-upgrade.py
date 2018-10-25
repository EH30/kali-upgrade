import os
import webbrowser
import sys

#Created By: TheTechHacker #
#I made This Script For Fun You can update kali linux Without This script #
#SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ      #

os.system("clear")

print "\033[1;32m"
Username = raw_input("Username: ")
Password = raw_input("Password: ")
print "\033[1;m"

if Username == "kali":
    if Password == "server":
        print "\033[1;32m Access Granted \033[1;m"
        print "\033[1;32m"
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get upgrade -y")
        os.system("dist-upgrade -y")
        os.system("sudo apt-get install kali -y")
        print "\033[1;m"
        print"\033[1;32m"
        vmtools = raw_input("Do You Want To Install vmware tools y/n: ")
        Gnome = raw_input("Do You Want To Download Gnome y/n: ")
        xfce = raw_input("Do You Want To Download xfce4 y/n: ")
        print "\033[1;m"

    else:
        exit("\033[1;32m Access Denied \033[1;m")
else:
    exit("\033[1;32m Access Denied \033[1;m")

print "\033[1;32m"

if vmtools == 'Y':
    os.system("sudo apt install open-vm-tools-desktop -y")
elif vmtools == 'y':
    os.system("sudo apt install open-vm-tools-desktop -y")
elif vmtools == 'N':
    pass
elif vmtools == 'n':
    pass
else:
    exit("Error")


if Gnome == "y":
    os.system("sudo apt-get install gnome")
elif Gnome == "Y":
    os.system("sudo apt-get install gnome")
elif Gnome == "n":
    pass
elif Gnome == "N":
    pass
else:
    exit("Error")



if xfce == 'Y':
    os.system("wget http://kali.org/xfce4.sh")
elif xfce == 'y':
    os.system("wget http://kail.org/xfce4.sh")
elif xfce == 'N':
    pass
elif xfce == 'n':
    pass
else:
    exit("Error")

print "\033[1;m"


print "\033[1;32m"
SUBSCRIBE = raw_input("SUBSCRIBE TO MY YOUTUBE CHANNEL y/n: ")

if SUBSCRIBE == 'Y':
    webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")
elif SUBSCRIBE == 'y':
    webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")
elif SUBSCRIBE == 'N':
    pass
elif SUBSCRIBE == 'n':
    pass
else:
    exit("Error")
print "\033[1;m"
