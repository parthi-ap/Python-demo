## Program to extract files from all .zip archives in a folder
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
import zipfile  


Folders_List = []
list_of_Files = []

DEST_PATH = os.getcwd()
print DEST_PATH

Folders_List.append(DEST_PATH)
sub_folders = next(os.walk(DEST_PATH))[1]

for each_folder in sub_folders:
    if('.svn' in each_folder):
        pass
    else:
        Folders_List.append(DEST_PATH + "\\" + each_folder)


for idx,path in enumerate(Folders_List):
    each_list=[]
    csv_list=[]
    main_list=[]


    for fname in os.listdir(path):
        path1 = os.path.join(path, fname)

        
        if ('.zip' in path1):

            with zipfile.ZipFile(path1,"r") as zip_ref:

                try:
                    
                    zip_ref.extractall()

                    print path1 +"-- EXTRACTED"

                    path2 =path1.replace(".zip","")

                   
                except Exception as inst:
                    print type(inst)
                    print inst.args
                    print inst
                    print path1 +"-- NOT EXTRACTED"
                    pass

        extension = '.csv'

        try :
            
            for root, dirs_list, files_list in os.walk(os.getcwd()):
                for file_name in files_list:
##                    print file_name
                    if os.path.splitext(file_name)[-1] == extension:
                        file_name_path = os.path.join(root, file_name)
    ##                    print file_name
                        os.remove(file_name_path)    

     
        except Exception as inst1:
##            print type(inst1)
##            print inst1.args
##            print inst1
            pass
                

''' Future work   
    for each in files:
       each_list.append(each)

       print each

    print each_list
    
    for each_file in each_list:
        if('SVN_Rev' in each_file):
            pass
        elif('Support_' in each_file or 'support_' in each_file):
            support_script_list.append(each_file)
        elif('.csv' in each_file):
            csv_list.append(each_file)
        elif('.zip' in each_file):
            print each_file
            print os.getcwd()
            with zipfile.ZipFile(each_file,"r") as zip_ref:
                zip_ref.extract()
'''
