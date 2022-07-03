#!/bin/bash

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstinstall-all.sh        [Update:  2022-07-03 | 5:00  - PM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The tool for install all dependencies and install OPST in                #
#  /usr/share/omegapstoolkit-master/ and write the 'opst' command in        #
#  /usr/bin                                                                 #
#                                                                           #
#  Language  ~  Bash                                                        #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © PSociety™, 2022 All rights reserved     #
#---[Operating System]------------------------------------------------------#
#  Developed for linux                                                      #
#---[Licence]---------------------------------------------------------------#
#  GNU General Public License v3.0                                          #
#  -------------------------------                                          #
#                                                                           #
#  This program is free software; you can redistribute it and/or modify     #
#  it under the terms of the GNU General Public License as published by     #
#  the Free Software Foundation; either version 2 of the License, or        #
#  (at your option) any later version.                                      #
#                                                                           #
#  This program is distributed in the hope that it will be useful,          #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#  GNU General Public License for more details.                             #
#                                                                           #
#  You should have received a copy of the GNU General Public License along  #
#  with this program; if not, write to the Free Software Foundation, Inc.,  #
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.              #
#---------------------------------------------------------------------------#

# Colors #
## Basic colors ##
W='\033[0m'      # white (normal)
R='\033[31m'     # red
G='\033[32m'     # green
O='\033[33m'     # orange
B='\033[34m'     # blue
P='\033[35m'     # purple
C='\033[36m'     # cyan
GR='\033[37m'    # gray
D='\033[2m'      # dims current color. {W} resets.

## Text formating ##
bold='\033[1m'
italic='\033[3m'
underscore='\033[4m'
normal='\033[22m'
# ###### #

# opstinstall's version #
__VERSION_OPSTINSTALL=$(cat /usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstinstall)
# ##################### #

INSTALL_DIR="/usr/share/OmegaPSToolkit"
BIN_DIR="/usr/bin"
TEMP_DIR="/tmp/OmegaPSToolkit"


# Check if user have root privileges
if [ $(id -u) != "0" ]; then
    # Many fresh installed linux distros do not come with sudo installed
    which sudo > /dev/null 2>&1
    if [ "$?" != "0" ]; then
        
        echo "[$C$D$(date +"%T")$W]    ["$R"ERROR$W]  You Linux distribution doesn't have the \"sudo\" command pre-install. Install the current \"sudo\" command..."
        sleep 1
        apt update -y && apt-get install sudo -y
    fi
    ####
        if ! hash sudo 2>/dev/null; then
            echo -e " 
[$C$D$(date +"%T")$W]  ["$R"ERROR$W]  OPSTInstall-all could be run as the$R root user$W or with the$R sudo command$W
[$C$D$(date +"%T")$W]  ["$R"INFO$W]  Re-run the opstinstall-all with$R sudo$W or with the$R root$W user
[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Run :$B sudo opstinstall-all $W"
                exit 1
        else # Switch to sudo (root)
            echo
            echo -e "[$C$D$(date +"%T")$W]  ["$R"ERROR$W]  OPSTInstall-all could be run as the$R root user$W or with the$R sudo command$W
[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Switching to$R root user$W to run the$G opstinstall-all$W
"
            sudo -E bash $0 $@
            exit 0
        fi
    fi
####

# The main script
clear

echo -e "
$GR$D _______ ______ _______ _______ _______               __          __ __ $W$G  OPSTInstall's$D version: $__VERSION_OPSTINSTALL$W
$GR$D|       |   __ \     __|_     _|_     _|.-----.-----.|  |_.---.-.|  |  |$G$D  Coded by MyMeepSQL for © PSociety™$W
$GR$D|   -   |    __/__     | |   |  _|   |_ |     |__ --||   _|  _  ||  |  |$W$D  A massive penetration testing toolkit$W
$GR$D|_______|___|  |_______| |___| |_______||__|__|_____||____|___._||__|__|$C$D  https://github.com/MyMeepSQL/OmegaPSToolkit$W
$GR$D + ------------------------ !* Welcome to the OPSTInstall-all *! ------------------------ +$W

[$C$D$(date +"%T")$W]  ["$G"CHECK$W]  Checking for internet connection..."

# First check of setup for internet connection by connecting to google over http
wget -q --tries=10 --timeout=5 --spider http://google.com
if [ $? -eq 0 ]; then
    echo -e '['$C$D$(date +"%T")$W']  ['$G'INFO'$W']  Internet status: '$G'Connected'$W'.\n'
    echo -e '+ ---- ----=[  '$underscore'This tool will:'$W'                                                                                                           ]
            [  ...'$G'Update'$W' your system ('$R'apt update'$W'),                                                                                       ]
            [  ...Install '$G'Python3'$W' and '$G'PIP3'$W' ('$R'apt install python3 python3-pip'$W'),                                                            ]
            [  ...Install all '$G'tools'$W' that OPST must have,                                                                                 ]
            [  ...Create the OmegaPSToolkit folder to '$G'/usr/share/OmegaPSToolkit/'$W'" and '$R'clone OmegaPSToolkit files into it'$W' (from'$R' GitHub'$W'),  ]
            [  ...Create the commands '$G'opstconsole'$W', '$G'opsthelp'$W', '$G'opstupdate'$W', '$G'opstsetup'$W' and '$G'opstinstall-all'$W' into '$G'/usr/bin/'$W',                   ]
            [  ...Apply all rights on the new file in '$G'/usr/share/OmegaPSToolkit/'$W' and for all commands in '$G'/usr/bin/'$W'.                      ]
            [  ...Install '
    echo
    echo -ne "[$C$D$(date +"%T")$W]  ["$C"QUESTION$W]  Do you want to continue? [Y/n] "
    read y_n
    if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ] || [ ! "$y_n" ]; then
        
        echo -e "
$G$D----------------------------------------------------------------------------------------$W

[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Updating the system..."
        sleep 0.5
        apt-get update -qq -y && apt-get update -qq --fix-missing -y
        
        echo -e "[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  Update complete."
        sleep 1
        
        echo -e "
$G$D----------------------------------------------------------------------------------------$W

[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Installing Python3 and PIP3..."
        sleep 0.5
        apt-get install -qq -y git python3 python3-pip whois traceroute net-tools
        
        echo -e "[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  Install complete."
        sleep 1
        echo -e "
$G$D----------------------------------------------------------------------------------------$W
"
        if [ -d "$INSTALL_DIR" ]; then
            
            echo -e "[$C$D$(date +"%T")$W]  ["$O"WARNING$W]  A OmegaPSToolkit directory was found. ("$G"/usr/share/OmegaPSToolkit$W)"
            echo -ne "[$C$D$(date +"%T")$W]  ["$C"QUESTION$W]  Do you want to replace it ? [Y/n] "
            read y_n
            if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ] || [ ! "$y_n" ]; then
                
                echo -e "
$G$D--------------------------------$W
[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Answer: "$G"Yes$W.
$G$D--------------------------------$W

[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Removing the current OmegaPSToolkit folder..."
                    sleep 0.5
                rm -fr "$INSTALL_DIR"
                rm -fr "$TEMP_DIR"
                rm -f "$BIN_DIR/opstconsole"
                rm -f "$BIN_DIR/opstsetup"
                rm -f "$BIN_DIR/opstupdate"
                rm -f "$BIN_DIR/opsthelp"
                rm -f "$BIN_DIR/opstinstall-all"

                echo -e "[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  Done for the OmegaPSToolkit's remove."
                sleep 1
                echo -e "
$G$D----------------------------------------------------------------------------------------$W
"
            else
                
                echo -e "
$G$D---------------------------------$W
[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Answer: "$R"No$W.
$G$D---------------------------------$W

[$C$D$(date +"%T")$W]  ["$R"ERROR$W]  You must remove all old OmegaPSToolkit files for install the new ones.
[$C$D$(date +"%T")$W]  ["$O"INFO$W]  Exiting opstinstall-all..."
                exit 1
            fi
        fi

        # for run the SetupTool (opstsetup) anywhere in the terminal. The "opstsetup" will be write into "/usr/share/OmegaPSToolkit"
        echo -e "[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Installing OmegaPSToolkit into $G/usr/share/OmegaPSToolkit/$W..."
        sleep 0.5

        mkdir $INSTALL_DIR
        mkdir $TEMP_DIR

        git clone -q https://github.com/MyMeepSQL/OmegaPSToolkit.git "$TEMP_DIR"

        # for the "/usr/share/OmegaPSToolkit"
        cp -r "$TEMP_DIR/"* "$INSTALL_DIR/"
        ##

        # for the "/usr/bin"
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstconsole.py" '${1+"$@"}' > "$TEMP_DIR/opstconsole"
        echo "#!/bin/bash
        bash $INSTALL_DIR/opstupdate.sh" '${1+"$@"}' > "$TEMP_DIR/opstupdate"
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opstsetup.py" '${1+"$@"}' > "$TEMP_DIR/opstsetup"
        echo "#!/bin/bash
        python3 $INSTALL_DIR/opsthelp.py" '${1+"$@"}' > "$TEMP_DIR/opsthelp"
        echo "#!/bin/bash
        bash $INSTALL_DIR/opstinstall-all.sh" '${1+"$@"}' > "$TEMP_DIR/opstinstall-all"

        cp "$TEMP_DIR/opstconsole" "$BIN_DIR"
        cp "$TEMP_DIR/opstupdate" "$BIN_DIR"
        cp "$TEMP_DIR/opstsetup" "$BIN_DIR"
        cp "$TEMP_DIR/opsthelp" "$BIN_DIR"
        cp "$TEMP_DIR/opstinstall-all" "$BIN_DIR"

        rm -fr "$TEMP_DIR"
        ##
        
        echo -e "[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  Done for the OmegaPSToolkit's installation."
        sleep 1
        echo -e "
$G$D--------------------------------------------------------------------------------------$W
"

        # Apply all rights
        
        echo -e "[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Apply all rights to files..."
        sleep 0.5

        # for '/usr/share/OmegaPSToolkit'
        chmod 777 -R "$INSTALL_DIR"

        # chmod 777 "$INSTALL_DIR/opstconsole.py"
        # chmod 777 "$INSTALL_DIR/opstupdate.sh"
        # chmod 777 "$INSTALL_DIR/opstsetup.py"
        # chmod 777 "$INSTALL_DIR/opstinstall-all.sh"
        # chmod 777 "$INSTALL_DIR/opsthelp.py"

        # chmod 777 "$INSTALL_DIR/opstfunctions.py"
        # chmod 777 "$INSTALL_DIR/opstcolors.py"
        # chmod 777 "$INSTALL_DIR/opstversions.py"
        ##

        # for '/usr/bin'
        chmod 777 "$BIN_DIR/opstconsole"
        chmod 777 "$BIN_DIR/opstupdate"
        chmod 777 "$BIN_DIR/opstsetup"
        chmod 777 "$BIN_DIR/opstinstall-all"
        chmod 777 "$BIN_DIR/opsthelp"
        ##
        
        echo -e "[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  Apply complete."
        sleep 1
        
        echo -e "
$G$D--------------------------------------------------------------------------------------$W

[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  All Done.
"
        sleep 0.4
        echo -e "$G$D--------------------------------------------------------------------------------------$W
"
        
        echo -ne "[$C$D$(date +"%T")$W]  ["$C"QUESTION$W]  Do you want to reload your terminal (just in case) ? [Y/n] "
        read y_n
        if [ "$y_n" = 'Y' ] || [ "$y_n" = 'y' ] || [ ! "$y_n" ]; then
            
            echo -e "
$G$D--------------------------------------------------------------------------------------$W

$G$D---------------------$W
[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Reloading...
$G$D---------------------$W"
            sleep 0.5
            reset
            
            echo -e "
$G$D----------------------------------------------------------------------------------------------------------------------------------------------------$W

[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  All programmes and all '"$G"opst"$W"' commands are now "$G"install"$W" on you machine. Now run the "$G"opstsetup"$W" with "$B"\""$W"sudo opstsetup install"$B"\""$W".

$G$D----------------------------------------------------------------------------------------------------------------------------------------------------$W
"
            exit 0
        else
            
            echo -e "
$G$D--------------------$W
[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Answer: "$R"No$W.
$G$D--------------------$W

$G$D----------------------------------------------------------------------------------------------------------------------------------------------------$W

[$C$D$(date +"%T")$W]  ["$G"SUCCESS$W]  All programmes and all '"$G"opst"$W"' commands are now "$G"install"$W" on you machine. Now run the "$G"opstsetup"$W" with "$B"\""$W"sudo opstsetup install"$B"\""$W".

$G$D----------------------------------------------------------------------------------------------------------------------------------------------------$W
"
            exit 0
        fi
    else
        
        echo -e "[$C$D$(date +"%T")$W]  ["$O"INFO$W]  Abort."
        exit 1
    fi
else
    
    echo -e "[$C$D$(date +"%T")$W]  ["$G"INFO$W]  Internet status: "$R"Not connected"$W".
[$C$D$(date +"%T")$W]  ["$R"ERROR$W]  Not Internet connexion found, please check you are connected to Internet and retry."
    exit 1
fi
