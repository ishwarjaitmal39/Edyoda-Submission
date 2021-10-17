def upper_lower_count(a):
    lowerCount = 0
    upperCount = 0
    for i in a:
        if i.isupper():
            upperCount+=1
        if i.islower():
            lowerCount+=1
    print(f"No of UpperCase character: {upperCount}\nNo of LowerCase character: {lowerCount}")


str1=input("Enter string here\n")
upper_lower_count(str1)