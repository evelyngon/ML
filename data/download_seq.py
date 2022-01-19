#! usr/bin/env python3
# Download Biological Sequences from NCBI using Python
# Load the biopython Entrez module
from Bio import Entrez
# Load biopython SeqIO module
from Bio import SeqIO
# Set your email
Entrez.email="evelyngon@gmail.com"
import sys
# id=unique or multiple identifiers or Accession Numbers for db=protein
# db=protein
# outputformat=multifasta
# displaymode=text
arg=sys.argv[1]
try:
    with open(arg,'r') as infile:
        readline=infile.read().splitlines()
        id_list=list(readline)
except FileNotFoundError:
    print ("The file {arg} does not exist, try a different file")
    raise (SystemExit)

handle=Entrez.efetch(db="protein", id=id_list, rettype="fasta", retmode="text")
record=SeqIO.parse(handle, 'fasta')
outputname='/home/evelyn/ncbi-multibeta-lactam.txt'
SeqIO.write(record, outputname, 'fasta')






