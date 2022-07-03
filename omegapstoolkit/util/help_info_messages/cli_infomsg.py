#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_infomsg.py              [Created: 2022-05-25 | 17:51 PM]  #
#                                         [Update: 2022-05-25 | 17:51 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The information about OPST for cli version                               #
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
from ..versions.python_version import *
from ..os_details import *
from ..distribution_name import *


def cli_infomsg():
    print(f"""
{sc.GR}{sc.D} _______ ______ _______ _______ {sc.W}{sc.G}  OmegaPSToolkit CLI {sc.D}v{opstconsole_cli_version}
{sc.GR}{sc.D}|       |   __ \     __|_     _|{sc.G}{sc.D}  Coded by MyMeepSQL for © PSociety™
{sc.GR}{sc.D}|   -   |    __/__     | |   |  {sc.W}{sc.D}  A massive penetration testing toolkit
{sc.GR}{sc.D}|_______|___|  |_______| |___|  {sc.C}{sc.D}  https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}

{sc.G}[>]{sc.W} Some informations about the OmegaPSToolkit and other
{sc.G}[*]{sc.W} This is the small version, for all informations, run {sc.B}fullinfo{sc.W}

{sc.C}Informations about OmegaPSToolkit{sc.GR}:{sc.W}

    {sc.G}All OPST commands versions{sc.GR}:{sc.W}
        opstconsole             v{opstconsole_version}
        odstconsole CLI         v{opstconsole_cli_version}
        opstupdate              {opstupdate_version}
        opsthelp                v{opsthelp_version}
        odstsetup               {opstsetup_version}
        odstinstall-all         {opstinstallall_version}

    {sc.G}Other informations{sc.GR}:{sc.W}
        GitHub page             {sc.underscore}{sc.C}https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}

{sc.C}Informations about author{sc.GR}:{sc.W}

    {sc.G}General informations{sc.GR}:{sc.W}
        Author                  {sc.italic}Thomas Pellissier{sc.W}
        Codename                {sc.G}@{sc.W}MyMeepSQL{sc.W} or {sc.G}@{sc.W}th300905{sc.W}
        Email                   {sc.P}thomas.pellissier@outlook.com{sc.W} ({sc.R}only for professional{sc.W} or for {sc.G}repport bugs of OmegaPSToolkit{sc.W})
        Owner                   {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}.

{sc.C}Ohter informations{sc.GR}:{sc.W}

    {sc.G}Other versions{sc.GR}:{sc.W}
        Python's version        v{python_version}
        
    {sc.G}System{sc.GR}:{sc.W}
        Operating System        {OS}
        Distribution / Release  {distribution_name}
""")
