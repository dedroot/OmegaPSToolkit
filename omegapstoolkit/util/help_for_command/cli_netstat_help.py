#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_netstat_help.py         [Created: 2022-05-25 | 18:37 PM]  #
#                                         [Update: 2 022-06-31 | 8:31  AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for the netstat command                                 #
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

def cli_netstat_help():
    print(f"""
{sc.G}Usage{sc.GR}:{sc.W}
   [-{sc.R}vWeenNcCF{sc.W}] [<Af>] -{sc.R}r{sc.W}        ( netstat -{sc.R}V{sc.W}|--{sc.R}version{sc.W}|-{sc.R}h{sc.W}|--{sc.R}help{sc.W} )
   [-{sc.R}vWnNcaeol{sc.W}] [<Socket> ...]
   ( [-{sc.R}vWeenNac{sc.W}] -{sc.R}i{sc.W} | [-{sc.R}cnNe{sc.W}] -{sc.R}M{sc.W} | -{sc.R}s{sc.W} [-{sc.R}6tuw{sc.W}] )

        -{sc.R}r{sc.W}, --{sc.R}route{sc.W}              display routing table
        -{sc.R}i{sc.W}, --{sc.R}interfaces{sc.W}         display interface table
        -{sc.R}g{sc.W}, --{sc.R}groups{sc.W}             display multicast group memberships
        -{sc.R}s{sc.W}, --{sc.R}statistics{sc.W}         display networking statistics (like SNMP)
        -{sc.R}M{sc.W}, --{sc.R}masquerade{sc.W}         display masqueraded connections

        -{sc.R}v{sc.W}, --{sc.R}verbose{sc.W}            be verbose
        -{sc.R}W{sc.W}, --{sc.R}wide{sc.W}               don't truncate IP addresses
        -{sc.R}n{sc.W}, --{sc.R}numeric{sc.W}            don't resolve names
        --{sc.R}numeric-hosts{sc.W}          don't resolve host names
        --{sc.R}numeric-ports{sc.W}          don't resolve port names
        --{sc.R}numeric-users{sc.W}          don't resolve user names
        -{sc.R}N{sc.W}, --{sc.R}symbolic{sc.W}           resolve hardware names
        -{sc.R}e{sc.W}, --{sc.R}extend{sc.W}             display other/more information
        -{sc.R}p{sc.W}, --{sc.R}programs{sc.W}           display PID/Program name for sockets
        -{sc.R}o{sc.W}, --{sc.R}timers{sc.W}             display timers
        -{sc.R}c{sc.W}, --{sc.R}continuous{sc.W}         continuous listing

        -{sc.R}l{sc.W}, --{sc.R}listening{sc.W}          display listening server sockets
        -{sc.R}a{sc.W}, --{sc.R}all{sc.W}                display all sockets (default: connected)
        -{sc.R}F{sc.W}, --{sc.R}fib{sc.W}                display Forwarding Information Base (default)
        -{sc.R}C{sc.W}, --{sc.R}cache{sc.W}              display routing cache instead of FIB
        -{sc.R}Z{sc.W}, --{sc.R}context{sc.W}            display SELinux security context for sockets

  <Socket>=(-{sc.R}t{sc.W}|--{sc.R}tcp{sc.W}) (-{sc.R}u{sc.W}|--{sc.R}udp{sc.W}) (-{sc.R}U{sc.W}|--{sc.R}udplite{sc.W}) (-{sc.R}S{sc.W}|--{sc.R}sctp{sc.W}) (-{sc.R}w{sc.W}|--{sc.R}raw{sc.W})
           (-{sc.R}x{sc.W}|--{sc.R}unix{sc.W}) --{sc.R}ax25{sc.W} --{sc.R}ipx{sc.W} --{sc.R}netrom{sc.W}

  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25)
    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP)
    x25 (CCITT X.25)
""")