cmdb-bootcamp-homework
======================

Basic Exercises

1. How many lines are there?
        HINT: wc 
13564834 153048099 2662919684

2. How many lines deal with the gene Sxl?
        HINT: grep option 
696

3. How many types of features are there?
        HINT: column 3 cut sort uniq
18

4. How many of each feature type are there
        HINT: uniq option
78 CDS
  26 RNAi_reagent
  12 TSS
  30 exon
  40 five_prime_UTR
   1 gene
  37 intron
  24 mRNA
  62 match
 256 match_part
   1 modified_RNA_base_feature
  29 orthologous_to
   2 point_mutation
  24 protein
   3 protein_binding_site
   1 regulatory_region
  52 three_prime_UTR
  18 transposable_element_insertion_site


5. Push the results from #4 to your Github repository
        HINT: use '>' to redirect output to a new file