import pysvn
import glob
import xlwt
import xlrd
import csv
import os
import tempfile
import string

client = pysvn.Client()
## Before Running remove READ ONLY
from xlrd import open_workbook

xl_book = open_workbook('_Rename_Files_Automation.xlsx')

xl_sheet = xl_book.sheet_by_index(0)

textToSearch = "L1-MRJ-DTP-"

num_cols = xl_sheet.ncols
num_rows = xl_sheet.nrows

for row_idx in range(1,num_rows):
    old_name = xl_sheet.cell(row_idx, 0).value
    print "Old_Name",old_name
    new_name = xl_sheet.cell(row_idx, 1).value
    print "New_Name",new_name
##    os.rename(old_name,new_name)
    client.move(old_name,new_name)

    full_path = os.path.abspath(new_name)
    fh, abs_path = tempfile.mkstemp()
    tempFile = open(abs_path,'w')
    with open(new_name,'r+') as script_file:
        for line in script_file:
            if old_name in line:
                line=string.replace(line,old_name,new_name)
                tempFile.write(line)
                print new_name
                print "Successfully Replaced"
            else:
                tempFile.write(line)
    tempFile.close()
    script_file.close()
    os.close(fh)
    os.remove(full_path)
    os.rename(abs_path, full_path)
        
