#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opst.py                   [Created: 2022-06-10 | 6:32  - PM]  #
#                                       [Update:  2022-07-03 | 1:25  - AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The command-line parsing version of opst                                 #
#                                                                           #
#  Language  ~  Python3                                                     #
#---[Copyright]-------------------------------------------------------------#
#  Copyright (C) 2022 - © PSociety™, All rights reserved                    #
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

import argparse
import sys
import os
import subprocess
import textwrap
from time import strftime
from time import sleep
from omegapstoolkit.util.system_colors import system_colors as sc
from omegapstoolkit.util.clear import clear

# opstconsole's version
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstconsole", "r", encoding="utf-8") as opstconsole_version:
        __VERSION_OPSTCONSOLE = opstconsole_version.read()

# opstconsole_cli's version
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstconsole_cli", "r", encoding="utf-8") as opstconsole_CLI_version:
        __VERSION_OPSTCONSOLE_CLI = opstconsole_CLI_version.read()

# opstinstall's version
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstinstall", "r", encoding="utf-8") as opstinstall_version:
        __VERSION_OPSTINSTALL = opstinstall_version.read()

# opstinfo's version
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstinfo", "r", encoding="utf-8") as opstinfo_version:
        __VERSION_OPSTINFO = opstinfo_version.read()

# opstsetup's version
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstsetup", "r", encoding="utf-8") as opstsetup_version:
        __VERSION_OPSTSETUP = opstsetup_version.read()

# opstupdate's version
with open("/usr/share/omegapstoolkit-master/omegapstoolkit/util/versions/version_opstupdate", "r", encoding="utf-8") as opstupdate_version:
        __VERSION_OPSTUPDATE = opstupdate_version.read()

# __VERSION_OPSTCONSOLE='0.0.1.5'
# __VERSION_OPSTINSTALL='2.9'
# __VERSION_OPSTUPDATE='1.9'
# __VERSION_OPSTSETUP='1.5'
# __VERSION_OPSTINFO='1.5'


class BetterHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = f'{sc.C}Usage{sc.W}: '
        return super(BetterHelpFormatter, self).add_usage(
            usage, actions, groups, prefix)
    def _fill_text(self, text, width, indent):
        return ''.join(indent + line for line in text.splitlines(keepends=True))

def get_args():
    opst = argparse.ArgumentParser(
        prog="opst",
        description="OmegaPSToolkit ~ A massive penetration testing toolkit for penteser",
        epilog="",
        usage="opst [OPTION] [-h]",
        add_help=False,
        allow_abbrev=False,
        formatter_class=lambda prog: BetterHelpFormatter(prog, max_help_position=80, width=130,indent_increment=2),
        )

    opst._positionals.title = f'{sc.ll}Commands{sc.W}'
    opst._optionals.title = f'{sc.ll}Options{sc.W}'

    # Main options
    opst.add_argument(
        '-c','--console',
        action="store_true",
        help=f"start the console ({sc.G}opstconsole{sc.W}).",
    )

    opst.add_argument(
        '-i','--install',
        action="store_true",
        help=f"install all depencies for OmegaPSToolkit ({sc.G}opstinstall{sc.W})."
        )
    opst.add_argument(
        '-u','--update',
        action="store_true",
        help=f"update OmegaPSToolkit ({sc.G}opstupdate{sc.W})."
    )
    opst.add_argument(
        '-s','--setup',
        action="store_true",
        help=f"install all PIP package for OmegaPSToolkit ({sc.G}opstupdate{sc.W})."
    )

    # Options can be add with another option
    option_for_option = opst.add_argument_group(f"{sc.ll}Additional options{sc.W}")
    option_for_option.add_argument(
        "-y", "--yes",
        action="store_true",
        help='don\'t ask for confirmation for update or install'
        )
    option_for_option.add_argument(
        "-q", "--quiet",
        action="store_true",
        help='prevent header from displaying'
        )

    # Information's options
    info = opst.add_argument_group(f"{sc.ll}Information options{sc.W}")
    info.add_argument(
        '--info',
        action="store_true",
        help=f'show some information about OmegaPSToolkit and exit ({sc.G}opstinfo{sc.W}).'
    )
    info.add_argument(
        '-h',
        action="store_true",
        help="show more help for each option."
        )
    info.add_argument(
        '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='show this help message and exit.'
    )
    info.add_argument(
        '--version',
        type=str,
        nargs='?',
        const=1,
        metavar="console|install|update|setup|info|all",
        choices=['console','cli','install','update','setup','info','all'],
        help=f"show program's version and exit (default is {sc.G}opstconsole{sc.W})."
    )

    # for make group of options
    # group = aovpns.add_argument_group("Feature 1")

    if len(sys.argv) == 1:
        print(f"""opst: {sc.R}error{sc.W}: {sc.O}missing options{sc.W}
Try 'opst --help' for more information.""")
        sys.exit(1)
    return opst.parse_args()

def __main__():

    # Execute parse_args()
    args=get_args()

    try:
        if args.console:
            print("Starting opstconsole")
            sleep(1)

        elif args.update:
            if args.update:
                print("updating...")

        elif args.version:
            if args.h and args.version:
                print(f"""{sc.C}Usage{sc.W}: opst --version [console|install|update|setup|info|all]

The option for show all or each version of an {sc.G}opst{sc.W}'s command.

The default value, if you give no argument, is {sc.G}opstconsole{sc.W}.

All arguments avalable for {sc.C}--version{sc.W}:
  console   show the version of the main console of OPST ({sc.G}opstconsole{sc.W}).
  cli       show the version of the CLI version of opstconsole ({sc.G}opstconsole_cli{sc.W}).
  install   show the version of the install tool for OmegaPSToolkit ({sc.G}opstinstall{sc.W}).
  update    show the version of the update tool of OmegaPSToolkit ({sc.G}opstupdate{sc.W}).
  setup     show the version of the setup tool of OmegaPSToolkit ({sc.G}opstsetup{sc.W}).
  info      show the version of the informations command of OmegaPSToolkit ({sc.G}opstinfo{sc.W}).
  all       show all commands version's of OmegaPSToolkit.
            """)
            elif args.version == 'all':
                print(f"""OmegaPSToolkit (OPST), {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}
OmegaPSToolkit ({sc.G}opstconsole{sc.W}),     version: {__VERSION_OPSTCONSOLE}
OmegaPSToolkit ({sc.G}opstconsole cli{sc.W}), version: {__VERSION_OPSTCONSOLE_CLI}
OmegaPSToolkit ({sc.G}opstinstall{sc.W}),     version: {__VERSION_OPSTINSTALL}
OmegaPSToolkit ({sc.G}opstupdate{sc.W}),      version: {__VERSION_OPSTUPDATE}
OmegaPSToolkit ({sc.G}opstsetup{sc.W}),       version: {__VERSION_OPSTSETUP}
OmegaPSToolkit ({sc.G}opstinfo{sc.W}),        version: {__VERSION_OPSTINFO}""")

            elif args.version == 'console':
                print(f"OmegaPSToolkit (OPST), {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}.\nOmegaPSToolkit ({sc.G}opstconsole{sc.W}), version: {__VERSION_OPSTCONSOLE}")
            elif args.version == 'install':
                print(f"OmegaPSToolkit (OPST), {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}.\nOmegaPSToolkit ({sc.G}opstinstall{sc.W}), version: {__VERSION_OPSTINSTALL}")
            elif args.version == 'update':
                print(f"OmegaPSToolkit (OPST), {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}.\nOmegaPSToolkit ({sc.G}opstupdate{sc.W}), version: {__VERSION_OPSTUPDATE}")
            elif args.version == 'setup':
                print(f"OmegaPSToolkit (OPST), {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}.\nOmegaPSToolkit ({sc.G}opstsetup{sc.W}), version: {__VERSION_OPSTSETUP}")
            elif args.version == 'info':
                print(f"OmegaPSToolkit (OPST), {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}.\nOmegaPSToolkit ({sc.G}opstinfo{sc.W}), version: {__VERSION_OPSTINFO}")
            else:
                print(f"OmegaPSToolkit (OPST), {sc.italic}Copyright © 2021-2022 PSociety™{sc.W}, {sc.R}All rights reserved{sc.W}. {sc.italic}By Thomas Pellissier aka MyMeepSQL{sc.W}.\nOmegaPSToolkit ({sc.G}opstconsole{sc.W}), version: {__VERSION_OPSTCONSOLE}")


        elif args.h:
            print(f"""opst: {sc.R}error{sc.W}: argument -h: {sc.O}missing option{sc.W}
{sc.C}Usage{sc.W}: opst [OPTION] -h
  or:  opst -h [OPTION]

If you want to show more help and informations about an option or a command.

For use the {sc.G}-h{sc.W} option, you need to run it with a another option.

{sc.G}Avalable options{sc.W}:
  --version

{sc.G}Examples{sc.W}:
  --update -h   show the help message for the {sc.G}-u{sc.W}/{sc.G}--update{sc.W} option and exit.
  -h -c         show the help message for the {sc.G}-c{sc.W}/{sc.G}--console{sc.W} option and exit.

Try 'opst --help' for more information.""")
    except KeyboardInterrupt:
        print(f"\n[{sc.C}{sc.D}"+strftime("%X")+f"{sc.W}]  [{sc.O}INFO{sc.W}]  Interrupt received! Exiting cleanly...")
        sys.exit(1)

if __name__ == '__main__':
    try:
        __main__()
    except KeyboardInterrupt:
        print(f"\n[{sc.C}{sc.D}"+strftime("%X")+f"{sc.W}]  [{sc.O}INFO{sc.W}]  Interrupt received! Exiting cleanly...")