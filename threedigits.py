num = int(input("Enter a three-digit integer: "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10


print(digit1, digit2, digit3, sep="   ")

