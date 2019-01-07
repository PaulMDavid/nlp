#!/usr/bin/env python
from os import listdir
from os.path import isfile, join
onlyfiles=[]
i=1
maypath="/home/ai11/nlp/day03/New/Assignment 3"
for f in listdir(maypath):
 mypath="/home/ai11/nlp/day03/New/Assignment 3/C0"+str(i)
 onlyfiles.append(str(i))
 print
 if i==11:
  break
 i+=1
 onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# for fil in onlyfiles:
#  d=onlyfiles.open(fil)
#  traindata.append(d)

print len(onlyfiles)
 
