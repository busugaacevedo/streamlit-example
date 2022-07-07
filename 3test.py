#!/usr/bin/python3

import pandas as pd
from itertools import product
num_aa = int(input("Enter the length of the peptides:\t"))
outfile = input("Name of the outputfile.txt:\n")

com = product(["A","G","I","L","P","V","F","W","Y","D","E","R","H","K","S","T","C","M","N","Q"], repeat=num_aa)
#com = combinations_with_replacement(["A","G","I"], num_aa)
#Print the list of combinations
peps_tmp = []
peps_end = []
smiles_pep = []
count = 0
count_list = []
for p in list(com):
    peps_tmp.append(p)
    for i in peps_tmp:
        s = ''.join(p)
    count += 1
    count_list.append(count)
    peps_end.append(s)
df = pd.DataFrame.from_dict({'PEPS':peps_end})
#df = pd.DataFrame.from_dict({'N°':count_list,'PEPS':peps_end})
df.to_csv(outfile,index=False,sep="\t")
df

