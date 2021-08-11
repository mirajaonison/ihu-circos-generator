import pandas as pd
import math, csv, sys

max_size = 100
defaultZ = 20
defaultCol = "black"

def split_dataframe(df, chunk_size = 10000): 
    chunks = list()
    num_chunks = math.ceil(len(df) / chunk_size)
    for i in range(num_chunks):
        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
    return chunks

if __name__ == '__main__':
    data = pd.read_csv(sys.argv[1], sep="\t", header=None,names=["genes", "organisms"])
    # Get unique organisms and count number of genes
    groups = data.groupby("organisms")["genes"].count().reset_index()
    # Get minimum number of genes per group
    min_size = groups.min()["genes"]
    # Assign unit
    unit = min_size if min_size <= max_size else max_size
    group_increment = 1
    rows = []
    for index, df_row in data.iterrows(): 
            row = [index, df_row["organisms"]]
            rows.append(row)
    # Karyotype
    groups['genes'] = groups['genes'].transform(lambda subgroup: math.ceil(subgroup/unit))
    karyotypes = []
    links = []
    for index, group in groups.iterrows():
        row = ['chr', '-', group['organisms'], group['organisms'], 0, group['genes'], "color%s" % group['organisms'].lower()]
        karyotypes.append(row)
    groupstart = 1; groupend = 1; before = rows[0][1]
    for i,row in enumerate(rows):
        karyotype = ['chr', '-', row[0], row[0], 0, 1, "black"]
        karyotypes.append(karyotype)
        link = [row[0], 1, 1, row[1], groupstart, groupend, "color=color%s" % row[1].lower()]
        links.append(link)
        groupstart = 1 if before != row[1] else groupend
        groupend = 1 if before != row[1] else (groupend + 1)
        before = row[1]
    with open("karyotype.txt", "w") as karyotypehandle:
        writer = csv.writer(karyotypehandle, delimiter=' ')
        writer.writerows(karyotypes)
    with open("links.txt", "w") as linkshandle:
        writer = csv.writer(linkshandle, delimiter=' ')
        writer.writerows(links)



