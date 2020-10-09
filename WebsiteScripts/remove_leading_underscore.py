from os import listdir, rename
from os.path import isfile, join, isdir

# C:\Users\ACarr\Desktop\200912_Hochzeit_Lydia_Nico\04_Paarfotos\02_Steg\Andere\jpg_ohne_edit
MAINFODLER = r"C:\Users\ACarr\Desktop\homepage_201009"

def main():


   if not isdir(MAINFODLER):
       raise Exception("Sourcedirectory %s doesnt exist!" %MAINFODLER)

   allfiles = [f for f in listdir(MAINFODLER) if isfile(join(MAINFODLER, f))]
   print(allfiles)
   with_underscore = [f for f in allfiles if f.startswith("_")]
   print(with_underscore)

   for file in with_underscore:
       without_underscore = file.lstrip("_")
       rename(join(MAINFODLER, file), join(MAINFODLER, without_underscore))


if __name__ == '__main__':
    main()

