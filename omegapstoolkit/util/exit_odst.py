#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ exit_odst.py              [Created: 2022-05-25 | 17:08 - PM]  #
#                                       [Update:  2022-06-31 | 8:31  - AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The exit OPST ouput function                                             #
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
def exit_odst():

    """
    when the user exit opst with typing "exit" or with CTRL + C
    """

    time=strftime("%X")
    exit_odst = f"\n[{sc.C}{sc.D}{time}{sc.W}]  [{sc.G}EXIT{sc.W}]  Goodby\n"
    exit(exit_odst)