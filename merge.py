#!/usr/bin/python

import glob,os
import sys

if len(sys.argv) >= 3:
	os.chdir(sys.argv[1])
	fastaapend=open(sys.argv[2], "w")
	for file in glob.glob("*.fasta"):
		fasta=open(file, "r")
		lines = fasta.readlines()
		seq="".join(lines)
		fastaapend.write(seq)
		fasta.close()
	fastaapend.close()
else:
        print "Workpath and file_out are needed";
