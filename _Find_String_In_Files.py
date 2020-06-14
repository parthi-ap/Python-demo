import glob
import os
import os.path
import re
import time
import xlwt
import sys
import datetime
from sys import *
import math
import csv
#!/usr/bin/env python3
import fileinput
import tempfile
import string

## Before Running remove READ ONLY
list_of_Files = glob.glob("*.py")

################################################################################
## Update Required by USER
################################################################################
textToSearch_1 = '#Test_Step_Prev = Calculate_PFT_Test_Step(1,Mon_TC,(Test_Step-1),0)'
textToSearch_2 = '#common.power_off(2)'
File_List_1 = []
File_List_2 = []
################################################################################
## END Of User Updates
################################################################################
for each_file in list_of_Files:
    if 'Find_String_In_Files' in each_file or 'SVN_Rev' in each_file:
        pass
    else:
        full_path = os.path.abspath(each_file)
        with open(full_path,'r+') as script_file:
            for line in script_file:
                if textToSearch_1 in line:
                    File_List_1.append(each_file)
                    break
                elif textToSearch_2 in line:
                    File_List_2.append(each_file)
                    break
        script_file.close()

print "File_List_1",File_List_1
print

print "File_List_2",File_List_2

   
    
    



