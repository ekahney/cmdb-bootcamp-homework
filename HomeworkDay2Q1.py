#!/usr/bin/env python


## 	1.	Make boxplot of top/middle/bottom 1/3rd FPKMs -- for SRR072893, SRR072915
##HINT: pass plt.boxplot() a 3-element list

import pandas as pd

import matplotlib.pyplot as plt

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"

df = pd.read_table(cufflinks_output)

df = df.sort("FPKM")

bottom = df["FPKM"] [0:5021]
middle = df["FPKM"] [5201:10402]
top = df["FPKM"] [10402:15603]

list_boxplot = bottom, middle, top

plt.boxplot(list_boxplot)

plt.savefig("box893.png")


cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 = pd.read_table(cufflinks_output2)

df2 = pd.read_table(cufflinks_output2)

df2 = df2.sort("FPKM")

bottom = df2["FPKM"] [0:5021]
middle = df2["FPKM"] [5201:10402]
top = df2["FPKM"] [10402:15603]

list_boxplot = bottom, middle, top

plt.boxplot(list_boxplot)

plt.savefig("box915.png")

#plt.figure()
