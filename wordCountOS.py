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

inputFile =  os.open(textFname, os.O_RDONLY)
line = os.read(inputFile, 50000).decode()
while(line != ""):
    # get rid of newline characters
    nline = line.strip()
    # remove capitalization
    nline = nline.lower()
    # split line punctuation
    # split line on whitespace
    words = re.split('[ \t '+ string.punctuation +' \n ]', nline)
    for word in words:
        if(word != ""):
            if word in master:
                master[word]+=1
            else:
                master[word]=1
    line=os.read(inputFile, 50000).decode()
os.close(inputFile)

keys = list(master.keys())
keys.sort()
master = {i: master[i] for i in keys}

outputFile = os.open(outputFname, os.O_WRONLY | os.O_CREAT)
for word in master:
    os.write(outputFile, (word + " "+ str(master[word])+"\n").encode())
os.close(outputFile)