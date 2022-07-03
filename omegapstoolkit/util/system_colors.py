#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ system_colors.py            [Created: 2022-05-25 | 20:56 AM]  #
#                                         [Update: 2022-05-25 | 20:56 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  All colors directly from the system                                      #
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

class system_colors():

    """
    The colors directly available
    """

    # Basic colors
    W = '\033[0m'      # white (normal)
    R = '\033[31m'     # red
    G = '\033[32m'     # green
    O = '\033[33m'     # orange
    B = '\033[34m'     # blue
    P = '\033[35m'     # purple
    C = '\033[36m'     # cyan
    GR = '\033[37m'    # gray
    D = '\033[2m'      # dims current color. {W} resets.

    # Light colors
    cyan = '\033[36m'
    white = '\033[37m'
    light_gray = '\033[90m'
    light_R = '\033[91m'
    ll = '\033[92m'         # light_lime
    light_yellow = '\033[93m'
    light_B2 = '\033[94m'
    light_purple = '\033[95m'

    # Dark colors
    darkblack = '\033[030m'
    darkR = '\033[031m'
    darkgreen = '\033[032m'
    darkyellow = '\033[033m'
    darkB = '\033[034m'
    darkmagenta = '\033[035m'
    darkcyan = '\033[036m'
    darkwhite = '\033[037m'

    # Text formating
    bold = '\033[1m'
    dark = '\033[2m'
    italic = '\033[3m'
    underscore = '\033[4m'