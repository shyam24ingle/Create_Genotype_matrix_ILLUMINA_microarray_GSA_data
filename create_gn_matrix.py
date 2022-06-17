# ILLUMINA microarray GSA data processing
# Create Genotype matrix format using map and ped file program
# Indus Health Plus Python Assignment
# Python V3.9.0
# Author: Shyam Ingle
# Date: 17/06/2022
###################################################################
# File inputs

import sys
import argparse

if __name__ == '__main__':	
	parser = argparse.ArgumentParser(description='Genotype matrix format Programm')
	parser.add_argument("-m", "--map", help="map file name is required", required=True, action="store")
	parser.add_argument("-p", "--ped", help="ped file name is required", required=True, action="store")
	#parser.add_argument("-l", "--log", help="Log file name need to mention", required=True, action="store")
	args = parser.parse_args()

log = open("log.txt",'w')# log file 

if sys.argv[2].endswith('.map'):
	mapIN = open(sys.argv[2],'r').read() # map file name with extention argument
	log.write(sys.argv[2]+" is opened sucessfully!\n")
else:
	print("-m File is not map type!")
	log.write("-m File is not map type!\n")
	exit()
	
if sys.argv[4].endswith('.ped'):
	pedIN = open(sys.argv[4],'r').read() # ped file name with extention argument
	log.write(sys.argv[4]+" is opened sucessfully!\n")
else:
	print("-p File is not ped type!")
	log.write("-p File is not ped type!\n")
	exit()

###################################################################
#useful functions

def get_no_genotp(peddata):  # Get list of genotypes present in ped file for all samples
	gntpno = []
	for ln in peddata: gntpno.append(int(len(ln.split("\t")[6:])/2))
	return gntpno

def get_gentyp(pedln): # Get list of genotypes (biallelic SNP's) from ped file for single sample
	gentyp = []; k = 0
	gntp = pedln.split("\t")[6:]
	for g in range(int((len(gntp))/2)): gentyp.append(gntp[k]+gntp[k+1]);k=k+2; 
	return gentyp
	
def write_headers(pedln): # Make header for genotype matrix file
	headr = "x\t"
	for h in range(len(pedln)):headr = headr+(str(pedln[h].split("\t")[1])+'\t')
	return headr
	
#####################################################################
#Main code

snplist = mapIN[:-1].split("\n") # Get SNP entry lines from map file
pedsamp = pedIN[:-1].split("\n") # Get sample entry lines from ped file

nsnp = len(snplist) # Numbers of SNP's listed in map file

if nsnp not in get_no_genotp(pedsamp): # Ckeck no. of SNP's from map file and No. of genotypes in every samples in ped file
	print("Error: Gentype count not match with SNP's numbers in map file\nPlease check the PED file")
	log.write("Error: Genotype count not match with SNP's numbers in map file\nPlease check the PED file")
else:
	log.write("Total "+str(nsnp)+" Gentype matrix file is processed!\n")
	allsample = [] 
	GM = open("genotype_matrix.txt",'w') # Opening Genotype matrix file for writing
	GM.write(write_headers(pedsamp)+'\n')	# writing headers
	for i in range(len(pedsamp)): allsample.append(get_gentyp(pedsamp[i])); 
	for x, ln in enumerate(snplist): 
		snp = ln.split("\t")[1]; GM.write(str(snp))
		for i in range(len(pedsamp)): #writing genotypes to matrix file
			if '00' ==  str(allsample[i][x]): GM.write('\t--'); 
			else:GM.write('\t'+str(allsample[i][x])); 
		GM.write('\n')
	GM.close()
	log.write("Gentype matrix file is sucessfully created as genotype_matrix.txt\n")
	log.close()

#########################################################################