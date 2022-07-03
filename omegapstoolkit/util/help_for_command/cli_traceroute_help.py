#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_traceroute_help.py      [Created: 2022-05-25 | 18:25 PM]  #
#                                         [Update: 2 022-06-31 | 8:31  AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The help message for the traceroute command                              #
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

def cli_traceroute_help():
    print(f"""
{sc.G}Usage{sc.GR}:{sc.W}
  [ -{sc.R}46dFITnreAUDV{sc.W} ] [ -{sc.R}f {sc.O}first_ttl{sc.W} ] [ -{sc.R}g {sc.O}gate{sc.W},... ] [ -{sc.R}i {sc.O}device{sc.W} ] [ -{sc.R}m max_ttl{sc.W} ] 
  [ -{sc.R}N {sc.O}squeries{sc.W} ] [ -{sc.R}p {sc.O}port{sc.W} ] [ -{sc.R}t {sc.O}tos{sc.W} ] [ -{sc.R}l {sc.O}flow_label{sc.W} ] [ -{sc.R}w {sc.O}MAX{sc.W},{sc.O}HERE{sc.W},{sc.O}NEAR{sc.W} ] 
  [ -{sc.R}q {sc.O}nqueries{sc.W} ] [ -{sc.R}s {sc.O}src_addr{sc.W} ] [ -{sc.R}z {sc.O}sendwait{sc.W} ] [ --{sc.R}fwmark{sc.P}={sc.O}num{sc.W} ] {sc.B}host{sc.W} [ {sc.O}packetlen{sc.W} ]

{sc.C}Options{sc.GR}:{sc.W}
  -{sc.R}4{sc.W}                            Use IPv4
  -{sc.R}6{sc.W}                            Use IPv6
  -{sc.R}d{sc.W}  --{sc.R}debug{sc.W}                   Enable socket level debugging
  -{sc.R}F{sc.W}  --{sc.R}dont-fragment{sc.W}           Do not fragment packets
  -{sc.R}f{sc.W} {sc.O}first_ttl{sc.W}  --{sc.R}first{sc.P}={sc.O}first_ttl{sc.W}
                                Start from the first_ttl hop (instead from 1)
  -{sc.R}g{sc.W} {sc.O}gate{sc.W},...  --{sc.R}gateway{sc.P}={sc.O}gate{sc.W},...
                                Route packets through the specified gateway
                                (maximum 8 for IPv4 and 127 for IPv6)
  -{sc.R}I{sc.W}  --{sc.R}icmp{sc.W}                    Use ICMP ECHO for tracerouting
  -{sc.R}T{sc.W}  --{sc.R}tcp{sc.W}                     Use TCP SYN for tracerouting (default port is 80)
  -{sc.R}i{sc.W} {sc.O}device{sc.W}  --{sc.R}interface{sc.P}={sc.O}device{sc.W}
                                Specify a network interface to operate with
  -{sc.R}m{sc.W} {sc.O}max_ttl{sc.W}  --{sc.R}max-hops{sc.P}={sc.O}max_ttl{sc.W}
                                Set the max number of hops (max TTL to be
                                reached). Default is 30
  -{sc.R}N{sc.W} {sc.O}squeries{sc.W}  --{sc.R}sim-queries{sc.P}={sc.O}squeries{sc.W}
                                Set the number of probes to be tried
                                simultaneously (default is 16)
  -{sc.R}n{sc.W}                            Do not resolve IP addresses to their domain names
  -{sc.R}p{sc.W} {sc.O}port{sc.W}  --{sc.R}port{sc.P}={sc.O}port{sc.W}          Set the destination port to use. It is either
                                initial udp port value for "default" method
                                (incremented by each probe, default is 33434), or
                                initial seq for "icmp" (incremented as well,
                                default from 1), or some constant destination
                                port for other methods (with default of 80 for
                                "tcp", 53 for "udp", etc.)
  -{sc.R}t{sc.W} {sc.O}tos{sc.W}  --{sc.R}tos{sc.P}={sc.O}tos{sc.W}             Set the TOS (IPv4 type of service) or TC (IPv6
                                traffic class) value for outgoing packets
  -{sc.R}l{sc.W} {sc.O}flow_label{sc.W}  --{sc.R}flowlabel{sc.P}={sc.O}flow_label{sc.W}
                                Use specified flow_label for IPv6 packets
  -{sc.R}w{sc.W} {sc.O}MAX{sc.W},{sc.O}HERE{sc.W},{sc.O}NEAR{sc.W}  --{sc.R}wait{sc.P}={sc.O}MAX{sc.W},{sc.O}HERE{sc.W},{sc.O}NEAR{sc.W}
                                Wait for a probe no more than HERE (default 3)
                                times longer than a response from the same hop,
                                or no more than NEAR (default 10) times than some
                                next hop, or MAX (default 5.0) seconds (float
                                point values allowed too)
  -{sc.R}q{sc.W} {sc.O}nqueries{sc.W}  --{sc.R}queries{sc.P}={sc.O}nqueries{sc.W}
                                Set the number of probes per each hop. Default is
                                3
  -{sc.R}r{sc.W}                            Bypass the normal routing and send directly to a
                                host on an attached network
  -{sc.R}s{sc.W} {sc.O}src_addr{sc.W}  --{sc.R}source{sc.P}={sc.R}src_addr{sc.W}
                                Use source src_addr for outgoing packets
  -{sc.R}z{sc.W} {sc.O}sendwait{sc.W}  --{sc.R}sendwait{sc.P}={sc.O}sendwait{sc.W}
                                Minimal time interval between probes (default 0).
                                If the value is more than 10, then it specifies a
                                number in milliseconds, else it is a number of
                                seconds (float point values allowed too)
  -{sc.R}e{sc.W}  --{sc.R}extensions{sc.W}              Show ICMP extensions (if present), including MPLS
  -{sc.R}A{sc.W}  --{sc.R}as-path-lookups{sc.W}         Perform AS path lookups in routing registries and
                                print results directly after the corresponding
                                addresses
  -{sc.R}M{sc.W} {sc.O}name{sc.W}  --{sc.R}module{sc.P}={sc.O}name{sc.W}        Use specified module (either builtin or external)
                                for traceroute operations. Most methods have
                                their shortcuts (`-I' means `-M icmp' etc.)
  -{sc.R}O{sc.W} {sc.O}OPTS{sc.W},...  --{sc.R}options{sc.P}={sc.O}OPTS{sc.W},...
                                Use module-specific option OPTS for the
                                traceroute module. Several OPTS allowed,
                                separated by comma. If OPTS is "help", print info
                                about available options
  --{sc.R}sport{sc.P}={sc.R}num{sc.W}                   Use source port num for outgoing packets. Implies
                                `-N 1'
  --{sc.R}fwmark{sc.P}={sc.R}num{sc.W}                  Set firewall mark for outgoing packets
  -{sc.R}U{sc.W}  --{sc.R}udp{sc.W}                     Use UDP to particular port for tracerouting
                                (instead of increasing the port per each probe),
                                default port is 53
  -{sc.R}UL{sc.W}                           Use UDPLITE for tracerouting (default dest port
                                is 53)
  -{sc.R}D{sc.W}  --{sc.R}dccp{sc.W}                    Use DCCP Request for tracerouting (default port
                                is 33434)
  -{sc.R}P {sc.O}prot{sc.W}  --{sc.R}protocol{sc.P}={sc.O}prot{sc.W}      Use raw packet of protocol prot for tracerouting
  --{sc.R}mtu{sc.W}                         Discover MTU along the path being traced. Implies
                                `-F -N 1'
  --{sc.R}back{sc.W}                        Guess the number of hops in the backward path and
                                print if it differs
  -{sc.R}V{sc.W}  --{sc.R}version{sc.W}                 Print version info and exit
  --{sc.R}help{sc.W}                        Read this help and exit

{sc.C}Arguments{sc.GR}:{sc.W}
+ {sc.G}host{sc.W}                          The host to traceroute to
  {sc.O}packetlen{sc.W}                     The full packet length (default is the length of an IP
                                header plus 40). Can be ignored or increased to a minimal
                                allowed value

{sc.C}Commands{sc.GR}:{sc.W}
  {sc.B}clear{sc.W}                         Clear the terminal
  {sc.B}leave{sc.W}                         leave the {sc.R}traceroute{sc.W} tool
  {sc.B}man traceroute{sc.W}                get all details about {sc.R}traceroute{sc.W} command

{sc.C}Exemple{sc.GR}:{sc.W}
  -{sc.R}n{sc.W} {sc.G}8.8.8.8{sc.W}
  -{sc.R}n{sc.W} -{sc.R}p{sc.W} {sc.O}61600{sc.W} {sc.G}google.com{sc.W}
""")