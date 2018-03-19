
import os
import pandas as pd
import numpy as np

cwd = os.getcwd()
filepath =cwd+"/graph.txt"
max_iteration=40
data = pd.read_csv(filepath, sep="\t", header=None)
data.columns = ["source", "destination"]
nodedegree=data.groupby(["source"]).size().reset_index(name='counts')
nodedegree["degree"]=1/nodedegree["counts"]
row,col=nodedegree.shape
M=data
M["value"]=1
M=M.pivot_table(index='destination', columns='source', values='value', fill_value=0)
for column in M:
    degree=nodedegree[(nodedegree["source"]==column)]["degree"].values[0]
    M[column]=M[column]*degree

pageRank= np.ones(row)*1/(row)
N=row

for num in range(max_iteration):
    pageRank= (( 0.8*(M*pageRank).sum(axis=1)) + (0.2/N))

print(pageRank)

pageRankIndex=np.argsort(pageRank)+1
print("List the top 5 node IDs with the highest PageRank scores.")
print(pageRankIndex[::-1] [:5] )

print("List the bottom 5 node IDs with the lowest PageRank scores")
print(pageRankIndex[:5] )
