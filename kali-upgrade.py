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

if Username == "kali" and Password == "os":
    print "\033[1;32m Access Granted \033[1;m"
    print "\033[1;32m"
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get upgrade -y")
    os.system("sudo apt-get dist-upgrade -y")
    os.system("sudo apt-get install kali -y")
    print"\033[1;32m"
    vmtools = raw_input("Do You Want To Install vmware tools y/n: ")
    Gnome = raw_input("Do You Want To Download Gnome y/n: ")
    xfce = raw_input("Do You Want To Download xfce4 y/n: ")
    SUBSCRIBE = raw_input("SUBSCRIBE TO MY YOUTUBE CHANNEL y/n: ")
    print "\033[1;m"
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
        exit("\033[1;32m Error \033[1;m")
    if Gnome == "y":
        os.system("sudo apt-get install gnome")
    elif Gnome == "Y":
        os.system("sudo apt-get install gnome")
    elif Gnome == "n":
        pass
    elif Gnome == "N":
        pass
    else:
        exit("\033[1;32m Error \033[1;m")
    if xfce == 'Y':
        os.system("wget https://kali.sh/xfce4.sh")
    elif xfce == 'y':
        os.system("wget https://kail.sh/xfce4.sh")
    elif xfce == 'N':
        pass
    elif xfce == 'n':
        pass
    else:
        exit("\033[1;32m Error \033[1;m")

    if SUBSCRIBE == 'Y':
        webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")
    elif SUBSCRIBE == 'y':
        webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")
    elif SUBSCRIBE == 'N':
        pass
    elif SUBSCRIBE == 'n':
        pass
    else:
        exit("\033[1;32m Error \033[1;m")
    print "\033[1;m"

elif Username == "subscribe@gmail.com" and Password == "viewer":
        print "\033[1;32m Access Granted \033[1;m"
        print "\033[1;32m"
        webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")
elif Username == "kali" and Password == "EH30":
    print "\033[1;32m Access Granted \033[1;m"
    print "\033[1;32m"
    os.system("git clone https://github.com/EH30/Email-bomber")
    os.system("git clone https://github.com/EH30/eztactics")
    os.system("git clone https://github.com/EH30/LazyDDoS")
    os.system("git clone https://github.com/EH30/batsploit")
    os.system("git clone https://github.com/EH30/geo-tracker")
    print "\33[1;m"
else:
    exit("\033[1;32m Access Denied \033[1;m")