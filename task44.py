# -*- coding: utf-8
# Программа вызывается с входным параметром - путем к директории.
# Необходимо протестировать на целостность все архивы, содержащиеся 
# в директории.

import os
import sys
import subprocess

def print_result(cmd, filename):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	out, err = p.communicate()
	if p.returncode != 0:
		print("File %s is not OK!" % filename)
	else:				
		print("File %s is OK." % filename)


def test_archives(path):
	if not os.path.isdir(path) or not os.path.exists(path):
		print("Incorrect path!")
		return
	files = os.listdir(path)
	for file in files:
		file_ext = os.path.splitext(file)[1]
		if file_ext == ".zip":
			_path = os.path.join(path, file)
			cmd = ["unzip", "-t", _path]
			print_result(cmd, file)
		elif file_ext == ".rar":
			_path = os.path.join(path, file)
			cmd = ["unrar", "t", _path]
			print_result(cmd, file)

if len(sys.argv) != 2:
	print("Please, enter the directory in parameters.")
else:
	_path = os.path.normpath(sys.argv[1])
	test_archives(_path)