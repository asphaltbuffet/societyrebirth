#! /usr/bin/python
#filename manifest.py

import os

# temporarily archive manifest file
if os.path.isfile('server.manifest.old'):
	os.remove('server.manifest.old')
if os.path.isfile('server.manifest'):
	os.rename('server.manifest', 'server.manifest.old')

startpath = os.getcwd()
dirToList = ['config', 'mods', 'scripts']

outFile = open("server.manifest", "a")
	
for d in dirToList:
	for root, dirs, files in os.walk(os.path.join(startpath, d)):
		for file in files:
			outFile.write('.{}'.format(os.path.join(root, file).replace(startpath, '')))
			outFile.write('\n')
		
outFile.close()