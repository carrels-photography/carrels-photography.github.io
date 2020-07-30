import os
from shutil import copyfile


MAINFODLER = r"C:\Users\ACarr\Desktop\299723_eisbach_surf_kris"

SOURCE_RELPATH = ""

TARGET_RELPATH = "selection2"

SELECTION_FILE_RELPATH = "selection.txt"

PREFIX = "_DSC"

SUFFIX = ".ARW"
#SUFFIX = ".JPG"


def main():
   source_path = os.path.join(MAINFODLER, SOURCE_RELPATH)
   target_path = os.path.join(MAINFODLER, TARGET_RELPATH)

   if not os.path.isdir(source_path):
       raise Exception("Sourcedirectory doesnt exist!")

   if not os.path.isdir(target_path):
       os.mkdir(target_path)

   with open(os.path.join(MAINFODLER, SELECTION_FILE_RELPATH)) as fp:
        Lines = fp.readlines()
        for line in Lines:
            id = line.strip()
            filename = PREFIX + id + SUFFIX

            source = os.path.join(source_path, filename)
            target = os.path.join(target_path, filename)

            copyfile(source, target)




if __name__ == '__main__':
    main()

