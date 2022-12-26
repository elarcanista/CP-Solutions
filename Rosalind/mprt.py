import sys
import re
import requests
import urllib

motif = re.compile("N[^P][ST][^P]")

def find(protein):
    ans = []
    last = 0
    result = motif.search(protein)
    while result != None:
        last = result.start() + 1
        ans.append(last)
        result = motif.search(protein, last)
    return ans

for ID in sys.stdin:
    data = requests.get(f"http://www.uniprot.org/uniprot/{ID[:6]}.fasta").text.splitlines()
    protein = ""
    for line in data[1:]:
        protein += line
    ans = find(protein)
    if len(ans) != 0:
        print(ID.strip())
        print(*ans)