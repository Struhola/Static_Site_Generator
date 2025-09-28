#./main.sh

import os
import shutil
import sys
from file_operations import copy_contents


dir_path_static = "./static"
dir_path_public = "./public"
#"./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if not os.path.exists(dir_path_static):
        raise Exception(f"Source {dir_path_static} doesn't exists")

    if os.path.exists(dir_path_public):
        print(f"Destination {dir_path_public} already exists - REMOVING")
        shutil.rmtree(dir_path_public)

    copy_contents(dir_path_static, dir_path_public)

if __name__ == "__main__":
    main()