#! /usr/bin/python
#filename build_server.py

import os
import sys
import zipfile

z = zipfile.ZipFile('server.zip', 'w')
count = 0

# Open the file with filelist.
with open('server.manifest') as f:
	files = f.read().splitlines()
    # Iterate over the lines, each line represents a file name.
	for file in files:
		count = count + 1
		z.write(os.path.normpath(file), os.path.normpath(file), compress_type = zipfile.ZIP_DEFLATED)
z.close()

print('{} files compressed to server.zip'.format(count))