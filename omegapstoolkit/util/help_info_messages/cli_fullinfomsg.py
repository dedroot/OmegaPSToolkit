#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opsthelp.py                 [Update:  2022-05-30 | 1:40  PM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for OmegaPSToolkit                                      #
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

# Import section
import sys
import time
sys.path.insert(0, '/mnt/d/Dev/PSociety/Tools/OmegaPSToolkit (OPST toolkit)/OmegaPSToolkit (OPST toolkit)/functions')
from functions.system_colors import system_colors as sc
from functions.versions.opst_commands_version import *
from functions.versions.python_version import *
from functions.get_private_ip import *
from functions.get_public_ip import *
from functions.get_mac_adress import *
from functions.os_details import *
from functions.distribution_name import *
from functions.ram_info import *
from functions.gpudetails import *
# from opstfunctions import GPU_details_id,GPU_details_id,GPU_details_gpuName,GPU_details_totalMemoy, GPU_details_freeMemory,GPU_details_usedMemory,GPU_details_uuid

####

# The main command
## Font = Chunky from https://www.coolgenerator.com/ascii-text-generator
def cli_fullinfomsg():
    print(f"""
{sc.GR}{sc.D} ______  ______ _______ _______ {sc.W}{sc.G}  OmegaPSToolkit {sc.D}v{opsthelp_version} (opsthelp's version)
{sc.GR}{sc.D}|       |   __ \     __|_     _|{sc.G}{sc.D}  Coded by MyMeepSQL for © PSociety™
{sc.GR}{sc.D}|   -   |    __/__     | |   |  {sc.W}{sc.D}  A massive penetration testing toolkit
{sc.GR}{sc.D}|_______|___|  |_______| |___|  {sc.C}{sc.D}  https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}

{sc.G}[>]{sc.W} All informations about OmegaPSToolkit and other{sc.W}
{sc.G}[*]{sc.W} This is the biggest version, for less informations, run {sc.B}info{sc.W}

{sc.C}Informations about OmegaPSToolkit{sc.GR}:{sc.W}

    {sc.G}Main commands{sc.GR}:{sc.W}
        odstconsole                Start the current tool
        odstupdate                 Update OPST with the latest version from GitHub
        odsthelp                   Print this message and exit

    {sc.G}Other commands (to install OPST the first time){sc.GR}:{sc.W}
        odstsetup                  Install all pip packages that OPST needs
        odstinstall-all            Update you system, copy OPST to {sc.G}"{sc.C}/usr/share/OmegaPSToolkit{sc.G}"{sc.W} and write all comamnds in {sc.G}"{sc.C}/usr/bin/{sc.G}"{sc.W}

    {sc.G}All OPST commands versions{sc.GR}:{sc.W}
        opstconsole                {opstconsole_version}
        odstconsole CLI            {opstconsole_cli_version}
        opstupdate                 {opstupdate_version}
        opsthelp                   {opsthelp_version}
        odstsetup                  {opstsetup_version}
        odstinstall-all            {opstinstallall_version}

    {sc.G}Other informations{sc.GR}:{sc.W}
        GitHub page                {sc.underscore}{sc.C}https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}
        Changelogs                 {sc.underscore}{sc.C}https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md{sc.W}

{sc.C}Informations about author{sc.GR}:{sc.W}

    {sc.G}General informations{sc.GR}:{sc.W}
        Author                     {sc.italic}Thomas Pellissier{sc.W}
        Codename                   {sc.G}@{sc.W}MyMeepSQL{sc.W} or {sc.G}@{sc.W}th300905{sc.W}
        Email                      {sc.P}thomas.pellissier@outlook.com{sc.W} ({sc.R}only for professional{sc.W} or for {sc.G}repport bugs of OmegaPSToolkit{sc.W})
        Owner                      {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}

    {sc.G}Other informations{sc.GR}:{sc.W}
        GitHub profile             {sc.underscore}{sc.C}https://github.com/MyMeepSQL{sc.W}
        Twitter profile            {sc.C}@{sc.W}MyMeepSQL
        Discord profile            $_MyMeepSQL{sc.C}#{sc.G}0141{sc.W}

{sc.C}Ohter informations{sc.GR}:{sc.W}

    {sc.G}Other versions{sc.GR}:{sc.W}
        Python's version           {python_version}

    {sc.G}Network{sc.GR}:{sc.W}
        Private IP                 {sc.O}{privateIP}{sc.W}        Public IP                  {sc.O}{publicIP}{sc.W}
        MAC adress ({sc.C}eth0{sc.W})          {sc.O}{mac_adress}{sc.W}

        {sc.G}Details {sc.W}({sc.C}with all inrefaces{sc.W}){sc.GR}:{sc.W}""")
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"            Interface: {sc.C}{interface_name}{sc.W}")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"""                  IP Address:      {sc.O}{address.address}{sc.W}
                  Netmask:         {sc.O}{address.netmask}{sc.W}
                  Broadcast IP:    {sc.O}{address.broadcast}{sc.W}""")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"""                  MAC Address:     {sc.O}{address.address}{sc.W}
                  Netmask:         {sc.O}{address.netmask}{sc.W}
                  Broadcast MAC:   {sc.O}{address.broadcast}{sc.W}\n""")
    print(f"""
    {sc.G}System{sc.GR}:{sc.W}
        Operating System           {OS}
        Distribution / Release     {distribution_name}
        PC's Name                  {my_system.node}
        Machine                    {my_system.machine}
        Processor                  {my_system.processor}

        {sc.G}RAM details{sc.GR}:{sc.W}
            Total memory           {RAM_total_memory}
            Free memory            {RAM_avalable_memory}
            Used memory            {RAM_used_memory}
            RAM usage              {RAM_usage}""")

    import os 
    os.system("exit")
    print(f"\n        {sc.G}GPU details{sc.GR}:{sc.W}")
    for gpu in gpus:
        try:
            print(f"""            Card {sc.C}{GPU_details_id}{sc.W}:
                  Name             {sc.C}{GPU_details_gpuName}{sc.W}
                  Total memory     {GPU_details_totalMemoy}
                  Free memory      {GPU_details_freeMemory}
                  Loaded memory    {GPU_details_load}
                  Used memory      {GPU_details_usedMemory}
                  Temperature      {GPU_details_temperature}
                  Driver version   {GPU_details_driverVersion}
                  UUID             {GPU_details_uuid}             """)
        except:
            print(f"            Card {sc.C}{GPU_details_id}{sc.W}")
            print(f"                    Cannot get GPU informations")
    print(f"                                                                                            {sc.G}/[{sc.W} Scroll {sc.O}UP{sc.W} for the main informations {sc.G}]\{sc.W}\n")