#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ cli_nslookup_man_help.py    [Created: 2022-05-25 | 18:40 PM]  #
#                                         [Update: 2022-05-25 | 18:53 PM]   #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The man help message for the nslookup command                            #
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

def cli_nslookup_man_help():
    print(f"""
    {sc.G}NAME{sc.GR}:{sc.W}
       nslookup - query Internet name servers interactively

{sc.C}SYNOPSIS{sc.GR}:{sc.W}
       nslookup [-option] [name | -] [server]

{sc.C}DESCRIPTION{sc.GR}:{sc.W}
       Nslookup is a program to query Internet domain name servers.  Nslookup has two modes: interactive and non-interactive. Interactive mode allows
       the user to query name servers for information about various hosts and domains or to print a list of hosts in a domain. Non-interactive mode is
       used to print just the name and requested information for a host or domain.

{sc.C}COMMANDS{sc.GR}:{sc.W}
       clear
           Clear the terminal (the {sc.R}cls{sc.W} (the windows clear command) command can't be run)

       leave
           Leave the nslookup tool

       man nslookup
           Show this message and exit

{sc.C}ARGUMENTS{sc.GR}:{sc.W}
       Interactive mode is entered in the following cases:

        1. when no arguments are given (the default name server will be used)

        2. when the first argument is a hyphen (-) and the second argument is the host name or Internet address of a name server.

       Non-interactive mode is used when the name or Internet address of the host to be looked up is given as the first argument. The optional second
       argument specifies the host name or address of a name server.

       Options can also be specified on the command line if they precede the arguments and are prefixed with a hyphen. For example, to change the
       default query type to host information, and the initial timeout to 10 seconds, type:

           nslookup -query=hinfo  -timeout=10

       The -version option causes nslookup to print the version number and immediately exits.

{sc.C}INTERACTIVE COMMANDS{sc.GR}:{sc.W}
       host [server]
           Look up information for host using the current default server or using server, if specified. If host is an Internet address and the query
           type is A or PTR, the name of the host is returned. If host is a name and does not have a trailing period, the search list is used to qualify
           the name.

           To look up a host not in the current domain, append a period to the name.

       server domain

       lserver domain
           Change the default server to domain; lserver uses the initial server to look up information about domain, while server uses the current
           default server. If an authoritative answer can't be found, the names of servers that might have the answer are returned.

       {sc.G}root{sc.W}
           not implemented

       {sc.G}finger{sc.W}
           not implemented

       {sc.G}ls{sc.W}
           not implemented

       {sc.G}view{sc.W}
           not implemented

       {sc.G}help{sc.W}
           not implemented

       {sc.G}?{sc.W}
           not implemented

       {sc.G}exit{sc.W}
           Exits the program.

       {sc.G}set keyword[=value]{sc.W}
           This command is used to change state information that affects the lookups. Valid keywords are:

           all
               Prints the current values of the frequently used options to set. Information about the current default server and host is also printed.

           class=value
               Change the query class to one of:

               IN
                   the Internet class

               CH
                   the Chaos class

               HS
                   the Hesiod class

               ANY
                   wildcard

               The class specifies the protocol group of the information.

               (Default = IN; abbreviation = cl)

           [no]debug
               Turn on or off the display of the full response packet and any intermediate response packets when searching.

               (Default = nodebug; abbreviation = [no]deb)

           [no]d2
               Turn debugging mode on or off. This displays more about what nslookup is doing.

               (Default = nod2)

           domain=name
               Sets the search list to name.

           [no]search
               If the lookup request contains at least one period but doesn't end with a trailing period, append the domain names in the domain search
               list to the request until an answer is received.

               (Default = search)

           port=value
               Change the default TCP/UDP name server port to value.

               (Default = 53; abbreviation = po)

           querytype=value

           type=value
               Change the type of the information query.

               (Default = A and then AAAA; abbreviations = q, ty)

               Note: It is only possible to specify one query type, only the default behavior looks up both when an alternative is not specified.

           [no]recurse
               Tell the name server to query other servers if it does not have the information.

               (Default = recurse; abbreviation = [no]rec)

           ndots=number
               Set the number of dots (label separators) in a domain that will disable searching. Absolute names always stop searching.

           retry=number
               Set the number of retries to number.

           timeout=number
               Change the initial timeout interval for waiting for a reply to number seconds.

           [no]vc
               Always use a virtual circuit when sending requests to the server.

               (Default = novc)

           [no]fail
               Try the next nameserver if a nameserver responds with SERVFAIL or a referral (nofail) or terminate query (fail) on such a response.

               (Default = nofail)

{sc.C}RETURN VALUES{sc.GR}:{sc.W}
       nslookup returns with an exit status of 1 if any query failed, and 0 otherwise.

{sc.C}IDN SUPPORT{sc.GR}:{sc.W}
       If nslookup has been built with IDN (internationalized domain name) support, it can accept and display non-ASCII domain names.  nslookup
       appropriately converts character encoding of domain name before sending a request to DNS server or displaying a reply from the server. If you'd
       like to turn off the IDN support for some reason, define the IDN_DISABLE environment variable. The IDN support is disabled if the variable is set
       when nslookup runs or when the standard output is not a tty.

{sc.C}FILES{sc.GR}:{sc.W}
       /etc/resolv.conf

{sc.C}SEE ALSO{sc.GR}:{sc.W}
       dig(1), host(1), named(8).

{sc.C}AUTHOR{sc.GR}:{sc.W}
       Internet Systems Consortium, Inc.

{sc.C}COPYRIGHT{sc.GR}:{sc.W}
       Copyright © 2004-2007, 2010, 2013-2020 Internet Systems Consortium, Inc. ("ISC")
""")
