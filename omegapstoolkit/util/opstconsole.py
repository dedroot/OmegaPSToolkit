#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstconsole.py                [Update: 2022-05-29 | 12:13 AM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  OmegaPSTookit ~ A massive penetration testing toolkit for penteser       #
#                                                                           #
#  Language  ~  Python3                                                     #
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

# Version #
## opstconsole's version ##
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstconsole", "r", encoding="utf-8") as opstconsole_version:
        __VERSION_OPSTCONSOLE = opstconsole_version.read()

## opstconsole_cli's version ##
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstconsole_cli", "r", encoding="utf-8") as opstconsole_CLI_version:
        __VERSION_OPSTCONSOLE_CLI = opstconsole_CLI_version.read()

## opstinstall's version ##
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstinstall", "r", encoding="utf-8") as opstinstall_version:
        __VERSION_OPSTINSTALL = opstinstall_version.read()

## opstinfo's version ##
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstinfo", "r", encoding="utf-8") as opstinfo_version:
        __VERSION_OPSTINFO = opstinfo_version.read()

## opstsetup's version ##
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstsetup", "r", encoding="utf-8") as opstsetup_version:
        __VERSION_OPSTSETUP = opstsetup_version.read()

## opstupdate's version ##
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstupdate", "r", encoding="utf-8") as opstupdate_version:
        __VERSION_OPSTUPDATE = opstupdate_version.read()
# ####### #

# Custom imports
"""
In the "function/"
"""
from abort import *
from clear import clear
from system_colors import system_colors as sc
from distribution_name import *
from exit_odst import *
from get_mac_adress import *
from get_private_ip import *
from get_public_ip import *
from gpudetails import *
from internet_check import *
from invalid_option import *
from not_linux import *
from option_error import *
from os_details import *
from ram_info import *
from y_or_n_error import *
from criticalmsg import *

"""
In the "function/help for comand/"
"""
from help_for_command.cli_netstat_help import *
from help_for_command.cli_nslookup_help import *
from help_for_command.cli_ping_help import *
from help_for_command.cli_traceroute_help import *
from help_for_command.cli_whois_help import *

"""
In the "function/help_for_command/"
"""
from help_info_messages.cli_fullinfomsg import *
from help_info_messages.cli_helpmsg import *
from help_info_messages.cli_infomsg import *
from help_info_messages.mainpage_helpmsg import *

"""
In the "function/man_help_for_command/"
"""
from man_help_for_command.cli_netstat_man_help import *
from man_help_for_command.cli_nslookup_man_help import *
from man_help_for_command.cli_ping_man_help import *
from man_help_for_command.cli_traceroute_man_help import *
from man_help_for_command.cli_whois_man_help import *

from time import sleep
#-Check module is installed---------------------------------------------------------------------#
try:
    # Check if the user run OPST with root privilege
    import os
    if os.getuid() != 0:
        time=strftime("%X")
        permerror =f"""
[{sc.C}{sc.D}{time}{sc.W}]  [{sc.R}ERROR{sc.W}]  OPSTConsole could be run as the {sc.R}root user{sc.W} or with the {sc.R}sudo command{sc.W}
[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  Re-run the opstconsole with {sc.R}sudo{sc.W} or with the {sc.R}root{sc.W} user
[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  Run : {sc.C}sudo opstconsole{sc.W}
"""
        sys.exit(permerror)
except AttributeError:
    not_linux()
else:
    clear()
    # Checking if modules are installed
    sys.stdout.write("\x1b]2;Checking if all modules are [OK]\x07")
    try:
        print(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  Checking if the current modules of OPST are installed...")
        sleep(1.5)
        sys.path.insert(0, '/mnt/d/Dev/PSociety/Tools/OmegaPSToolkit (OPST toolkit)/OmegaPSToolkit (OPST toolkit)/functions')
        import os
        import sys
        import time
        import itertools
        import psutil
        import progress
        import colored
        import shutil
        import time
        import platform
        import shlex
        import textwrap
        from collections import namedtuple
        from builtins import format
        
        from criticalmsg import *
        """
        In the "function/"
        """
        from colored_colors import colored_colors as cc
        from opstinfo import opstinfo
        
        time=strftime("%X")
        print(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  All modules are install !")
        try:
            time=strftime("%X")
            print(f"\n[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  Checking for Internet internet_check... (Press CTRL + C to skip)")
            sleep(1)
            if internet_check() == True:
                internetstatus = f"{sc.G}Connected{sc.W}"
                time=strftime("%X")
                print(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  Internet status : {sc.G}Connected{sc.W}.")
            else:
                internetstatus = f"{sc.R}Not connected{sc.W}"
                time=strftime("%X")
                print(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.O}WARNING{sc.W}]  Internet status : {sc.R}Not connected{sc.W}.")
            print()
        except KeyboardInterrupt:
            time=strftime("%X")
            print(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  CTRL + sc.C detected, skipping the Internet checker...")
            internetstatus = (f"{cc.yC}Skipped{cc.r}")
            pass
        time=strftime("%X")
        print(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}INFO{sc.W}]  Launching of OPST...")
        sys.stdout.write("\x1b]2;OmegaPSToolkit | A massive penetration testing toolkit.\x07")  # Main title page
        sleep(1)
    except KeyboardInterrupt:
        abort()
    except EOFError:
        abort()
    except ModuleNotFoundError:
        exit(criticalmsg)
    except ImportError:
        exit(criticalmsg)
    except NameError:
        exit(criticalmsg)
#-END-OF-MODULES-CHECKER---------------------------------------------#

#-Main-tool----------------------------------------------------------#
try:
### Wireless Atack | main page
    def wireless_mainpage():
        clear()
        print(f"{cc.gC}         ________ __              __                         __                __        {cc.r}")
        print(f"{cc.gC}        |  |  |  |__|.----.-----.|  |.-----.-----.-----.    |  |_.-----.-----.|  |.-----.{cc.r}")
        print(f"{cc.gC}        |  |  |  |  ||   _|  -__||  ||  -__|__ --|__ --|    |   _|  _  |  _  ||  ||__ --|{cc.r}")
        print(f"{cc.gC}        |________|__||__| |_____||__||_____|_____|_____|    |____|_____|_____||__||_____|{cc.r}")
        print(f"{cc.bC}     ╓────────────────────────────────────────────────────────────────────────────────{cc.gC}►{cc.r}")


        ##          coming soon

#---Information Gathering--------------------------------------------#

### Information Gathering | main page ###
    def informationgathering_mainpage():
        clear() 
        print(f"""
{cc.rC2}      _______         ___                             __   __                    {cc.r}
{cc.rC2}     |_     _|.-----.'  _|.-----.----.--------.---.-.|  |_|__|.-----.-----.      {cc.r}
{cc.rC2}      _|   |_ |     |   _||  _  |   _|        |  _  ||   _|  ||  _  |     |      {cc.r}
{cc.rC2}     |_______||__|__|__|  |_____|__| |__|__|__|___._||____|__||_____|__|__|      {cc.r}
{cc.bC}   ◄═════════════════════════════════════════════════════════════════════════►    {cc.r}
{cc.rC2}          _______         __   __                __ {cc.r}
{cc.rC2}         |     __|.---.-.|  |_|  |--.-----.----.|__|.-----.-----.                {cc.r}
{cc.rC2}         |    |  ||  _  ||   _|     |  -__|   _||  ||     |  _  |                {cc.r}
{cc.rC2}         |_______||___._||____|__|__|_____|__|  |__||__|__|___  |                {cc.r}
{cc.bC}   ╔══════════════════════════════════════════════════════{cc.rC2}|_____|{cc.bC}══►{cc.r}
{cc.bC}   ╚═════╗{cc.r}
{cc.bC}         ║{cc.r}   In this category you will find tools to collect information,
{cc.bC}         ║{cc.r}              such as port scan, SQL injections etc
{cc.bC}         ║{cc.r}
{cc.bC}         ╟──── [{cc.gC}  Made by   {cc.bC}] ───{cc.gC}► {cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
{cc.bC}         ╟──── [{cc.gC}  Codename  {cc.bC}] ───{cc.gC}► {cc.bC2}@{cc.r}{cc.rC}MyMeepSQL")
{cc.bC}         ╟──── [{cc.gC}  Version   {cc.bC}] ───{cc.gC}► {cc.bC2}v{cc.rC}0.0.1{cc.r})
{cc.bC}         ║{cc.r}
{cc.bC}         ╟────{cc.gC}► {cc.r}[{cc.bC}1{cc.r}]{cc.gC}    Scan{cc.r}
{cc.bC}         ╟────{cc.gC}► {cc.r}[{cc.bC}o{cc.r}]{cc.gC}    Return to the{cc.rC} OmegaPSToolkit{cc.gC} main page{cc.r}
{cc.bC}         ╙────{cc.gC}► {cc.r}[{cc.bC}exit{cc.r}]{cc.gC} Exit the opstconsole\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/Information_Gathering{cc.bC}]{cc.r}""")
        global commands
        command = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if command == "1":
            informationgathering_scan_mainpage()
        elif command == "x":
            clear()
            main_page()
        elif not command:
            option_error()
            clear()
            informationgathering_mainpage()
        else:
            invalid_option(command)
            clear()
            informationgathering_mainpage()

### Information Gathering | Scan tools ### 
    def informationgathering_scan_mainpage():
        clear()
        print(f"{cc.gC}       _____             _____         _               {cc.r}")
        print(f"{cc.gC}      |   __|___ ___ ___|_   _|___ ___| |___           {cc.r}")
        print(f"{cc.gC}      |__   |  _| .'|   | | | | . | . | |_ -|          {cc.r}")
        print(f"{cc.gC}      |_____|___|__,|_|_| |_| |___|___|_|___|          {cc.r}")
        print(f"{cc.gC}     ╓────────────────────────────────────────{cc.gC}►{cc.r}")
        print(f"{cc.gC}     ╙────╖")
        print(f"{cc.gC}          ║{cc.r}   Some tools for scanning target")
        print(f"{cc.gC}          ║{cc.r}")
        print(f"{cc.gC}          ╟──────{cc.gC}►{cc.r}{cc.bC2} Created by :: {cc.r}{cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}")
        print(f"{cc.gC}          ╟──────{cc.gC}►{cc.r}{cc.bC2} Codename   :: @{cc.r}{cc.rC}MyMeepSQL{cc.r}")
        print(f"{cc.gC}          ╟──────{cc.gC}►{cc.r}{cc.bC2} Version    :: v{cc.r}{cc.rC}0.0.1{cc.r}")
        print(f"{cc.gC}          ║{cc.r}")
        print(f"{cc.gC}          ╙─────╖{cc.r}")
        print(f"{cc.gC}                ╟────{cc.gC}► {cc.r}[{cc.bC}1{cc.r}]{cc.gC}    Nmap{cc.r}")
        print(f"{cc.gC}                ╟────{cc.gC}► {cc.r}[{cc.bC}2{cc.r}]{cc.gC}    SQLMap{cc.r}")
        print(f"{cc.gC}                ╟────{cc.gC}► {cc.r}[{cc.bC}x{cc.r}]{cc.gC}    Return to the{cc.rC} Information Gathering{cc.gC} main page{cc.r}")
        print(f"{cc.gC}                ╟────{cc.gC}► {cc.r}[{cc.bC}o{cc.r}]{cc.gC}    Return to the{cc.rC} OmegaPSToolkit{cc.gC} main page{cc.r}")
        print(f"{cc.gC}                ╙────{cc.gC}► {cc.r}[{cc.bC}exit{cc.r}]{cc.gC} Exit the opstconsole\n{cc.r}")
        print(f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/Information_Gathering/ScanTools{cc.bC}]{cc.r}")
        global command
        command = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if command == "2":
            informationgathering_scan_sqlmap()

        # if scan_mainpage_ == 2:
            # informationgathering_sqlmap()

        elif command == "x":
            clear()
            informationgathering_scan_mainpage()
        elif command == "o":
            clear()
            main_page()
        elif command == "exit":
            exit_odst()
        elif not command:
            option_error()
            clear()
            informationgathering_scan_mainpage()
        else:
            invalid_option(command)
            clear()
            informationgathering_scan_mainpage()

    def informationgathering_scan_sqlmap():
        while True:
            prompt_for_command = f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/Information_Gathering/ScanTools/sqlmap{cc.bC}]{cc.r}"
            user_input = input(prompt_for_command + f"\n{cc.bC}└╼{cc.rC}$ {cc.r}")
            command = user_input
            if not command:
                print()
                user_input
            # elif "connexionstatus" == command:
            #     print(f"{sc.B}[-]{sc.GR}    Checking for Internet internet_check...{sc.W}")
            #     sleep(1)
            #     if internet_check() == True:
            #         internetstatus = f"{sc.G}Connected{sc.W}"
            #         print(f"{sc.G}[+]{sc.GR}    Internet status : {sc.G}Connected{sc.W}.")
            #     else:
            #         internetstatus = f"{sc.R}Not connected{sc.W}"
            #         print(f"{sc.R}[!]{sc.GR}    Internet status : {sc.R}Not connected{sc.W}.")
            #     print()
            
            elif command:
                os.system(command)
            elif "clear" == command:
                clear()
                informationgathering_scan_sqlmap()
            elif "info" == command:
                cli_infomsg()
            elif "leave" == command:
                print(f"{sc.G}[-]{sc.W}   Exiting CLI mode...")
                sleep(0.5)
                informationgathering_scan_mainpage()
            elif "exit" == command:
                exit_odst()
            else:
                unknown_command = f"{sc.R}\n[!]{sc.W}   '{command}' is not recognized as an internal or external command.\n"
                print(unknown_command)
#---End of Information Gathering-------------------------------------#

#---Usefull tool-----------------------------------------------------#
### Usefull Windows tool | main page ###
    def usefulltools_mainpage():
        clear()
        print(f"""
{cc.rC2}       _____ _____         _     {cc.r}
{cc.rC2}      |  |  |_   _|___ ___| |___ {cc.r}
{cc.rC2}      |  |  | | | | . | . | |_ -|{cc.r}
{cc.rC2}      |_____| |_| |___|___|_|___|{cc.r}
   {cc.bC}╔═════════════════════════════{cc.gC}►{cc.r}
   {cc.bC}╚════╗
        {cc.bC}║{cc.r}   UsefulTools include several useful
        {cc.bC}║{cc.r}        tools like Windows tools
        {cc.bC}║
        {cc.bC}╟──── [{cc.gC}  Made by   {cc.bC}] ───{cc.gC}►{cc.rC} Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
        {cc.bC}╟──── [{cc.gC}  Codename  {cc.bC}] ───{cc.gC}►{cc.bC2} @{cc.rC}MyMeepSQL{cc.r}
        {cc.bC}╟──── [{cc.gC}  Version   {cc.bC}] ───{cc.gC}►{cc.bC2} v{cc.rC}0.1.0{cc.r}
        {cc.bC}║
        {cc.bC}╟────{cc.gC}► {cc.r}[{cc.bC}1{cc.r}]{cc.gC}     Backup tool{cc.r}
        {cc.bC}╟────{cc.gC}► {cc.r}[{cc.bC}2{cc.r}]{cc.gC}     Network commands{cc.r}
        {cc.bC}╟────{cc.gC}► {cc.r}[{cc.bC}o{cc.r}]{cc.gC}     Return to the{cc.rC} OmegaPSToolkit{cc.gC} main page{cc.r}
        {cc.bC}╙────{cc.gC}► {cc.r}[{cc.bC}exit{cc.r}]{cc.gC}  Exit the opstconsole\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools{cc.bC}]{cc.r}""")
        global command
        command = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if command == "1":
            usefulltools_backup_main()
        if command == "2":
            usefulltools_networkC_main_page()
        elif command == "o":
            main_page()
        elif not command:
            option_error()
            clear()
            usefulltools_mainpage()
        elif command == "exit":
            exit_odst()
        else:
            invalid_option(command)
            clear()
            usefulltools_mainpage()

### Usefull Windows tool  | Network commands ###
    def usefulltools_networkC_main_page():
        while internet_check == False:
            internet_check()
        clear()
        print(f"""
{cc.rC2}        _______         __                        __     ______                                         __        {cc.r}
{cc.rC2}       |    |  |.-----.|  |_.--.--.--.-----.----.|  |--.|      |.-----.--------.--------.---.-.-----.--|  |.-----.{cc.r}
{cc.rC2}       |       ||  -__||   _|  |  |  |  _  |   _||    < |   ---||  _  |        |        |  _  |     |  _  ||__ --|{cc.r}
{cc.rC2}       |__|____||_____||____|________|_____|__|  |__|__||______||_____|__|__|__|__|__|__|___._|__|__|_____||_____|{cc.r}
{cc.bC}   ╓───────────────────────────────────────────────────────────────────────────────────────────────────────────────{cc.gC}►{cc.r}
{cc.bC}   ╚════╗{cc.r}
{cc.bC}        ║{cc.r}    Some network commands{cc.r}
{cc.bC}        ║{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Created by       :: {cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Codename         :: @{cc.rC}MyMeepSQL{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Version          :: v{cc.rC}0.1.9{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Internet Status  :: {cc.rC}{internetstatus}{cc.r}
{cc.bC}        ║{cc.r}
{cc.bC}        ╚══════╗{cc.r}
{cc.bC}               ╟────{cc.gC}► {cc.r}[{cc.bC}1{cc.r}]{cc.gC}     Ping
{cc.bC}               ╟────{cc.gC}► {cc.r}[{cc.bC}2{cc.r}]{cc.gC}     NSLookup
{cc.bC}               ╟────{cc.gC}► {cc.r}[{cc.bC}3{cc.r}]{cc.gC}     Traceroute
{cc.bC}               ╟────{cc.gC}► {cc.r}[{cc.bC}4{cc.r}]{cc.gC}     Netstat
{cc.bC}               ╟────{cc.gC}► {cc.r}[{cc.bC}5{cc.r}]{cc.gC}     Whois
{cc.bC}               ╟────{cc.gC}► {cc.r}[{cc.bC}x{cc.r}]{cc.gC}     Return to the{cc.rC} UTools{cc.gC} main page{cc.r}
{cc.bC}               ╟────{cc.gC}► {cc.r}[{cc.bC}o{cc.r}]{cc.gC}     Return to the{cc.rC} OmegaPSToolkit{cc.gC} main page{cc.r}
{cc.bC}               ╙────{cc.gC}► {cc.r}[{cc.bC}exit{cc.r}]{cc.gC}  Exit the opstconsole\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/NetworkCommands{cc.bC}]{cc.r}""")
        global command
        command = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if command == "1":
            usefulltools_networkC_ping()
        elif command == "2":
            usefulltools_networkC_nslookup()
        elif command == "3":
            usefulltools_networkC_traceroute()
        elif command == "4":
            usefulltools_networkC_netstat()
        elif command == "5":
            usefulltools_networkC_whois()
        elif command == "x":
            usefulltools_mainpage()
        elif command == "o":
            main_page()
        elif command == "exit":
            exit_odst()
        elif not command:
            option_error()
            clear()
            usefulltools_networkC_main_page()
        else:
            invalid_option(command)
            clear()
            usefulltools_networkC_main_page()

    def usefulltools_networkC_netstat():
        clear()
        print(f"""
{cc.rC2}       _______         __          __          __   {cc.r}
{cc.rC2}      |    |  |.-----.|  |_.-----.|  |_.---.-.|  |_ {cc.r}
{cc.rC2}      |       ||  -__||   _|__ --||   _|  _  ||   _|{cc.r}
{cc.rC2}      |__|____||_____||____|_____||____|___._||____|{cc.r}
{cc.bC}   ╓─────────────────────────────────────────────────{cc.gC}►{cc.r}
{cc.bC}   ╚════╗
{cc.bC}        ║{cc.r}   To show all output one your PC.
{cc.bC}        ║
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Created by       ::  {cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Codename         ::  {cc.bC2}@{cc.rC}MyMeepSQL{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Version          ::  {cc.bC2}v{cc.rC}0.0.1{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Internet Status  ::  {cc.rC}{internetstatus}{cc.r}
{cc.bC}      ╔═╝{cc.r}
{cc.bC}      ╚════════════════════════════════════════════╗{cc.r}
        Type 'netstat --help for the help message  {cc.bC}║{cc.r}
         (type 'exit' for exit the Netstat tool)   {cc.bC}║{cc.r}
{cc.bC}      ═════════════════════════════════════════════╝\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/NetworkCommands/Netstat{cc.bC}]{cc.r}""")
        netstatcommand = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))
        if netstatcommand == "exit":
            usefulltools_networkC_main_page()
        elif netstatcommand:
            try:
                netstat = os.system(f"{netstatcommand}")
                print(netstat)
                input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to remake a netstat{cc.bC}]{cc.r}")
                usefulltools_networkC_netstat()
            except KeyboardInterrupt:
                print()
                print(f"{cc.bC}[{cc.rC2}*{cc.bC}]{cc.bC}─[{cc.gC}CTRL + sc.C detected stop the netstat...{cc.bC}]{cc.r}")
                input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to remake a netstat{cc.bC}]{cc.r}")
                usefulltools_networkC_netstat()
        else:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}No netstat command found{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_networkC_netstat()

    def usefulltools_networkC_whois():
        clear()
        print(f"""
{cc.rC2}       ________ __           __        {cc.r}
{cc.rC2}      |  |  |  |  |--.-----.|__|.-----.{cc.r}
{cc.rC2}      |  |  |  |     |  _  ||  ||__ --|{cc.r}
{cc.rC2}      |________|__|__|_____||__||_____|{cc.r}
{cc.bC}   ╓────────────────────────────────────{cc.gC}►{cc.r}
{cc.bC}   ╚════╗
{cc.bC}        ║{cc.r}   Find out how many routers a packet passes
{cc.bC}        ║{cc.r}        through before its destination.
{cc.bC}        ║
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Created by       ::  {cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Codename         ::  {cc.bC2}@{cc.rC}MyMeepSQL{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Version          ::  {cc.bC2}v{cc.rC}0.0.1{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Internet Status  ::  {cc.rC}{internetstatus}{cc.r}
{cc.bC}      ╔═╝{cc.r}
{cc.bC}      ╚═════════════════════════════════════════════════════════════════════════════════════════╗{cc.r}
        Write an domain for see informations about it, type 'whois --help for the help message  {cc.bC}║{cc.r}
                              (type 'exit' for exit the Traceroute tool)                        {cc.bC}║{cc.r}
{cc.bC}      ══════════════════════════════════════════════════════════════════════════════════════════╝\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/NetworkCommands/Traceroute{cc.bC}]{cc.r}""")
        whoiscommand = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if whoiscommand == "exit":
            usefulltools_networkC_main_page()
        elif whoiscommand:
            if internet_check() == True:
                try:
                    whois = os.system(f"{whoiscommand}")
                    print(whois)
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to write an another IP/domain for get informations about it{cc.bC}]{cc.r}")
                    usefulltools_networkC_whois()
                except KeyboardInterrupt:
                    print()
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to write an another IP/domain for whois{cc.bC}]{cc.r}")
                    usefulltools_networkC_whois()
                else:
                    print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Can’t get informations, check your Inthernet internet_check and try again{cc.bC}]{cc.r}")
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
                    usefulltools_networkC_whois()
        else:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}No IP/domain found, write an IP/domain to whois it{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_networkC_whois()

    def usefulltools_networkC_traceroute():
        clear()
        print(f"""
{cc.rC2}       _______                                          __         {cc.r}
{cc.rC2}      |_     _|.----.---.-.----.-----.----.-----.--.--.|  |_.-----.{cc.r}
{cc.rC2}        |   |  |   _|  _  |  __|  -__|   _|  _  |  |  ||   _|  -__|{cc.r}
{cc.rC2}        |___|  |__| |___._|____|_____|__| |_____|_____||____|_____|{cc.r}
{cc.bC}   ╓────────────────────────────────────────────────────────────────{cc.gC}►{cc.r}
{cc.bC}   ╚════╗
{cc.bC}        ║{cc.r}   Find out how many routers a packet passes
{cc.bC}        ║{cc.r}        through before its destination.
{cc.bC}        ║
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Created by       ::  {cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Codename         ::  {cc.bC2}@{cc.rC}MyMeepSQL{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Version          ::  {cc.bC2}v{cc.rC}0.0.7{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Internet Status  ::  {cc.rC}{internetstatus}{cc.r}
{cc.bC}      ╔═╝{cc.r}
{cc.bC}      ╚═════════════════════════════════════════════════════════════════════════════════════╗{cc.r}
        Write an IP to ping it and track it, type 'traceroute --help' for the help message  {cc.bC}║{cc.r}
                            (type 'exit' for exit the Traceroute tool)                      {cc.bC}║{cc.r}
{cc.bC}      ══════════════════════════════════════════════════════════════════════════════════════╝\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/NetworkCommands/Traceroute{cc.bC}]{cc.r}""")
        traceroutecommand = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if traceroutecommand == "exit":
            usefulltools_networkC_main_page()
        elif traceroutecommand:
            if internet_check() == True:
                try:
                    traceroute = os.system(f"{traceroutecommand}")
                    print(traceroute)
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to write an another IP for traceroute it{cc.bC}]{cc.r}")
                    usefulltools_networkC_traceroute()
                except KeyboardInterrupt:
                    print()
                    print(f"{cc.bC}[{cc.rC2}*{cc.bC}]{cc.bC}─[{cc.gC}CTRL + sc.C detected stop the traceroute...{cc.bC}]{cc.r}")
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to write an another IP for traceroute{cc.bC}]{cc.r}")
                    usefulltools_networkC_traceroute()
                except RuntimeError:
                    print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}'{traceroutecommand}' not found, prlease ckeck the IP before trace it{cc.bC}]{cc.r}")
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
                    usefulltools_networkC_traceroute()
                else:
                    print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Can’t reach the destination, check your Internet Inthernet and try again{cc.bC}]{cc.r}")
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
                    usefulltools_networkC_traceroute()
        else:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}No IP/domain found, write an IP/domain to traceroute it{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_networkC_traceroute()

    def usefulltools_networkC_nslookup():
        clear()
        print(f"""
{cc.rC2}       _______ _______ _____                __{cc.r}
{cc.rC2}      |    |  |     __|     |_.-----.-----.|  |--.--.--.-----.{cc.r}
{cc.rC2}      |       |__     |       |  _  |  _  ||    <|  |  |  _  |{cc.r}
{cc.rC2}      |__|____|_______|_______|_____|_____||__|__|_____|   __|{cc.r}
{cc.bC}   ╓───────────────────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚════╗{cc.r}
{cc.bC}        ║{cc.r}    Some windows network commands
{cc.bC}        ║{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Created by       :: {cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Codename         :: @{cc.rC}MyMeepSQL{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Version          :: v{cc.rC}0.0.8{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Internet Status  :: {cc.rC}{internetstatus}{cc.r}
{cc.bC}      ╔═╝{cc.r}
{cc.bC}      ╚═══════════════════════════════════════════╗{cc.r}
         Write a domain for look the IP he used   {cc.bC}║{cc.r}
        (type 'exit' for exit the NSLookup tool)  {cc.bC}║{cc.r}
{cc.bC}      ════════════════════════════════════════════╝\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/NetworkCommands/NSLookup{cc.bC}]{cc.r}""")
        ip_domain = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))
        if ip_domain == "exit":
            usefulltools_networkC_main_page()
        elif ip_domain:
            if internet_check() == True:
                print(f"""
{cc.bC}╔══════════════════════╗
{cc.bC}║{cc.r}   NSLookup respond{cc.bC}   ║
{cc.bC}╚══════════════════════╝{cc.r}
""")
                nslookup = os.system(f"nslookup {ip_domain}")
                print(nslookup)
                print()
                input(f"{cc.bC}[{cc.rC2}-{cc.bC}]─[{cc.gC}Press [ENTER] key to write an another domain for nslookup{cc.bC}]{cc.r}")
                usefulltools_networkC_nslookup()
            else:
                print(f"{cc.bC}[{cc.rC2}!{cc.bC}]─[{cc.gC}Can’t reach the destination, check your Internet Inthernet and try again{cc.bC}]{cc.r}")
                input(f"{cc.bC}[{cc.rC2}-{cc.bC}]─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
                usefulltools_networkC_nslookup()
        else:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]─[{cc.gC}No domain found, write an domain for lookup it{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_networkC_nslookup()

    def usefulltools_networkC_ping():
        clear()
        print(f"""
{cc.rC2}      ______ __               {cc.r}
{cc.rC2}     |   __ \__|.-----.-----. {cc.r}
{cc.rC2}     |    __/  ||     |  _  | {cc.r}
{cc.rC2}     |___|  |__||__|__|___  | {cc.r}
{cc.bC}   ╓──────────────────{cc.rC2}|_____|{cc.bC}──{cc.gC}►{cc.r}
{cc.bC}   ╚════╗{cc.r}
{cc.bC}        ║{cc.r}    Ping IP/domain to test if it responds (if it is connected)
{cc.bC}        ║{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Created by       :: {cc.rC}Thomas Pellissier {cc.bC2}(from © PSociety™){cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Codename         :: @{cc.rC}MyMeepSQL{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Version          :: v{cc.rC}0.0.9{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.bC2} Internet Status  :: {cc.rC}{internetstatus}{cc.r}
{cc.bC}      ╔═╝{cc.r}
{cc.bC}      ╚═════════════════════════════════════════════════════════════╗{cc.r}
        Write an IP to ping it, type 'ping -help' for help message  {cc.bC}║{cc.r}
                   (type 'exit' for exit the Ping tool)             {cc.bC}║{cc.r}
{cc.bC}      ══════════════════════════════════════════════════════════════╝\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/NetworkCommands/Ping{cc.bC}]{cc.r}""")
        pingcommand = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if pingcommand == "exit":
            usefulltools_networkC_main_page()
        elif pingcommand:
            if internet_check() == True:
                try:
                    ping = os.system(f"{pingcommand}")
                    print(ping)
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to write an another IP for pinging{cc.bC}]{cc.r}")
                    usefulltools_networkC_ping()
                except KeyboardInterrupt:
                    print()
                    print(f"{cc.bC}[{cc.rC2}*{cc.bC}]{cc.bC}─[{cc.gC}CTRL + C detected stop the ping...{cc.bC}]{cc.r}")
                    input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to write an another IP for pinging{cc.bC}]{cc.r}")
                    usefulltools_networkC_ping()
            else:
                print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Can’t reach the destination, check your Internet Inthernet and try again{cc.bC}]{cc.r}")
                input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
                usefulltools_networkC_ping()
        else:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}No IP found, write an IP to ping it{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_networkC_ping()

### Usefull Windows tool  | Backup tool ###
    def usefulltools_backup_main():
        clear()
        print(f"""
{cc.rC2}      _______                              ______              __                 {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----. {cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  | {cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __| {cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚════════╗{cc.r}
{cc.bC}            ║{cc.r}    A tool for make backup quickly{cc.r}
{cc.bC}            ║{cc.r}
{cc.bC}            ╟──────{cc.gC}►{cc.bC2} Created by :: {cc.rC}Thomas Pellissier{cc.bC2} (from © PSociety™){cc.r}
{cc.bC}            ╟──────{cc.gC}►{cc.bC2} Codename   :: @{cc.rC}MyMeepSQL{cc.r}
{cc.bC}            ╟──────{cc.gC}►{cc.bC2} Version    :: v{cc.rC}0.1.4{cc.r}
{cc.bC}    ╔═══════╝{cc.r}
{cc.bC}    ╚════════════════════════════════╗{cc.r}
      Do you want make backup [Y/n]  {cc.bC}║{cc.r}
{cc.bC}    ═════════════════════════════════╝\n{cc.r}
{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/menu{cc.bC}]{cc.r}""")
        choice = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if choice == "y" or choice == "Y":
            usefulltools_backup_source()
        elif choice == "n":
            usefulltools_mainpage()
        elif not choice:
            y_or_n_error()
            usefulltools_backup_main()
        else:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Invalid option, chose [Y/n]{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_backup_main()

    def usefulltools_backup_source():
        clear()
        print(f"""
{cc.rC2}      _______                              ______              __                  {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  {cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  {cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  {cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚════════════════════════════════════════════╗{cc.r}
     Whish folder or file you want backup it ?  {cc.bC}║{cc.r}
           {cc.rC}/!\{cc.r} Type the source path {cc.rC}/!\         {cc.bC}║{cc.r}
{cc.bC}   ═════════════════════════════════════════════╝{cc.r}

{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/source{cc.bC}]{cc.r}""")
        global omegabackup_source
        omegabackup_source = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if not omegabackup_source:
            print(f"{cc.bC}[{cc.r}{cc.rC2}!{cc.r}{cc.bC}]{cc.r}{cc.bC}─[{cc.r}{cc.gC}Type your source path{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.r}{cc.rC2}-{cc.r}{cc.bC}]{cc.r}{cc.bC}─[{cc.r}{cc.gC}Press [ENTER] key to continue{cc.bC}]{cc.r}")
            usefulltools_backup_source()
        else:
            usefulltools_backup_destination()

    def usefulltools_backup_destination():
        clear()
        print(f"""
{cc.rC2}      _______                              ______              __                  {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  {cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  {cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  {cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚════════════════════════════════════╗{cc.r}
       Where you want to backup it ?    {cc.bC}║{cc.r}
     {cc.rC}/!\{cc.r} Type the destination path {cc.rC}/!\  {cc.bC}║{cc.r}
{cc.bC}   ═════════════════════════════════════╝{cc.r}

{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/destination{cc.bC}]""")
        global oemgabackup_destination
        oemgabackup_destination = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))
            
        if not oemgabackup_destination:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Type your destination path{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_backup_destination()
        else:
            usefulltools_backup_verification()

    def usefulltools_backup_verification():
        clear()
        print(f"""
{cc.rC2}      _______                              ______              __                  {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.  {cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |  {cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|  {cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚═════════════════════════════════════╗{cc.r}
     Are you sure you want backup [Y/n]  {cc.bC}║{cc.r}
{cc.bC}   ╔═════════════════════════════════════╝{cc.r}
{cc.bC}   ╚════╗{cc.r}
{cc.bC}        ╟──────{cc.gC}►{cc.rC} Source{cc.bC} ───────{cc.gC}► {cc.rC}"{cc.r}{omegabackup_source}{cc.rC}"{cc.r}
{cc.bC}        ╚──────{cc.gC}►{cc.rC} Destination{cc.bC} ──{cc.gC}► {cc.rC}"{cc.r}{oemgabackup_destination}{cc.rC}"{cc.r}

{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/verification{cc.bC}]{cc.r}""")
        sure = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

        if not sure:
            print(f"{cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Chose [Y/n]{cc.bC}]{cc.r}")
            input(f"{cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_backup_verification()

        elif sure == "y" or sure == "Y":
            clear()
            print(f"""
{cc.rC2}      _______                              ______              __                {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚═══════════╗{cc.r}
     Backuping...  {cc.bC}║
{cc.bC}   ════════════╝{cc.r}""")
            try:
                from datetime import datetime
                from pathlib import Path
                import zipfile
                OBJECT_TO_BACKUP = f'{omegabackup_source}'          # The file or directory to backup
                BACKUP_DIRECTORY = f'{oemgabackup_destination}'     # The location to store the backups in
                MAX_BACKUP_AMOUNT = 20                              # The maximum amount of backups to have in BACKUP_DIRECTORY

                object_to_backup_path = Path(OBJECT_TO_BACKUP)
                backup_directory_path = Path(BACKUP_DIRECTORY)
                assert object_to_backup_path.exists()               # Validate the object we are about to backup exists before we continue

                # Validate the backup directory exists and create if required
                backup_directory_path.mkdir(parents=True, exist_ok=True)

                # Get the amount of past backup zips in the backup directory already
                existing_backups = [
                    x for x in backup_directory_path.iterdir()
                    if x.is_file() and x.suffix == '.zip' and x.name.startswith('backup-')
                ]

                # Enforce max backups and delete oldest if there will be too many after the new backup
                oldest_to_newest_backup_by_name = list(sorted(existing_backups, key=lambda f: f.name))
                while len(oldest_to_newest_backup_by_name) >= MAX_BACKUP_AMOUNT:  # >= because we will have another soon
                    backup_to_delete = oldest_to_newest_backup_by_name.pop(0)
                    backup_to_delete.unlink()

                # Create zip file (for both file and folder options)
                backup_file_name = f'BACKUP-{datetime.now().strftime("%Y-%m-%W %Hh%M %Ss")} - {object_to_backup_path.name}.zip'
                zip_file = zipfile.ZipFile(str(backup_directory_path / backup_file_name), mode='w')
                if object_to_backup_path.is_file():
                    # If the object to write is a file, write the file
                    zip_file.write(
                        object_to_backup_path.absolute(),
                        arcname=object_to_backup_path.name,
                        compress_type=zipfile.ZIP_DEFLATED
                    )
                elif object_to_backup_path.is_dir():
                    # If the object to write is a directory, write all the files
                    for file in object_to_backup_path.glob('**/*'):
                        if file.is_file():
                            zip_file.write(
                                file.absolute(),
                                arcname=str(file.relative_to(object_to_backup_path)),
                                compress_type=zipfile.ZIP_DEFLATED
                            )
                # Close the created zip file
                zip_file.close()

                clear()
                print(f"""
{cc.rC2}      _______                              ______              __                {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚════════════════════════════╗{cc.r}
     Backup end successfully !{cc.bC}  ║{cc.r}
{cc.bC}   ═════════════════════════════╝{cc.r}""")
                sleep(2)
                usefulltools_backup_remakebackup()
            except KeyboardInterrupt:
                print(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.R}[*]{sc.W}CTRL + C detected stop the ping.")
                print(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.R}[!]{sc.W}Backup interrupted.")
                print(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.G}[-]{sc.W}Deleting current backup...")
                os.system(f"rm -fr ")
            except PermissionError:
                print(f"{cc.bC}     ║ [{cc.rC2}!{cc.bC}]─[{cc.gC}Permission denied.{cc.bC}]{cc.r}")
                print(f"{cc.bC}     ║ [{cc.rC2}!{cc.bC}]─[{cc.gC}Please check your permissions with your folder/users.{cc.bC}]{cc.r}")
                print(f"{cc.bC}     ║ [{cc.rC2}-{cc.bC}]─[{cc.gC}Do you want to remake the backup config ? [Y/n]{cc.bC}]{cc.r}")
                print(f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/permission_denied{cc.bC}]{cc.r}")
                permerror = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))

                while not permerror:
                    print(f"{cc.bC}[{cc.rC2}!{cc.bC}]─[{cc.gC}Chose [Y/n]{cc.bC}]{cc.r}")
                    print(f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/permission_denied{cc.bC}]{cc.r}")
                    permerror = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))
                if permerror == "y" or permerror == "Y":
                    usefulltools_backup_source()
                if permerror == "n" or permerror == "N":
                    usefulltools_mainpage()
            except:
                print(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.R}[!]{sc.W}  Error occurred while copying file")
                print(f"""[{sc.C}{sc.D}{time}{sc.W}]  {sc.R}[!]{sc.W}  Check the source/destination path whether they are correct or no,
     [{sc.C}{sc.D}{time}{sc.W}]     check that the files are not corrupted or some other problem and redo the backup configuration""")
                input(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.G}[-]{sc.W}  Press [ENTER] key to remake the backup configuration")
                usefulltools_backup_source()
        elif sure == "n" or sure =="N":
            usefulltools_backup_reconfig()
        else:
            print(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.R}[!]{sc.W}  Invalid option, chose [Y/n]")
            input(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.G}[-]{sc.W}  Press [ENTER] key to retry")
            usefulltools_backup_verification()

    def usefulltools_backup_reconfig():
        clear()
        print(F"""
{cc.rC2}      _______                              ______              __                {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚═════════════════════════════════════════════════╗{cc.r}
     Do you want reconfig the backup config ? [Y/n]  {cc.bC}║{cc.r}
{cc.bC}   ══════════════════════════════════════════════════╝{cc.r}

{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/Remake_the_backup_config{cc.bC}]{cc.r}""")
        choice = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))
        if choice == "y" or choice == "Y":
            usefulltools_backup_source()
        elif choice == "n" or choice == "N":
            usefulltools_mainpage()
        elif not choice:
            print(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Choose [Y/n]{cc.bC}]{cc.r}")
            input(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_backup_reconfig()
        else:
            print(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Invalid option, choose [Y/n]{cc.bC}]{cc.r}")
            input(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_backup_reconfig()

    def usefulltools_backup_remakebackup():
        clear()
        print(f"""
{cc.rC2}      _______                              ______              __                {cc.r}
{cc.rC2}     |       |.--------.-----.-----.---.-.|   __ \.---.-.----.|  |--.--.--.-----.{cc.r}
{cc.rC2}     |   -   ||        |  -__|  _  |  _  ||   __ <|  _  |  __||    <|  |  |  _  |{cc.r}
{cc.rC2}     |_______||__|__|__|_____|___  |___._||______/|___._|____||__|__|_____|   __|{cc.r}
{cc.bC}   ╓─────────────────────────{cc.rC2}|_____|{cc.bC}──────────────────────────────────────{cc.rC2}|__|{cc.bC}────{cc.gC}►{cc.r}
{cc.bC}   ╚═════════════════════════════════════════╗{cc.r}
     Do you want to remake a backup ? [Y/n]  {cc.bC}║{cc.r}
{cc.bC}   ══════════════════════════════════════════╝{cc.r}

{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/UTools/BackupTool/remake_backup_config{cc.bC}]{cc.r}""")
        choice = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))
        if choice == "y" or choice == "Y":
            usefulltools_backup_source()
        elif choice == "n" or choice == "N":
            usefulltools_mainpage()
        elif not choice:
            print(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Choose [Y/n]{cc.bC}]{cc.r}")
            input(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_backup_reconfig()
        else:
            print(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}!{cc.bC}]{cc.bC}─[{cc.gC}Invalid option, choose [Y/n]{cc.bC}]{cc.r}")
            input(f"[{sc.C}{sc.D}{time}{sc.W}]  {cc.bC}[{cc.rC2}-{cc.bC}]{cc.bC}─[{cc.gC}Press [ENTER] key to retry{cc.bC}]{cc.r}")
            usefulltools_backup_reconfig()
#-End-Usefull Windows tool-------------------------------------------#

#-OmegaPSToolkit-CLI-main-page---------------------------------------#
    def cli_main_page():
        print(f"""
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\        {cc.r}{cc.bC} 
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM \       {cc.r}{cc.gC}      _____                   _____ _____ _____         _ _   _ _{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  \      {cc.r}{cc.gC}     |     |_____ ___ ___ ___|  _  |   __|_   _|___ ___| | |_|_| |_{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM   |     {cc.r}{cc.gC}     |  |  |     | -_| . | .'|   __|__   | | | | . | . | | '_| |  _|{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM   |     {cc.r}{cc.gC}     |_____|_|_|_|___|_  |__,|__|  |_____| |_| |___|___|_|_,_|_|_|   {cc.gC}v{sc.R}{__VERSION_OPSTCONSOLE_CLI} CLI{cc.r}
{cc.bC}{sc.italic}        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM   |     {cc.r}{cc.bC} ╓───────────────────{cc.gC}|___|{cc.bC}─────────────────────────────────────────────────────{cc.gC}►{cc.r}
{cc.bC}{sc.italic}        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM   |     {cc.r}{cc.bC} ║{cc.r}
{cc.bC}{sc.italic}        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM   |     {cc.r}{cc.bC} ║     {cc.r}OmegaPSToolkit factory for penetration testing{cc.r}
{cc.bC}{sc.italic}        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM   |     {cc.r}{cc.bC} ║{cc.r}
{cc.bC}{sc.italic}        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM   |     {cc.r}{cc.bC} ╚════╗{cc.r}
{cc.bC}{sc.italic}        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}Created by{sc.W}{sc.C}       ::{sc.R} Thomas Pellissier{sc.C} (from © PSociety™){cc.r}
{cc.bC}{sc.italic}        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM   |     {cc.r}{cc.bC}      ╟────╥─{cc.gC}► {sc.C}{sc.underscore}Codename{sc.W}{sc.C}         :: {sc.C}@{sc.R}MyMeepSQL or {sc.C}@{sc.GR}th300905{cc.r}
{cc.bC}{sc.italic}        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM   |     {cc.r}{cc.bC}      ║{cc.bC}    ╙─────────────────────{cc.gC}►{sc.C}{sc.R}  The {sc.C}{sc.underscore}seconde{sc.W}{sc.R} codename is also mine{cc.r}
{cc.bC}{sc.italic}        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}OPSTC Version{sc.W}{sc.C}    :: {cc.gC}v{sc.R}{opstconsole_version}{cc.r}
{cc.bC}{sc.italic}        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}Internet Status{sc.W}{sc.C}  ::{sc.R} {internetstatus}{cc.r}
{cc.bC}{sc.italic}        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}Private IP{sc.W}{sc.C}       ::{sc.O} {privateIP}{cc.r}{cc.bC}        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM {cc.bC}  |           ╟──────{cc.gC}► {sc.C}{sc.underscore}Public IP{sc.W}{sc.C}        ::{sc.O} {publicIP}{cc.r}
{cc.bC}{sc.italic}        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}MAC adress{sc.W}{sc.C}       ::{sc.O} {mac_adress}{cc.r}
{cc.bC}{sc.italic}        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o   |     {cc.r}{cc.bC}      ╚════════╗{cc.r}
{cc.bC}{sc.italic}        N               hMMMMMMM`              o   |     {cc.r}{cc.bC}               ║                      {cc.r}Developed for linux{cc.r}
{cc.bC}{sc.italic}        M               yMMMMMMM               s   |     {cc.r}{cc.bC}               ║{cc.r}
{cc.bC}{sc.italic}        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM   |     {cc.r}{cc.bC}               ║{cc.gC}             Welcome to the OmegaPSToolkit (OPST).{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.gC} The toolkit which includes a set of penetration testing tools.{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║         {cc.r}{sc.italic}The OmegaPSToolkit is a product of © PSociety™.{sc.W}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.r}{sc.italic}                 2021-2022, All rights reserved.{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{sc.R}       No responsability is taken by developers in case of{sc.W}
{cc.bC}{sc.italic}        \                                       \  |     {cc.r}{cc.bC}               ╚{sc.R}                 explicit uses of OmegaPSToolkit!{sc.W}
{cc.bC}{sc.italic}         \                                       \ |     {cc.r}
{cc.bC}{sc.italic}          \_______________________________________\|     {cc.r}

{sc.G}[*]{sc.GR}  This is the CLI version of opstonsole, type {sc.B}help{sc.GR} for all commands
{sc.R}[!]{sc.GR}  This CLI version of osptconsoel is {sc.underscore}{sc.R}TOTALLY{sc.W}{sc.GR} in {sc.R}BETA{sc.R}

""")

        while True:
            prompt_for_command = f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/CLI_BETA{cc.bC}]{cc.r}"
            user_input = input(prompt_for_command + f"\n{cc.bC}└╼{cc.rC}$ {cc.r}")
            command = user_input
            if not command:
                print()
                user_input
            # elif "connexionstatus" == command:
            #     print(f"{sc.B}[-]{sc.GR}    Checking for Internet internet_check...{sc.W}")
            #     sleep(1)
            #     if internet_check() == True:
            #         internetstatus = f"{sc.G}Connected{sc.W}"
            #         print(f"{sc.G}[+]{sc.GR}    Internet status : {sc.G}Connected{sc.W}.")
            #     else:
            #         internetstatus = f"{sc.R}Not connected{sc.W}"
            #         print(f"{sc.R}[!]{sc.GR}    Internet status : {sc.R}Not connected{sc.W}.")
            #     print()


            ## Ping
            elif "ping" == command:
                print(f"""
{sc.C}[*]{sc.W}  Type an IP/domain to ping it (type {sc.B}help{sc.W} for the help message (you can also use {sc.B}man ping{sc.W} for all details), type {sc.B}leave{sc.W} for exit ping tool)
""")
                while True:
                    prompt_for_command = f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/CLI_BETA/ping{cc.bC}]{cc.r}"
                    user_input = input(prompt_for_command + f"\n{cc.bC}└╼{cc.rC}$ {cc.r}")
                    command = user_input

                    if not command:
                        print()
                        user_input
                    elif "ping" == command:
                        print(f"{sc.R}\n[!]{sc.W}  You don't need to write {sc.R}ping{sc.W} before option(s). Write directly the option(s) before.\n")
                    elif "help" == command:
                        cli_ping_help()
                    elif "man ping" == command:
                        cli_ping_man_help()
                    elif "clear" == command:
                        clear()
                    elif "leave" == command:
                        print()
                        print(f"{sc.G}[-]{sc.W}  Exiting ping tool...")
                        print()
                        break
                    else:
                        os.system(f"ping {command}")
                        print()


            ## Traeroute
            elif "traceroute" == command:
                print(f"""
{sc.C}[*]{sc.W}  Type an IP/domain to trace to network host (type {sc.B}help{sc.W} for the help message (you can also use {sc.B}man traceroute{sc.W} for all details), type {sc.B}leave{sc.W} for exit traceroute tool)
""")
                while True:
                    prompt_for_command = f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/CLI_BETA/traceroute{cc.bC}]{cc.r}"
                    user_input = input(prompt_for_command + f"\n{cc.bC}└╼{cc.rC}$ {cc.r}")
                    command = user_input

                    if not command:
                        print()
                        user_input
                    elif "traceroute" == command:
                        print(f"{sc.R}\n[!]{sc.W}  You don't need to write {sc.R}traceroute{sc.W} before option(s). Write directly the option(s) before .\n")
                    elif "help" == command:
                        cli_traceroute_help()
                    elif "man traceroute" == command:
                        cli_traceroute_man_help()
                    elif "clear" == command:
                        clear()
                    elif "leave" == command:
                        print()
                        print(f"{sc.G}[-]{sc.W}  Exiting traceroute tool...")
                        print()
                        break
                    else:
                        os.system(f"traceroute {command}")
                        print()


            ## NSLookup
            elif "nslookup" == command:
                print(f"""
{sc.C}[*]{sc.W}  Type an IP/domain to nslookup it (type {sc.B}help{sc.W} for the help message (you can also use {sc.B}man nslookup{sc.W} for all details), type {sc.B}leave{sc.W} for exit nslookup tool)
""")
                while True:
                    prompt_for_command = f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/CLI_BETA/nslookup{cc.bC}]{cc.r}"
                    user_input = input(prompt_for_command + f"\n{cc.bC}└╼{cc.rC}$ {cc.r}")
                    command = user_input

                    if not command:
                        print()
                        user_input
                    elif "nslookup" == command:
                        print(f"""
{sc.R}\n[!]{sc.W}  You don't need to write {sc.R}nslookup{sc.W} before option(s). Write directly the option(s) before.
""")
                    elif "help" == command:
                        cli_nslookup_help()
                    elif "man nslookup" == command:
                        cli_nslookup_man_help()
                    elif "clear" == command:
                        clear()
                    elif "leave" == command:
                        print()
                        print(f"{sc.G}[-]{sc.W}    Exiting nslookup tool...")
                        print()
                        break
                    else:
                        os.system(f"nslookup {command}")
                        print()

            ## Netstat
            elif "netstat" == command:
                print(f"""
{sc.C}[*]{sc.W}  Type {sc.B}help{sc.W} for the help message (you can also use {sc.B}man nslookup{sc.W} for all details), type {sc.B}leave{sc.W} for exit nslookup tool
""")
                while True:
                    prompt_for_command = f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/CLI_BETA/netstat{cc.bC}]{cc.r}"
                    user_input = input(prompt_for_command + f"\n{cc.bC}└╼{cc.rC}$ {cc.r}")
                    command = user_input

                    if not command:
                        print()
                        user_input
                    elif "netstat" == command:
                        print(f"{sc.R}\n[!]{sc.W}  You don't need to write {sc.R}netstat{sc.W} before option(s). Write directly the option(s) before.\n")
                    elif "help" == command:
                        cli_netstat_help()
                    elif "man netstat" == command:
                        cli_netstat_man_help()
                    elif "clear" == command:
                        clear()
                    elif "leave" == command:
                        print()
                        print(f"{sc.G}[-]{sc.W}      Exiting nslookup tool...")
                        print()
                        break
                    else:
                        os.system(f"netstat {command}")
                        print()
            ## Whois
            elif "whois" == command:
                print(f"""
{sc.C}[*]{sc.W}  Type an IP/domain to get information about it (type {sc.B}help{sc.W} for the help message (you can also use {sc.B}man whois{sc.W} for all details), type {sc.B}leave{sc.W} for exit whois tool)
""")
                while True:
                    prompt_for_command = f"{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~/CLI_BETA/whois{cc.bC}]{cc.r}"
                    user_input = input(prompt_for_command + f"\n{cc.bC}└╼{cc.rC}$ {cc.r}")
                    command = user_input

                    if not command:
                        print()
                        user_input
                    elif "whois" == command:
                        print(f"{sc.R}\n[!]{sc.W}  You don't need to write {sc.R}netstat{sc.W} before option(s). Write directly the option(s) before.\n")
                    elif "help" == command:
                        cli_whois_help()
                    elif "man netstat" == command:
                        cli_whois_man_help()
                    elif "clear" == command:
                        clear()
                    elif "leave" == command:
                        print()
                        print(f"{sc.G}[-]{sc.W}  Exiting whois tool...")
                        print()
                        break
                    else:
                        os.system(f"whois {command}")
                        print()
            elif "clear" == command:
                clear()
            elif "cls" == command:
                print(f"{sc.R}\n[!]{sc.W}  The 'cls' command doesn't active, type 'clear' for clear the terminal.\n")
            elif "reset" == command:
                clear()
                cli_main_page()
            elif "help" == command:
                cli_helpmsg()
            elif "info" == command:
                cli_infomsg()
            elif "fullinfo" == command:
                cli_fullinfomsg()
            elif "leave" == command:
                print(f"{sc.G}[-]{sc.W}  Exiting CLI mode...")
                sleep(0.5)
                main_page()
            elif "exit" == command:
                exit_odst()
            else:
                unknown_command = f"{sc.R}\n[!]{sc.W}  '{command}' is not recognized as an internal command. Type {sc.B}help{sc.W} for all commands.\n"
                print(unknown_command)
    
#-OmegaPSToolkit-main-page-------------------------------------------#
    def main_page():
            clear()
            print(f"""
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\        {cc.r}{cc.bC} 
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM \       {cc.r}{cc.gC}      _____                   _____ _____ _____         _ _   _ _{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  \      {cc.r}{cc.gC}     |     |_____ ___ ___ ___|  _  |   __|_   _|___ ___| | |_|_| |_{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMNmmmmNNMMMMMMMMMMMMMMMM   |     {cc.r}{cc.gC}     |  |  |     | -_| . | .'|   __|__   | | | | . | . | | '_| |  _|{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMdy+:.```..```.-/shNMMMMMMMMMM   |     {cc.r}{cc.gC}     |_____|_|_|_|___|_  |__,|__|  |_____| |_| |___|___|_|_,_|_|_|   {cc.gC}v{sc.R}{__VERSION_OPSTCONSOLE}{cc.r}
{cc.bC}{sc.italic}        MMMMMMMNy/``  -ohmNNNNNdy/`  `:smMMMMMMM   |     {cc.r}{cc.bC} ╓───────────────────{cc.gC}|___|{cc.bC}─────────────────────────────────────────────────────{cc.gC}►{cc.r}
{cc.bC}{sc.italic}        MMMMMNo.    :dNMMMMMMMMMMMNo`   `/dMMMMM   |     {cc.r}{cc.bC} ║{cc.r}
{cc.bC}{sc.italic}        MMMMh.     sMMMMMMMMMMMMMMMMd.    `+NMMM   |     {cc.r}{cc.bC} ║     {cc.r}OmegaPSToolkit factory for penetration testing{cc.r}
{cc.bC}{sc.italic}        MMMy`     sMMMMMMMMMMMMMMMMMMm`     /MMM   |     {cc.r}{cc.bC} ║{cc.r}
{cc.bC}{sc.italic}        MMm`     :MMMMMMMMMMMMMMMMMMMMy      oMM   |     {cc.r}{cc.bC} ╚════╗{cc.r}
{cc.bC}{sc.italic}        MM-      MMMMMMMMMMMMMMMMMMMMMM+      mM   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}Created by{sc.W}{sc.C}       ::{sc.R} Thomas Pellissier{sc.C} (from © PSociety™){cc.r}
{cc.bC}{sc.italic}        MMo      NMMMMMMMMMMMMMMMMMMMMM/     `MM   |     {cc.r}{cc.bC}      ╟────╥─{cc.gC}► {sc.C}{sc.underscore}Codename{sc.W}{sc.C}         :: {sc.C}@{sc.R}MyMeepSQL or {sc.C}@{sc.GR}th300905{cc.r}
{cc.bC}{sc.italic}        MMN`     yMMMMMMMMMMMMMMMMMMMMN`     sMM   |     {cc.r}{cc.bC}      ║{cc.bC}    ╙─────────────────────{cc.gC}►{sc.C}{sc.R}  The {sc.C}{sc.underscore}seconde{sc.W}{sc.R} codename is also mine{cc.r}
{cc.bC}{sc.italic}        MMMh`    .NMMMMMMMMMMMMMMMMMMM+     /MMM   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}OPSTC Version{sc.W}{sc.C}    :: {cc.gC}v{sc.R}{opstconsole_version}{cc.r}
{cc.bC}{sc.italic}        MMMMh.    :NMMMMMMMMMMMMMMMMMs    `oMMMM   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}Internet Status{sc.W}{sc.C}  ::{sc.R} {internetstatus}{cc.r}
{cc.bC}{sc.italic}        NdMMMMMNy/.` -smMMMMMMMMNy/` `:smMMMMMNm   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}Private IP{sc.W}{sc.C}       ::{sc.O} {privateIP}{cc.r}{cc.bC}        MMMMMNo.   -hNMMMMMMMMMMMMMm+   `/dMMMMM {cc.bC}  |           ╟──────{cc.gC}► {sc.C}{sc.underscore}Public IP{sc.W}{sc.C}        ::{sc.O} {publicIP}{cc.r}
{cc.bC}{sc.italic}        m`hNMMMMMMNdy: `MMMMMMMM+ .shmMMMMMMNm:+   |     {cc.r}{cc.bC}      ╟──────{cc.gC}► {sc.C}{sc.underscore}MAC adress{sc.W}{sc.C}       ::{sc.O} {mac_adress}{cc.r}
{cc.bC}{sc.italic}        m  -/+ooooooo+  mMMMMMMM: .ooooooo+/:` o   |     {cc.r}{cc.bC}      ╚════════╗
{cc.bC}{sc.italic}        N               hMMMMMMM`              o   |     {cc.r}{cc.bC}               ║                      {cc.r}Developed for linux{cc.r}
{cc.bC}{sc.italic}        M               yMMMMMMM               s   |     {cc.r}{cc.bC}               ║{cc.r}
{cc.bC}{sc.italic}        MNmmmmmmmmmmmmmmMMMMMMMMmmmmmmmmmmmmmmmM   |     {cc.r}{cc.bC}               ║{cc.gC}             Welcome to the OmegaPSToolkit (OPST).{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.gC} The toolkit which includes a set of penetration testing tools.{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║         {cc.r}{sc.italic}The OmegaPSToolkit is a product of © PSociety™.{sc.W}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.r}{sc.italic}                 2021-2022, All rights reserved.{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{cc.r}
{cc.bC}{sc.italic}        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   |     {cc.r}{cc.bC}               ║{sc.R}       No responsability is taken by developers in case of{sc.W}
{cc.bC}{sc.italic}        \                                       \  |     {cc.r}{cc.bC}               ║{sc.R}                 explicit uses of OmegaPSToolkit!{sc.W}
{cc.bC}{sc.italic}         \                                       \ |     {cc.r}{cc.bC}               ║{cc.r}
{cc.bC}{sc.italic}          \_______________________________________\|     {cc.r}{cc.bC}               ╚                        {sc.GR}{sc.underscore}SELECT AN OPTION{sc.W}
                                                                                                    
                [{sc.C}1{cc.r}]{cc.gC}    Information Gathering tools{cc.r}
                [{sc.C}2{cc.r}]{cc.gC}    Wireless tools{cc.r}
                [{sc.C}3{cc.r}]{cc.gC}    Useful tools (UT){cc.r}
                [{sc.C}cli{cc.r}]{cc.gC}  Use OPST like a Command Line Interpeter {cc.bC}[{sc.R}BETA{cc.bC}]{cc.r}
                [{sc.C}help{cc.r}]{cc.gC} Show the help message{cc.r}
                [{sc.C}exit{cc.r}]{cc.gC} Exit the opstconsole{cc.r}

OPST was not finish and he's totally in development!

{cc.bC}┌──({cc.rC}OmegaPSToolkit{cc.bC})─[{cc.r}~{cc.bC}]{cc.r}""")
            global command
            command = str(input(f"{cc.bC}└╼{cc.rC}$ {cc.r}"))
            time=strftime("%X")
            if command == "1":
                clear()
                informationgathering_mainpage()
            elif command == "2":
                clear()
                wireless_mainpage()
            elif command == "3":
                clear()
                usefulltools_mainpage()
            elif command == "cli":
                print(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.G}[-]{sc.W}  Loading CLI mode...")
                sleep(0.5)
                clear()
                cli_main_page()
            elif command == "help":
                mainpage_helpmsg()
                clear()
                main_page()
            elif command == "exit":
                exit_odst()
            elif not command:
                option_error()
                clear()
                main_page()
            else:
                invalid_option(command)
                clear()
                main_page()
    #-END-OF-MAIN-PAGE---------------------------------------------------#
    # call the main function
    if __name__ == '__main__':
        try:
            main_page()
        except KeyboardInterrupt:
            print()
            exit_odst()
        except EOFError:
            print()
            exit_odst()

except KeyboardInterrupt:
    print()
    exit_odst()
except EOFError:
    print()
    exit_odst()
    
#-END-OF-MAIN-TOOL---------------------------------------------------#



























#      _______________________
#     |    _____     _____    |
#     |   | __ |    | __ |    |
#     |   |____|    |____|    |
#     |                       |
#     |   __           __     |
#     |   \ \         / /     |
#     |    \ \_______/ /      |
#     |     \_________/       |
#     |_______________________|
#             |       |
#             |       |
#  ___________|       |____________
# |                                |
# |                                |
# |                                |
# |                                |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |     |                 |        |
# |_____|                 |________|
#       |                 |
#       |                 |
#       |                 |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       |       |         |
#       | ____  | ______j |
#       |_______|_________| Built by MyMeepSQL | Please don’t change/delete that. This is my signature.
#                           Codename MyMeepSQL by © PSociety™. 2021-2022, all rights reserved.

#                    ______
#                   / ____ |
#                  /</   |<|
#                 /</    |>|
#         _      /</     |<|
#      __||__   /</      \_/
#  ___| OPST |_/</
# |  __________  |
# \_____________/