#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_ping_help.py            [Created: 2022-05-25 | 18:21 PM]  #
#                                         [Update: 2 022-06-31 | 8:31  AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for the ping command                                    #
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

def cli_ping_help():
    print(f"""
{sc.G}Usage{sc.GR}:
  {sc.W} [{sc.R}options{sc.W}] <{sc.G}destination{sc.W}>

{sc.C}Options{sc.GR}:{sc.W}
  <{sc.G}destination{sc.W}>         dns name or ip address
  -{sc.R}a{sc.W}                    use audible ping
  -{sc.R}A{sc.W}                    use adaptive ping
  -{sc.R}B{sc.W}                    sticky source address
  -{sc.R}c{sc.W} <{sc.O}count{sc.W}>            stop after <count> replies
  -{sc.R}D{sc.W}                    print timestamps
  -{sc.R}d{sc.W}                    use SO_DEBUG socket option
  -{sc.R}f{sc.W}                    flood ping
  -{sc.R}h{sc.W}                    print help and exit
  -{sc.R}I{sc.W} <{sc.O}interface{sc.W}>        either interface name or address
  -{sc.R}i{sc.W} <{sc.O}interval{sc.W}>         seconds between sending each packet
  -{sc.R}L{sc.W}                    suppress loopback of multicast packets
  -{sc.R}l{sc.W} <{sc.O}preload{sc.W}>          send <preload> number of packages while waiting replies
  -{sc.R}m{sc.W} <{sc.O}mark{sc.W}>             tag the packets going out
  -{sc.R}M{sc.W} <{sc.O}pmtud opt{sc.W}>        define mtu discovery, can be one of <do|dont|want>
  -{sc.R}n{sc.W}                    no dns name resolution
  -{sc.R}O{sc.W}                    report outstanding replies
  -{sc.R}p{sc.W} <{sc.O}pattern{sc.W}>          contents of padding byte
  -{sc.R}q{sc.W}                    quiet output
  -{sc.R}Q{sc.W} <{sc.O}tclass{sc.W}>           use quality of service <tclass> bits
  -{sc.R}s{sc.W} <{sc.O}size{sc.W}>             use <size> as number of data bytes to be sent
  -{sc.R}S{sc.W} <{sc.O}size{sc.W}>             use <size> as SO_SNDBUF socket option value
  -{sc.R}t{sc.W} <{sc.O}ttl{sc.W}>              define time to live
  -{sc.R}U{sc.W}                    print user-to-user latency
  -{sc.R}v{sc.W}                    verbose output
  -{sc.R}V{sc.W}                    print version and exit
  -{sc.R}w{sc.W} <{sc.O}deadline{sc.W}>         reply wait <deadline> in seconds
  -{sc.R}W{sc.W} <{sc.O}timeout{sc.W}>          time to wait for response

{sc.C}IPv4 options{sc.GR}:{sc.W}
  -{sc.R}4{sc.W}                    use IPv4
  -{sc.R}b{sc.W}                    allow pinging broadcast
  -{sc.R}R{sc.W}                    record route
  -{sc.R}T{sc.W} <{sc.O}timestamp{sc.W}>        define timestamp, can be one of <tsonly|tsandaddr|tsprespec>

{sc.C}IPv6 options{sc.GR}:{sc.W}
  -{sc.R}6{sc.W}                    use IPv6
  -{sc.R}F{sc.W} <{sc.O}flowlabel{sc.W}>        define flow label, default is random
  -{sc.R}N{sc.W} <{sc.O}nodeinfo opt{sc.W}>     use icmp6 node info query, try <help> as argument

{sc.C}Commands{sc.GR}:{sc.W}
  {sc.B}clear{sc.W}                 clear the terminal
  {sc.B}leave{sc.W}                 leave the ping tool
  {sc.B}man ping{sc.W}              get all details about ping command

{sc.C}Exemple{sc.GR}:{sc.W}
  -{sc.R}c {sc.O}4 {sc.G}1.1.1.1{sc.W}
  -{sc.R}q {sc.G}google.com{sc.W}
  -{sc.R}c {sc.O}4 {sc.G}https://duckduckgo.com{sc.W}
""")