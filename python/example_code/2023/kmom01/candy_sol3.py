'''
Uppgift 1
'''

# Input, get allowance and cost_of_candy
allowance = input("Vad är din månadspeng? ")
cost_of_candy = input("Hur mycket handlar du godis för? ")

# Calculation
print(type(allowance))
left_of_allowance = allowance - cost_of_candy


# Output, print out what is left of allowance
print("Du har " + left_of_allowance + " kr kvar av din månadspeng.")
