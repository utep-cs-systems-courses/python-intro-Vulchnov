#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import string   

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

master={}

#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()

with open(textFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # remove capitalization
        line = line.lower()
        # split line punctuation
        # split line on whitespace
        words = re.split('[ \t '+ string.punctuation +']', line)
        for word in words:
            if(word != ""):
                if word in master:
                    master[word]+=1
                else:
                    master[word]=1

keys = list(master.keys())
keys.sort()
master = {i: master[i] for i in keys}

with open(outputFname, 'w') as outputFile:
    for word in master:
        outputFile.write((word + " "+ str(master[word])+"\n"))
