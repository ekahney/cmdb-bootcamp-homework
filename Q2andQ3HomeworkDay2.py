#!/usr/bin/env python

##1.	Extract Sxl expression for female 10/11/12/13/14A/14B/14C/14D
##HINT: create a file called samples.csv containing this metadata to use in a for loop
##sample,sex,stage SRR072893,male,10 SRR072894,male,11 SRR072895,male,12 SRR072896,male,13 ##SRR072897,male,14A SRR072899,male,14B SRR072901,male,14C SRR072903,male,14D ##SRR072905,female,10 SRR072906,female,11 SRR072907,female,12 SRR072908,female,13 ##SRR072909,female,14A SRR072911,female,14B SRR072913,female,14C SRR072915,female,14D
##--> Save dataframe with FPKM for all samples to a TSV file



import pandas as pd

import matplotlib.pyplot as plt

cufflinks_output1 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
cufflinks_output3 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
cufflinks_output4 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
cufflinks_output5 = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
cufflinks_output6 = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
cufflinks_output7 = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
cufflinks_output8 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

all_files = [cufflinks_output1, cufflinks_output2, cufflinks_output3, cufflinks_output4, cufflinks_output5, cufflinks_output6, cufflinks_output7, cufflinks_output8]

for i in all_files:
    f = open (i)
    line = f.readline()
    while True:
        line = f.readline()
        if "Sxl" in line:
            #print line
            fields = line.rstrip("\r\n").split("\t")
            #print fields[9]
            break
         
fields[9] = 35.519, 16.3992, 20.2589, 7.02107, 125.473, 120.963, 342.875, 348.442   
plt.figure()
plt.plot(fields[9])
plt.savefig("Sxl.png")
        


    