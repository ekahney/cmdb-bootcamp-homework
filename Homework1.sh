#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX=SRR0729
dmel5=/Users/cmdb/data/day1/dmel_r5.57_FB2014_03/gff/dmel-all-r5.57-removeFASTA.gff
GENOME_DIR=/Users/cmdb/data/genomes

ANNOTATION=dmel-all-r5.57.gff

CORES=4

for i in 24 {1..16}
do
	echo unzip $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz
	echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
    echo tophat $dmel5 $ANNOTATION $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
    echo cufflinks $dmel5 $ANNOTATION $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
done
