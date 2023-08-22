'''
Cast and input/output
'''

# Step 1
# Input
vehicle = "bil"
no_of_wheels = 4

# Type
print(type(vehicle))
print(type(no_of_wheels))

# Output
print(vehicle)
print(no_of_wheels)


# Step 2
print("\nLägg till inmatning")
# Input
vehicle = input("Vilket fordon? ")
no_of_wheels = input("Hur många hjul? ")

# Type
print(type(vehicle))
print(type(no_of_wheels))

# Output
print("En " + vehicle + " har " + no_of_wheels + " hjul.")


# Step 3
print("\nCasta variabeln no_of_wheels till int vid inmatning och skriv ut")
# Input
vehicle = input("Vilket fordon? ")
no_of_wheels = int(input("Hur många hjul? "))

# Type
print(type(vehicle))
print(type(no_of_wheels))

# Output
# Forget to cast no_of_wheels
print("En " + vehicle + " har " + no_of_wheels + " hjul.")
# Glöm inte att casta int till str vid utskrift!!!
#print("En " + vehicle + " har " + str(no_of_wheels) + " hjul.")
