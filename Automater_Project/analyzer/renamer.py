import os
import pathlib

this_directory = pathlib.Path(__file__).parent.absolute()
for _, dirs, _ in os.walk(this_directory):
	for dir in dirs:
		end_num = dir.split("Use_Case")[1]
		print(end_num)
		os.rename(dir, "use_case_"+end_num)