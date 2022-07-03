<!--

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ README.MD                     [Update: 2022-05-29 | 12:13 AM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  A long description of OmegaPSToolkit                                     #
#                                                                           #
#  Language  ~  Markdown                                                    #
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

-->

# **OmegaPSToolkit**
> [![MadeBy](https://img.shields.io/badge/Made%20by-Thomas%20Pellissier-informational?style=flat-square)](https://github.com/MyMeepSQL)
[![Codename](https://img.shields.io/badge/Codename-MyMeepSQL-informational?style=flat-square)](https://github.com/MyMeepSQL)
[![Owner](https://img.shields.io/badge/Owner-©%20PSociety™-informational?style=flat-square)](https://github.com/MyMeepSQL)
[![opstconsole_version](https://img.shields.io/badge/opstconsole%20version-v0.0.1.8-brightgreen?style=flat-square)](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md)
[![opstconsole_cli_Version](https://img.shields.io/badge/opstconsole_CLI%20Version%20[BETA]-v0.0.1.5-red?style=flat-square)](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md)
[![opsthelp_version](https://img.shields.io/badge/opsthelp%20version-v3.0-success?style=flat-square)](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md)
[![opstsetup_version](https://img.shields.io/badge/opstsetup%20version-v2.6-success?style=flat-square)](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md)
[![opstupdate_version](https://img.shields.io/badge/opstupdate%20version-v2.9-success?style=flat-square)](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md)
[![opstinstall-all_version](https://img.shields.io/badge/opstinstall%20version-v2.2-success?style=flat-square)](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md)
[![Release](https://img.shields.io/badge/Release-In%20Development-yellow?style=flat-square)]()
[![Supported OS](https://img.shields.io/badge/Supported%20OS-Linux-brightgreen?style=flat-square)]()
[![Licence](https://img.shields.io/badge/License-GNU%20GPL--3.0-important?style=flat-square)](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/LICENSE)
[![Contrinutions](https://img.shields.io/badge/Contributions-Open%20!-yellow?style=flat-square)]()
> > ### _**A massive penetration testing toolkit**_
> 
> # **Summary**
> - [**About OmegaPSToolkit**](https://github.com/MyMeepSQL/OmegaPSToolkit#about-omegapstoolkit)
>   - [**Changelog**](https://github.com/MyMeepSQL/OmegaPSToolkit#changelogs)
>   - [**License**](https://github.com/MyMeepSQL/OmegaPSToolkit#license)
>   - [**Features**](https://github.com/MyMeepSQL/OmegaPSToolkit#features)
> - [**Installation**](https://github.com/MyMeepSQL/OmegaPSToolkit#installation)
>   - [**Install Git tool**](https://github.com/MyMeepSQL/OmegaPSToolkit#step-1--install-git-tool-for-clone-this-repositories-with-if-you-didnt-have-it)
>   - [**Clone repositorie**](https://github.com/MyMeepSQL/OmegaPSToolkit#step-2--clone-the-repositorie-with)
>   - [**Go to the OmegaPSToolkit repositorie**](https://github.com/MyMeepSQL/OmegaPSToolkit#step-3--go-to-the-omegapstoolkit-repositorie-folder-with)
>   - [**Install Python3, PIP3 and make all "opst"'s commands**](https://github.com/MyMeepSQL/OmegaPSToolkit#step-4--to-install-python3-and-pip3-run-the-opstinstall-allsh-with)
>   - [**Install all PIP3's packages and make the OmegaPSToolkit's package**](https://github.com/MyMeepSQL/OmegaPSToolkit#step-5--run-the-setuptool-for-install-all-pip-modules-that-you-must-have-with)
>   - [**Run OPSTConsole**](https://github.com/MyMeepSQL/OmegaPSToolkit#step-6--run-the-omegapstoolkit-with)
> - [**Update**](https://github.com/MyMeepSQL/OmegaPSToolkit#update)
> - [**Help**](https://github.com/MyMeepSQL/OmegaPSToolkit#help)
> - [**Overview**](https://github.com/MyMeepSQL/OmegaPSToolkit#tool-overview)
>   - [**OPSTConsole**](https://github.com/MyMeepSQL/OmegaPSToolkit#opstconsole)
>   - [**OPSTConsole CLI**](https://github.com/MyMeepSQL/OmegaPSToolkit#opstconsole-cli)
>   - [**OPSTHelp**](https://github.com/MyMeepSQL/OmegaPSToolkit#opsthelp)
>   - [**OPSTUpdate**](https://github.com/MyMeepSQL/OmegaPSToolkit#opstupdate)
>   - [**OPSTSetup**](https://github.com/MyMeepSQL/OmegaPSToolkit#opstsetup)
>   - [**OPSTInstall-all**](https://github.com/MyMeepSQL/OmegaPSToolkit#opstinstall-all)
> # **About OmegaPSToolkit**
> _**`The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL ! 2021-2022, All rights reserved.`**_
>
>  **OmegaPSToolkit (OPST)** is a toolkit that brings together penetration testing tools such as wireless tools, web tools, password cracking tools, etc.
> * **`Totally in development!`**
> * Can only be run on **Linux machine**
> * This tool is for educational purposes only, the use of **OmegaPSToolkit** on a target without its consent is totally **illegal!** I will not take any responsibility if this program is used explicitly
> 
> ## **Changelogs**
> All new changes compared to all _**OPSTs'**_ commands can be found _[here](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md)_.
> ## **License**
> This program uses the license _[General Public License v3.0](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/LICENSE)_.
> ## **Features**
> The tools will be categorized as:
>  * Scanning tools,
>  * Password Attacks,
>  * Wireless Attacks,
>  * Web Attack,
>  * Social Engineering Tools,
>  * Sniffing & Spoofing,
>  * Vulnerability Analysis,
>  * Exploitation Tools,
>  * UTools (UsefullTools made by me),
>  * _**And more**_
> 
> # **Installation**
> Instructions to install ***OmegaPSToolkit***... (Linux commands)
> 
> * ### _Step 1_ : Install **git** tool for clone this repositories with (if you didn’t have it):
>   ```bash
>   sudo apt install git -y
>   ```
> * ### _Step 2_ : **Clone** the repositorie with:
>   ```bash
>   sudo git clone https://github.com/MyMeepSQL/OmegaPSToolkit.git
>   ```
> * ### _Step 3_ : Go to the **OmegaPSToolkit repositorie folder** with:
>   ```bash
>   cd OmegaPSToolkit
>   ```
> * ### _Step 4_ : To install **Python3**,**PIP3**  and **all the tools that OPST must have**, run the "opstinstall-all.sh" with:
>   ```bash
>   bash opstinstall-all.sh
>   ```
> * ### _Step 5_ : Run the "**SetupTool**" for install all _pip modules_ that you must have with:
>   ```bash
>   sudo opstsetup install
>   ```
> * ### _Step 6_ : Run the **OmegaPSToolkit** with:
>   ```bash
>   sudo opstconsole                      # You can run OPST anywhere (tell me if a problem appears) 
>   ```
>   **Or**
>   ```bash
>   sudo python3 opstconsole              # You must be in its directory to run OPST like this (/usr/share/OmegaPSToolkit/)
>   ```
>> ## **Update**
>>To download the latest version of OPSTConsole, OPSTSetup, OPSTHelp and the OPSTInstall-all.
>>* Run the "OPSTUpdate" with:
>>   ```bash
>>   sudo opstupdate
>>   ```
>> ## **Help**
>>If you want the help message with all "opst" commands and with other information like the version of each command, what is your OS and other informations.
>>* Run the "OPSThelp" with:
>>   ```bash
>>   opsthelp
>>   ```
>
> # Tool overview
> ## OPSTConsole
> ![opstconsole](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/Screens/opstconsole_main_page.png)
> 
> ## OPSTConsole CLI
> ![opstconsole_cli](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/Screens/opstconsole_cli.png)
> 
> ## OPSTHelp
> ![opsthelp](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/Screens/opsthelp.png)
> 
> ## OPSTUpdate
> ![opstupdate](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/Screens/opstupdate.png)
>
> ## OPSTSetup 
> ![opsthelp](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/Screens/opstsetup.png)
>
> ## OPSTInstall-all
> ![opstupdate](https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/Screens/opstinstall-all.png)