import os
from shutil import copyfile
import shutil

# C:\Users\ACarr\Desktop\200912_Hochzeit_Lydia_Nico\04_Paarfotos\02_Steg\Andere\jpg_ohne_edit
MAINFODLER = "C:\\Users\\ACarr\\Desktop\\210827_Tina_Jess_Hochzeit"
#MAINFODLER = "C:\\Users\\ACarr\\Desktop\\200831_ReseTim_Rafael_Leipzig\\Sony"
SUBFOLDER = "\\00_Hinfahrt"
#SUBFOLDER = ""
PREFIX = "_DSC"
SUFFIX = ".ARW"
SUFFIX = ".JPG"

if SUFFIX == ".JPG":

    SOURCE_RELPATH = "\\Andere\\jpg_ohne_edit"
    #SOURCE_RELPATH = "\\andere_jpg"
    TARGET_RELPATH = "\\Auswahl_Alex\\jpg_ohne_edit"
    #TARGET_RELPATH = "\\selection_jpg"

else:
    SOURCE_RELPATH = "\\Andere\\raw"
    #SOURCE_RELPATH = "\\others_raw"
    TARGET_RELPATH = "\\Auswahl_Alex\\raw"
    #TARGET_RELPATH = "\\selection_raw"

SELECTION_FILE_RELPATH = "\\Auswahl_Alex\\Auswahl.txt"
#SELECTION_FILE_RELPATH = "\\auswahl.txt"



# source_path = os.path.join(MAINFODLER, SUBFOLDER, SOURCE_RELPATH)
# target_path = os.path.join(MAINFODLER, SUBFOLDER, TARGET_RELPATH)
source_path = MAINFODLER +SUBFOLDER + SOURCE_RELPATH
target_path = MAINFODLER +SUBFOLDER + TARGET_RELPATH
def main():


   if not os.path.isdir(source_path):
       raise Exception("Sourcedirectory %s doesnt exist!" %source_path)

   if not os.path.isdir(target_path):
       os.mkdir(target_path)

   #with open(os.path.join(MAINFODLER, SUBFOLDER, SELECTION_FILE_RELPATH)) as fp:
   print(MAINFODLER + SUBFOLDER +SELECTION_FILE_RELPATH)
   with open(MAINFODLER + SUBFOLDER +SELECTION_FILE_RELPATH) as fp:
        Lines = fp.readlines()
        for line in Lines:
            print(line)

            line_content = line.strip()

            if "-" in line_content:
                low_up = line.split("-")
                for index in range(int(low_up[0]), int(low_up[1]) + 1):
                    move_file_from_id(str(index))
            else:
                move_file_from_id(line_content)


def move_file_from_id(id):
    filename = PREFIX + id + SUFFIX
    # source = os.path.join(source_path, filename)
    # target = os.path.join(target_path, filename)
    source = source_path + "\\" + filename
    target = target_path + "\\" + filename
    if not os.path.isfile(source):
        print("File *%s* does not exist!" % filename)
    else:
        print("Move file *%s*" %filename)
        shutil.move(source, target)


if __name__ == '__main__':
    main()

