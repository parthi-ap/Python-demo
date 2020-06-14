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
textToSearch = 'Engage_Logic_Check_Test_Dict_Cat_4.csv'
textToReplace = 'PFT_Engage_Logic_Check_Test_Dict_2_Table.csv'

################################################################################
## END Of User Updates
################################################################################
for each_file in list_of_Files:
    if 'Replace_String_In_Files' in each_file or 'SVN_Rev' in each_file:
        pass
    else:
        full_path = os.path.abspath(each_file)
        fh, abs_path = tempfile.mkstemp()
        tempFile = open(abs_path,'w')
        with open(full_path,'r+') as script_file:
            for line in script_file:
                if textToSearch in line:
                    line=string.replace(line,textToSearch,textToReplace)
                    tempFile.write(line)
                    print each_file
                    print "Successfully Replaced"
                else:
                    tempFile.write(line)
        tempFile.close()
        script_file.close()
        os.close(fh)
        os.remove(full_path)
        os.rename(abs_path, full_path)


   
    
    



