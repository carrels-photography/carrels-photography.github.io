import os.path
from os import walk


def main():
    # path_structures = [
    #     ["..", "images", "nature"],
    #     ["..", "images", "people"],
    #     ["..", "images", "project"],
    #     ["..", "images", "morocco"],
    #     ["..", "images", "urban"],
    #     ["..", "images", "street", "colored"],
    #     ["..", "images", "street", "bnw"],
    #     ["..", "images", "kate_jan"],
    # ]
    path_structures = [
        ["..", "images", "kate_jan"]
    ]

    git_ignore_string = ["/00foto-colorlib", "/00iview452g"]
    git_cached_string = []

    for path_structure in path_structures:

        directory = os.path.join(*path_structure)
        directory2 = "/".join(path_structure[1:])
        directory3 = os.path.join(*path_structure[1:])
        image_files = getfiles(directory)

        image_files.reverse()
        # image_files = []
        #
        # os.chdir(directory)
        # for (dirpath, dirnames, filenames) in walk(directory):
        #     image_files.extend(filenames)
        #     break
        # print(image_files)
        # image_files = [os.path.join(directory, f) for f in image_files]  # add path to each file
        # print(image_files)
        # image_files.sort(key=lambda x: os.path.getmtime(x))
        # print(image_files)

        # print("Vor soriterung: %s" % len(image_files))
        # print(image_files)
        # os.chdir(directory2)
        # image_files.sort(key=lambda x: os.path.getmtime(x))
        # print("Nach sortierung: %s" % len(image_files))
        # print(image_files)
        filename = path_structure[-1] + "_html.txt"

        with open(os.path.join("..",filename), 'w') as f:
            for file in image_files:
                if file.endswith(".jpg") and not file.endswith("_med.jpg") and not file.endswith("_low.jpg"):
                    filename, file_extension = os.path.splitext(file)
                    line1 = "			<div class=\"p-item grid-sizer\"><a class=\"venobox\" href=\"%s/%s_med.jpg\">\n" % (
                        directory2, filename)
                    line2 = "				<img src=\"%s/%s_low.jpg\" alt=\"\"/></a></div>\n\n" % (directory2, filename)
                    f.write(line1)
                    f.write(line2)

                    git_ignore_string.append("%s/%s.jpg" %(directory2, filename))
                    git_cached_string.append("git rm --cached %s/%s.jpg" %(directory2, filename))

        # with open(os.path.join("..", ".gitignore"), 'w') as f:
        #     for item in git_ignore_string:
        #         f.write("%s\n" % item)
        #
        # with open(os.path.join("..", "git_cached_string.txt"), 'w') as f:
        #     for item in git_cached_string:
        #         f.write("%s\n" % item)


def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    # a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a


if __name__ == '__main__':
    main()