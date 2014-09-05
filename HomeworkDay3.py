#!/usr/bin/env python

"""
Parse multiple FASTA records from stdin and print them
"""
import sys

from fasta import FASTAReader

       
reader = FASTAReader(sys.stdin)

sequence_output = []    
for sid, sequence in reader:
    sequence_output.append(sequence)

sort_sequences = sorted(sequence_output, key = len, reverse = True)

longest_sequences = sort_sequences[:100]

if "ATG" in longest_sequences:
    print longest_sequences


""" Someone else's way to do Rev Comp
#def ReverseComplement1(seq):
  #  seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
 #   return "".join([seq_dict[base] for base in reversed(seq)])

"""

#My thoughts for Rev Comp

rev_comp = longest_sequences.replace( "A:T" , "G:C" , "C:G" , "T:A")

print rev_comp

    
