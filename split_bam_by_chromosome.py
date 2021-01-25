#!/usr/bin/env python3


import os, sys

inputseqids = sys.argv[1]
with open(inputseqids, 'r') as inputfile:
	seqids = inputfile.read().splitlines()


# read from stdin now

for line in sys.stdin:
	line=line.strip()
	if line.startswith("@SQ"):
		line_seqid = line.split()[1].replace("SN:", "")
		if line_seqid in seqids:
			print(line)
		else:
			pass
	elif not line.startswith("@"):
		data = line.split()
		if data[2] in seqids:
			print(line)
	else:
		print(line)

exit(0)
