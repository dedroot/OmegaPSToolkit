#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ colored_colors.py           [Created: 2022-05-25 | 20:56 AM]  #
#                                         [Update: 2022-05-25 | 20:56 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  All colors from the "colored" PIP module                                 #
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

class colored_colors():

    """
    The colors from the "colored" pip module
    """

    from colored import fg, attr
    # The blues
    bC = fg('#1d89f3')      # B
    bC2 = fg('#0B4D8F')     # dark B

    # The reds
    rC = fg('#F44336')      # R
    rC3 = fg('#ffa000')     # light orange
    rC2 = fg('#ec5a0d')     # orange

    # The greens
    gC = fg('#39CC3F')      # green

    # The yellows
    yC = fg('#EDFF00')

    # Reset
    r = attr('reset')       # to finish the color formatting