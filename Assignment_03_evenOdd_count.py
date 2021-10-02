# Write a Python program to count the number of even and odd numbers from a series of numbers.

a=int(input("Enter range of number\n"))
evenCount=0
oddCount=0
for i in range(a):
    if i%2==0:
        evenCount+=1
    else:
        oddCount+=1

print("Number of even numbers: {} \n Number of odd numbers: {}".format(evenCount, oddCount))