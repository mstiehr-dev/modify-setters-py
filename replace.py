#!/usr/bin/env python3

import re
import sys

#find . -type f -name TG*Form.java | xargs python3 /cygdrive/c/Temp/regex/regex.py


def replace(filename):
	print("start processing " + filename)
	f = open(filename, "r")
	text = f.read()
	f.close()
	
	pattern = re.compile(r"(?P<indent>\s*)(?P<signature>(\w|\s|\d|[\(\)])*{\s*)(?P<assignment>this(.)(\w|\d)* = )StringUtils.trimToNull\((?P<arg2>(\w|\s)*)\);")
	hits = len(re.findall(pattern, text))
	if hits > 0:
		out = re.sub(pattern, r"\g<indent>\g<signature>\g<assignment>\g<arg2>;", text)
		f = open(filename, "w")
		f.write(out)
		f.close()
	
	print("done with " + filename + " / found " + str(hits) + " hits")

if __name__ == "__main__":
	for arg in sys.argv:
		replace(arg)
	print("finished")
