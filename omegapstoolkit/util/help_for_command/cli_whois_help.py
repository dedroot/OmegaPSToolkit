#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_whois_help.py           [Created: 2022-05-25 | 18:32 PM]  #
#                                         [Update: 2 022-06-31 | 8:31  AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for the whois command                                   #
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

import sys
from ..system_colors import system_colors as sc

def cli_whois_help():
    print(f"""
{sc.G}Usage{sc.GR}:{sc.W}
  [{sc.R}OPTION{sc.W}]... {sc.G}OBJECT{sc.W}...

  -{sc.R}h {sc.O}HOST{sc.W}, --{sc.R}host {sc.O}HOST{sc.W}   connect to server HOST
  -{sc.R}p {sc.O}PORT{sc.W}, --{sc.R}port {sc.O}PORT{sc.W}   connect to PORT
  -{sc.R}I{sc.W}                     query whois.iana.org and follow its referral
  -{sc.R}H{sc.W}                     hide legal disclaimers
      --{sc.R}verbose{sc.W}        explain what is being done
      --{sc.R}help{sc.W}           display this help and exit
      --{sc.R}version{sc.W}        output version information and exit

These flags are supported by whois.ripe.net and some RIPE-like servers:
  -{sc.R}l{sc.W}                     find the one level less specific match
  -{sc.R}L{sc.W}                     find all levels less specific matches
  -{sc.R}m{sc.W}                     find all one level more specific matches
  -{sc.R}M{sc.W}                     find all levels of more specific matches
  -{sc.R}c{sc.W}                     find the smallest match containing a mnt-irt attribute
  -{sc.R}x{sc.W}                     exact match
  -{sc.R}b{sc.W}                     return brief IP address ranges with abuse contact
  -{sc.R}B{sc.W}                     turn off object filtering (show email addresses)
  -{sc.R}G{sc.W}                     turn off grouping of associated objects
  -{sc.R}d{sc.W}                     return DNS reverse delegation objects too
  -{sc.R}i {sc.O}ATTR{sc.W}[,{sc.R}ATTR{sc.W}]...      do an inverse look-up for specified ATTRibutes
  -{sc.R}T {sc.O}TYPE{sc.W}[,{sc.R}TYPE{sc.W}]...      only look for objects of TYPE
  -{sc.R}K{sc.W}                     only primary keys are returned
  -{sc.R}r{sc.W}                     turn off recursive look-ups for contact information
  -{sc.R}R{sc.W}                     force to show local copy of the domain object even
                       if it contains referral
  -{sc.R}a{sc.W}                     also search all the mirrored databases
  -{sc.R}s {sc.O}SOURCE{sc.W}[,{sc.O}SOURCE{sc.W}]...  search the database mirrored from SOURCE
  -{sc.R}g {sc.O}SOURCE:FIRST-LAST{sc.W}   find updates from SOURCE from serial FIRST to LAST
  -{sc.R}t {sc.O}TYPE{sc.W}                request template for object of TYPE
  -{sc.R}v {sc.O}TYPE{sc.W}                request verbose template for object of TYPE
  -{sc.R}q{sc.W} [{sc.R}version{sc.W}|{sc.R}sources{sc.W}|{sc.R}types{sc.W}]  query specified server info
""")
