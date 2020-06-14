
import glob
import xlwt
import xlrd
from natsort import natsorted, ns

wbk = xlwt.Workbook()
## worksheet "DTP-Proposed View"
sheet = wbk.add_sheet('File_Names')
print("*"*80)
print("Reading all File Names")
print("*"*80)
## To get list of all files in folder
list_of_Files = glob.glob("*.*")

row_no = 1
row_no_sheet1 = 1

file_list=[]
for each_file in list_of_Files:
    file_list.append(each_file)

file_list=natsorted(file_list, alg=ns.IGNORECASE)

for each_file in file_list:
    sheet.write(row_no,0,each_file) ## Write File name
    row_no+=1

wbk.save("List_Of_Files.xls")
print("*"*80)
print("List_Of_Files.xls saved")
print("*"*80)
###################################################
###################################################
