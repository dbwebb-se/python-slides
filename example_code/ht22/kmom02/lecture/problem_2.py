"""
Skriv ett program som beräknar sparande.
Input: startkapital, ränta och slutvärde
Output: antal år
"""

# Input or assign
capital = 1000
interest = 5
goal = 1200

# Calculation, new_value = old_value * (1 + interest / 100)
new_capital = capital *  (1 + interest / 100)

# Output
print("Du har " + str(capital) + " kr på kontot.")
print("Med ränta har du " + str(new_capital) + " kr på kontot.")
