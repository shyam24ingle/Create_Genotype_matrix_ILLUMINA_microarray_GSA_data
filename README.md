# ILLUMINA microarray GSA data processing
# Create Genotype matrix format using map and ped file program

For further understanding of the file format, please refere to 
https://zzz.bwh.harvard.edu/plink/data.shtml#ped

Use python version 3.8 or above.

The python script "create_gn_matrix.py" is to used both the file, and convert into a genotype matrix format:

example :
x	IHP210010056	IHP210010404
1:103380393	GG	GG
1:109439680	AA	AA
1:110198788	AA	AA
1:110201112	CC	CC
1:110201667	GG	GG
1:110202904	AA	AA
1:110203240	CC	CC
1:110203911	GG	GG
1:110206675	AA	AA
1:110228436_CNV_GSTM1	--	--
1:110228505_CNV_GSTM1	--	--

Output will saved in genotype_matrix.txt file
note: Please refer log.txt for script execution logs
