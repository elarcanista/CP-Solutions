import Bio.Seq

A = input()
B = input()

i = 0
C = ""
while not B == C:
    try:
        i += 1
        C = Bio.Seq.translate(A, table=i, stop_symbol='', to_stop=False)
    except:
        pass
print(i)

