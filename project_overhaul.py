import subprocess

# Welcome to Project Overhaul.

'''                         This tool is intended to integrate various penetration testing tools into a single command line script              '''

'''                         If you forgot what this tool does, just execute it and look at the output, it will guide you   '''

##############################################################################################################################################################

banner = '''
   ___             _         __    ____               __             __
  / _ \_______    (_)__ ____/ /_  / __ \_  _____ ____/ /  ___ ___ __/ /
 / ___/ __/ _ \  / / -_) __/ __/ / /_/ / |/ / -_) __/ _ \/ _ `/ // / / 
/_/  /_/  \___/_/ /\__/\__/\__/  \____/|___/\__/_/ /_//_/\_,_/\_,_/_/  
             |___/                                                     

                                                ~ Created by Afnaan'''

##############################################################################################################################################################

#                         Text Styles

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
brown = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
light_gray = "\033[0;37m"
dark_gray = "\033[1;30m"
light_red = "\033[1;31m"
light_green = "\033[1;32m"
yellow = "\033[1;33m"
light_blue = "\033[1;34m"
light_purple = "\033[1;35m"
light_cyan = "\033[1;36m"
light_white = "\033[1;37m"
bold = "\033[1m"
faint = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
blink = "\033[5m"
negative = "\033[7m"
crossed = "\033[9m"
reset = "\033[0m"




#                         Main menu

def main_menu():
    subprocess.run("clear")
    print(light_cyan + banner + reset)
    print()
    print(light_blue + "               MENU              ")
    print("              ------                " + reset)
    print()
    print(light_green + "[1]" + reset +" - Reconnaissance")
    print(light_red + "[2]" + reset + " - Exploitation")
    print(light_purple + "[3]" + reset + " - Miscellaneous")
    print(light_cyan + "[4]" + reset + " - Exit")
    print()
    response = input(" >    ")
    
    if response == '1':
        subprocess.run("clear", shell=True)
        reconnaissance_menu()

    elif response == '2':
        subprocess.run("clear", shell=True)
        exploitation_menu()
    
    elif response == '3':
        subprocess.run("clear", shell=True)
        miscellaneous_menu()
    
    elif response == '4':
        print(light_cyan + "\nGoodbye!\n" + reset)
    
    else:
        subprocess.run("clear", shell=True)
        print("")
        print(light_red + "Enter a valid option" + reset)
        main_menu()


#                             Reconnaissance menu

def reconnaissance_menu():
    print()
    print(light_blue + "               RECONNAISSANCE               ")
    print("              ----------------                    " + reset)
    print()
    print(light_green + "[1]" + reset + " - Nmap")
    print(light_cyan + "[2]" + reset + " - Back to main menu")
    print()

    response = input(" >    ")

    if response == '1':
        print()
        print(light_green + "Launching nmap..." + reset)
        print()
        result = subprocess.run("nmap",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: nmap is not installed" + reset)
            install = input("Do you wish to install nmap? (requires sudo password)")
            if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                print(light_green + "Installing Nmap..." + reset)
                result = subprocess.run("sudo apt update && sudo apt install nmap",shell=True)
                if result.returncode == 0:
                    print(light_green + "Nmap has been successfully installed" + reset)
                    reconnaissance_menu()
                else:
                    print(light_red + "Could not install nmap! Please install it manually" + reset)
            else:
                reconnaissance_menu()

    elif response == '2':
        main_menu()
    
    else:
        print("")
        print(light_red + "Enter a valid option" + reset)
        reconnaissance_menu()

#                             Exploitation menu

def exploitation_menu():
    print("")
    print(light_blue + "               EXPLOITATION                   ")
    print("              --------------                   " + reset)
    print("")
    print(light_green + "[1]" + reset + " - Metasploit")
    print(light_green + "[2]" + reset + " - SQLmap")
    print(light_green + "[3]" + reset + " - amass")
    print(light_cyan + "[4]" + reset + " - Back to main menu")
    print("")

    response = input(" >    ")

    if response == '1':
        print()
        print(light_green + "Launching Metasploit Framework..." + reset)
        print()
        result = subprocess.run("msfconsole",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: metasploit framework is not installed" + reset)
            install = input("Do you wish to install Metasploit Framework? (requires sudo password)")
            if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                print(light_green + "Installing Metasploit Framework..." + reset)
                result = subprocess.run("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall",shell=True)
                if result.returncode == 0:
                    print(light_green + "Metasploit Framework has been successfully installed" + reset)
                    exploitation_menu()
                else:
                    print(light_red + "Could not install Metasploit Framework! Please install it manually" + reset)
            else:
                exploitation_menu()

    elif response == '2':
        print()
        print(light_green + "Launching SQLmap..." + reset)
        print()
        result = subprocess.run("sqlmap",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: sqlmap is not installed" + reset)
            install = input("Do you wish to install sqlmap? (requires sudo password)")
            if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                print(light_green + "Installing sqlmap..." + reset)
                result = subprocess.run("sudo apt update && sudo apt install sqlmap",shell=True)
                if result.returncode == 0:
                    print(light_green + "sqlmap has been successfully installed" + reset)
                    exploitation_menu()
                else:
                    print(light_red + "Could not install sqlmap! Please install it manually" + reset)
            else:
                exploitation_menu()

    elif response == '3':
        print()
        print(light_green + "Launching amass..." + reset)
        print()
        result = subprocess.run("amass",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: amass is not installed" + reset)
            install = input("Do you wish to install amass? (requires sudo password)")
            if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                print(light_green + "Installing amass..." + reset)
                result = subprocess.run("sudo apt update && sudo apt install amass",shell=True)
                if result.returncode == 0:
                    print(light_green + "amass has been successfully installed" + reset)
                    exploitation_menu()
                else:
                    print(light_red + "Could not install amass! Please install it manually" + reset)
            else:
                exploitation_menu()

    elif response == '4':
        main_menu()
    
    else:
        print()
        print(light_red + "Enter a valid option" + reset)
        exploitation_menu()

#                             Miscellaneous menu

def miscellaneous_menu():
    print()
    print(light_blue + "               MISCELLANEOUS               ")
    print("              ---------------                    " + reset)
    print()
    print(light_green + "[1]" + reset + " - Display Banner")
    print(light_green + "[2]" + reset + " - Install all tools included in project overhaul")
    print(light_cyan + "[3]" + reset + " - Back to main menu")
    print()

    response = input(" >    ")

    if response == '1':
        print(light_cyan + banner + reset)
        miscellaneous_menu()

    elif response == '2':
        print(light_green + "Installing all tools, This may take a while..." + reset)
        noerrors = True
        subprocess.run("sudo apt update",shell=True)
        
        #nmap
        print(light_green + "Installing nmap..." + reset)
        result = subprocess.run("sudo apt install nmap",shell=True)
        if result.returncode == 0:
            print(light_green + "Nmap has been successfully installed" + reset)
        else:
            print(light_red + "Could not install nmap! Please install it manually" + reset)
            noerrors = False
        
        #metasploit
        result = subprocess.run("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall",shell=True)
        if result.returncode == 0:
            print(light_green + "Metasploit Framework has been successfully installed" + reset)
        else:
            print(light_red + "Could not install Metasploit Framework! Please install it manually" + reset)
            noerrors = False
        
        #sqlmap
        print(light_green + "Installing sqlmap..." + reset)
        result = subprocess.run("sudo apt install sqlmap",shell=True)
        if result.returncode == 0:
            print(light_green + "sqlmap has been successfully installed" + reset)
        else:
            print(light_red + "Could not install sqlmap! Please install it manually" + reset)
            noerrors = False
        
        #amass
        print(light_green + "Installing amass..." + reset)
        result = subprocess.run("sudo apt update && sudo apt install amass",shell=True)
        if result.returncode == 0:
            print(light_green + "amass has been successfully installed" + reset)
        else:
            print(light_red + "Could not install amass! Please install it manually" + reset)
            noerrors = False

        if noerrors == True:
            print(light_green + "All tools have been installed!" + reset)
        else:
            print(light_red + "one or more tools were not installed due to an error!" + reset)

    elif response == '3':
        main_menu()
    
    else:
        print("")
        print(light_red + "Enter a valid option" + reset)
        miscellaneous_menu()








#                           Running code
try:
    main_menu()
except KeyboardInterrupt:
    print(light_red + "Program was interrupted by the user" + reset)