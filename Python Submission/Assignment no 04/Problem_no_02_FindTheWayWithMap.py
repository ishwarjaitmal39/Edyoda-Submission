# Write a Python program to triple all numbers of a given list of integers. Use Python map.

ls=list(range(1,11))

triple_ls=list(map(lambda x:x*3,ls))

print(triple_ls)