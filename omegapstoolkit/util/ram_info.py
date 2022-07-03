#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ ram_info.py                 [Created: 2022-05-25 | 18:05 PM]  #
#                                         [Update: 2022-05-25 | 18:15 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The function for get details abour RAM usage                             #
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

import psutil

# Total RAM
RAM_total_memory=f"{round(psutil.virtual_memory().total/1000000000, 2)} GB"
# Available RAM
RAM_avalable_memory=f"{round(psutil.virtual_memory().available/1000000000, 2)} GB"
# Used RAM
RAM_used_memory=f"{round(psutil.virtual_memory().used/1000000000, 2)} GB"
# RAM usage
RAM_usage=f"{psutil.virtual_memory().percent}%"