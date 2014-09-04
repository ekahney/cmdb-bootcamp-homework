#!/usr/bin/env python


blast_out = "/Users/cmdb/data/day3/blastout"

f = open(blast_out)
line = f.readline()


while True:
    line = f.readline()
    if line == "":
        break
    elif "Identities" in line:
        print line  
    elif ">" in line or line.startswith("Query="):
        sequence_name = str([line.rstrip("\r\n").split("/t")[0]])
        print sequence_name


