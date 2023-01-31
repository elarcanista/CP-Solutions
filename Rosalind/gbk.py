from Bio import Entrez

genus = input()
date_from = input()
date_to = input()

Entrez.email = "aortega0703@gmail.com"
handle = Entrez.esearch(
    db="nucleotide", 
    term=f'(("{date_from}"[Publication Date] : "{date_to}"[Publication Date])) AND "{genus}"[Organism]')
record = Entrez.read(handle)
print(record["Count"])