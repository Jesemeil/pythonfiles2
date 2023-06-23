num= int(input("Enter yur score: "))
if num >= 0:
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number") 
else: 
    print(num, "is a negative number") 
