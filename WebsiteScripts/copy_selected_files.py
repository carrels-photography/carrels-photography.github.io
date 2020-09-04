import os
from shutil import copyfile


MAINFODLER = r"C:\Users\ACarr\Desktop\200831_ReseTim_Rafael_Leipzig\Sony\ich"

SOURCE_RELPATH = ""

TARGET_RELPATH = "auswahl"

SELECTION_FILE_RELPATH = "auswahl.txt"

PREFIX = "_DSC"

SUFFIX = ".ARW"
#SUFFIX = ".JPG"

source_path = os.path.join(MAINFODLER, SOURCE_RELPATH)
target_path = os.path.join(MAINFODLER, TARGET_RELPATH)

def main():


   if not os.path.isdir(source_path):
       raise Exception("Sourcedirectory doesnt exist!")

   if not os.path.isdir(target_path):
       os.mkdir(target_path)

   with open(os.path.join(MAINFODLER, SELECTION_FILE_RELPATH)) as fp:
        Lines = fp.readlines()
        for line in Lines:

            line_content = line.strip()

            if "-" in line_content:
                low_up = line.split("-")
                for index in range(int(low_up[0]), int(low_up[1]) + 1):
                    copy_file_from_id(str(index))
            else:
                copy_file_from_id(line_content)


def copy_file_from_id(id):
    filename = PREFIX + id + SUFFIX
    source = os.path.join(source_path, filename)
    target = os.path.join(target_path, filename)
    print("Copy file *%s*" %filename)
    copyfile(source, target)


if __name__ == '__main__':
    main()

