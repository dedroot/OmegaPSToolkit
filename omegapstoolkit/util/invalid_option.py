#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ invalid_option.py         [Created: 2022-05-25 | 19:12 - AM]  #
#                                       [Update:  2022-06-31 | 8:31  - AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The invalid option function                                              #
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

import sys
from time import strftime
from .system_colors import system_colors as sc

def invalid_option(command):

    """
    if the user enter a bad option (if the option type by the user are not recognized)"
    """

    time=strftime("%X")
    print(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.R}ERROR{sc.W}]  '{command}' is not a valid command")
    input(f"[{sc.C}{sc.D}{time}{sc.W}]  [{sc.C}INFO{sc.W}]  Press [ENTER] key to continue")

    # print(f"[{sc.C}{sc.D}{time}{sc.W}]  {sc.R}[!]{sc.W}  