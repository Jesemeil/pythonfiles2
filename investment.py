a = "Deposit amount at the end of the nth year" 
p = 1000 # Principal
r = 0.07 # Annual rate of return
n1 = 10 # Number of years

a = p * (1 + r) ** n1
print("The deposit amount after 10 years: $" + format(a, ".2f"))

n2 = 20
a = p * (1 + r) ** n2
print("The deposit amount after 20 years: $" + format(a, ".2f"))


n3 = 30
a = p * (1 + r) ** n3
print("The deposit amount after 30 years: $" + format(a, ".2f"))
