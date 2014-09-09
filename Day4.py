#!/usr/bin/env python

gtf_file = "/Users/cmdb/data/SRR072893_cufflinks_output/transcripts.gtf"




f = open(gtf_file)
line = f.readline() 



pos_transcript_start = []               
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
   # print fields[0], fields[3], fields [4], fields[6]
    if "+" in line:
        pos_transcipt_start = fields[3]
      #  print pos_transcipt_start



      

    
    #to use bedtools flank you need to make a genome folder with choromosome name and size columns. and thats it.
   



     
    