import subprocess, sys
from os import walk, path
from config import PATHS
from typing import Literal
import re

def get_all_files() -> str:
	files_arr = []
	for _path in PATHS.values():
		for (dirpath, dirnames, filenames) in walk(_path):
			for file in filenames:
				relative_path = path.join(dirpath, file)
				files_arr.append(f'--add-data={relative_path};{dirpath}')
				
	return " ".join(files_arr)

def build() -> None:
	files = get_all_files()
	subprocess.run(f"pyinstaller --onefile --windowed {files} __main__.py")
	if sys.argv[1] == "--run":
		subprocess.run(f"dist/__main__.exe")

build()