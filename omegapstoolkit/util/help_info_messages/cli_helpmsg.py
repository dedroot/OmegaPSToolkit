#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_helpomsg.py             [Created: 2022-05-25 | 18:16 PM]  #
#                                         [Update: 2022-05-25 | 18:20 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for CLI                                                 #
#                                                                           #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright © 2022 MyMeepSQL - © PSociety™, 2022 All rights reserved       #
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

def cli_helpmsg():
    print(f"""
{sc.GR}{sc.D} _______ ______ _______ _______ {sc.W}{sc.G}  OmegaPSToolkit CLI {sc.D}v{opstconsole_cli_version}
{sc.GR}{sc.D}|       |   __ \     __|_     _|{sc.G}{sc.D}  Coded by MyMeepSQL for © PSociety™
{sc.GR}{sc.D}|   -   |    __/__     | |   |  {sc.W}{sc.D}  A massive penetration testing toolkit
{sc.GR}{sc.D}|_______|___|  |_______| |___|  {sc.C}{sc.D}  https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}

All commands of the OmegaDSToolkit CLI you can use is the main page

{sc.C}COMMAND{sc.GR}:{sc.W}
    ping        ::  Send ICMP ECHO_REQUEST to network hosts
    nslookup    ::  Query Internet name servers interactively
    netstat     ::  Print network connections, routing tables, interface 
                      statistics, masquerade connections, and multicast memberships
    whois       ::  Client for the whois directory service
    traceroute  ::  Print the route packets trace to network host

{sc.C}{sc.D}OTHER COMMAND{sc.GR}:{sc.W}
    help        ::  Show this help message
    info        ::  Show informations about OSPT and other informations ({sc.R}small version{sc.W})
    fullinfo    ::  Show more informations ({sc.R}largest version{sc.W})
    clear       ::  Clear the terminal
    reset       ::  Reset to come back to the basic menu ({sc.R}CLI{sc.W})
    leave       ::  Exit opstconsole's CLI version ({sc.R}return to opstconsole{sc.W})
    exit        ::  Exit opstconsole
""")