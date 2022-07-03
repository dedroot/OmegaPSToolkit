#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ distribution_name.py      [Created: 2022-05-25 | 18:06 - PM]  #
#                                       [Update:  2022-06-31 | 8:31  - AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The function for get the current Linux's distribution name               #
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

## For the distribution's name

import sys
from .system_colors import system_colors as sc

import csv
RELEASE_DATA = {}

with open("/etc/os-release") as f:
    reader = csv.reader(f, delimiter="=")
    for row in reader:
        if row:
            RELEASE_DATA[row[0]] = row[1]

if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
    with open("/etc/debian_version") as f:
        DEBIAN_VERSION = f.readline().strip()
    major_version = DEBIAN_VERSION.split(".")[0]
    version_split = RELEASE_DATA["VERSION"].split(" ", maxsplit=1)
    if version_split[0] == major_version:
        # Just major version shown, replace it with the full version
        RELEASE_DATA["VERSION"] = " ".join([DEBIAN_VERSION] + version_split[1:])
else:
    distribution_name=f"{sc.O}Can't find the distribution name or not a Linux distribution{sc.W}"

distribution_name="{} {}".format(RELEASE_DATA["PRETTY_NAME"], RELEASE_DATA["VERSION"])