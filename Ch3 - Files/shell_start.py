#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
import shutil
import zipfile
from os import path


def main():
    # make a duplicate of an existing file
    if path.exists("file.txt"):
        # get the path to the file in the current directory
        src = path.realpath("file.txt")

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"
        # now use the shell to make a copy of the file
        shutil.copy(src, dst)
        # rename the original file
        os.rename("file.txt", "newfile.txt")

        # now put all the things into a ZIP archive
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        with zipfile.ZipFile("testzip.zip", "w") as sip:
            sip.write("newfile.txt")
            sip.write("file.txt.bak")


if __name__ == "__main__":
    main()
