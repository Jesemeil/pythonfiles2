age = int(input("Enter your age in years: "))
maximum_heart_rate = 220 - age


min_target_heart_rate = 0.5 * maximum_heart_rate 
max_target_heart_rate = 0.85 * maximum_heart_rate

print (" Your maximum heart rate in beats per minute is: ", maximum_heart_rate) 
print (" Your target heart range is: " +  str(min_target_heart_rate) + " to " + format(max_target_heart_rate, ".2f")+ " beats per minute ")

