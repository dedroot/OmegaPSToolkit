#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ gpu_details.py            [Created: 2022-05-25 | 12:08 - AM]  #
#                                       [Update:  2022-06-31 | 8:31  - AM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaPSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The function for get some details on all GPUs of the user                #
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

import GPUtil
import sys
from .system_colors import system_colors as sc
# Get GPU details
gpus = GPUtil.getGPUs()
for gpu in gpus:
    global GPU_details_id
    global GPU_details_gpuName
    global GPU_details_load
    global GPU_details_freeMemory
    global GPU_details_usedMemory
    global GPU_details_totalMemoy
    global GPU_details_temperature
    global GPU_details_uuid 
    global GPU_details_driverVersion

    # get the GPU id
    GPU_details_id = gpu.id
    # name of GPU
    GPU_details_gpuName = gpu.name
    # get % percentage of GPU usage of that GPU
    GPU_details_load = f"{gpu.load*100}%"
    # get free memory in MB format
    GPU_details_freeMemory = f"{gpu.memoryFree}MB"
    # get used memory
    GPU_details_usedMemory = f"{gpu.memoryUsed}MB"
    # get total memory
    GPU_details_totalMemoy = f"{gpu.memoryTotal}MB"
    # get GPU temperature in Celsius
    GPU_details_temperature = f"{gpu.temperature} °C"
    # get the driver version
    GPU_details_driverVersion = f"{gpu.driver}"

    GPU_details_uuid = gpu.uuid

    if GPU_details_temperature >= "65":
        GPU_details_temperature = f"{sc.R}{GPU_details_temperature}{sc.W}"
    elif GPU_details_temperature <= "60":
        GPU_details_temperature = f"{sc.O}{GPU_details_temperature}{sc.W}"
    elif GPU_details_temperature <= "45":
        GPU_details_temperature = f"{sc.B}{GPU_details_temperature}{sc.W}"