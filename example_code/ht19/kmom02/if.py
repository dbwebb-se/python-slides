num_one = int(input("Skriv en siffra: "))
num_two = int(input("Skriv ytterligare en siffra: "))

message = "Rejected"
if num_one > 10 and num_one < 100 and num_two > 10 and num_two < 100:
    if num_one < 50 or num_two < 50:
        if num_two > 40 or num_two > 40:
            message = "Accepted"

print(message)
