from os import listdir
from os.path import isfile, join
from shutil import copyfile



source_path= r"C:\Users\ACarr\Desktop\190706_Hochzeit_KatrinJan\backup4"
target_path= r'C:\Users\ACarr\Desktop\190706_Hochzeit_KatrinJan\Auswahl'

sourcefiles = [f for f in listdir(source_path) if isfile(join(source_path, f))]

print(sourcefiles)


targetfiles = [f for f in listdir(target_path) if isfile(join(source_path, f))]

print(targetfiles)

jpgs_in_target = [f for f in targetfiles if f.lower().endswith('jpg')]
raws_in_source = [f for f in sourcefiles if f.lower().endswith('raf')]

jpg_names = set([f[:-4] for f in jpgs_in_target])
raw_names = set([f[:-4] for f in raws_in_source])

print(jpg_names)
print(raw_names)

common_names = jpg_names & raw_names

print(common_names)

for file in common_names:
    filename = file + '.RAF'
    source = join(source_path, filename)
    if not isfile(source):
        print('ACHTUNG: File %s existiert nicht in Source!!', source)
        continue

    dest = join(target_path, filename)
    if isfile(dest):
        print('ACHTUNG: File %s existiert bereits in dest!!', dest)
        continue

    print('File wird kopiert!')
    copyfile(source, dest)

print('Kopiervorgang abgeschlossen!')

