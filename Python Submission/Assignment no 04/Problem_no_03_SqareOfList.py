# Write a Python program to square the elements of a list using map() function.ls=list(range(1,11))

ls=list(range(1,11))

squared_ls=list(map(lambda x:x*x,ls))

print(squared_ls)