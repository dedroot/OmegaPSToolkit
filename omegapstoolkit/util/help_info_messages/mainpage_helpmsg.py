#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ mainpage_helpmsg.py         [Created: 2022-05-25 | 17:20 PM]  #
#                                         [Update: 2022-05-25 | 17:20 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for the OPST main menu                                  #
#                                                                           #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright © 2022 MyMeepSQL - © PSociety™, 2022 All rights reserved     #
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

"""
=====================
Colors informations :
=====================
{R} = Option
{O} = Option's argument 
{G} = Option and argument (not with option, for exemple 'nmap 1.1.1.1', the '1.1.1.1' is a argument with no option)
{B} = Command (for exemple 'clear' or 'leave')
{P} = The eaqual caractere (=)
"""

import sys

from ..system_colors import system_colors as sc
from ..versions.opst_commands_version import *
from ..criticalmsg import time

def mainpage_helpmsg():
    print(f"""
{sc.GR}{sc.D} _______ ______ _______ _______ {sc.W}{sc.G}  OmegaPSToolkit {sc.D}v{opstconsole_version}
{sc.GR}{sc.D}|       |   __ \     __|_     _|{sc.G}{sc.D}  Coded by MyMeepSQL for © PSociety™
{sc.GR}{sc.D}|   -   |    __/__     | |   |  {sc.W}{sc.D}  A massive penetration testing toolkit
{sc.GR}{sc.D}|_______|___|  |_______| |___|  {sc.C}{sc.D}  https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}

All commands of the OmegaDSToolkit you can use is the main page

{sc.B}COMMAND:{sc.W}
    1           ::   Go to the Information Gathering page
    2           ::   Go to the Wireless Tools page
    3           ::   Go to the Usefull tools page
    cli         ::   Use the opstconsole like a CLI
    help        ::   Show this help message
    exit        ::   Exit opstconsole
    """)
    input(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.B}[-]{sc.W}  Press [ENTER] key to continue{sc.W}")