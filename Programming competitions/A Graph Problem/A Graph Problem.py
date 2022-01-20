#!/usr/bin/env python
# coding: utf-8

# # 11069 - A Graph Problem
# 
# Given an undirected graph of the following form with n nodes, 1 <= n <= 76:
# 
# <img src="graph.PNG" width=500/>
# 
# Your task is to calculate the number of subsets of nodes of the graph with the following properties:
# 
# - no nodes in the subset should be connected
# - it shouldn’t be possible to add further nodes to the subset without violating the first condition
# 
# 
# For a graph with 5 nodes the number of subsets which fulfill the above conditions is 4. The subsets are {1,3,5},{2,4},{2,5},{1,4}.
# 
# ---
# 
# ### Input
# The input will consist of a sequence of numbers n, 1 <= n <= 76. Each number will be on a separate line. The input will be terminated by EOF.
# 
# ### Output
# Output the number of subsets as described above on a single line. The number of all subsets will be less than 2^31.
# 
# #### Sample Input
# 1
# 
# 2
# 
# 3
# 
# 4
# 
# 5
# 
# 30
# 
# #### Sample Output
# 1
# 
# 2
# 
# 2
# 
# 3
# 
# 4
# 
# 4410

# In[ ]:


table = [0, 1, 2, 2]
L = 77
for i in range(0,L):
    table.append(table[-2] + table[-3])

while 1:
    try:
        n = int(input())
        print(table[n])
    except(EOFError):
        break


# In[ ]:




