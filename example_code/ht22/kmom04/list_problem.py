"""
Skriv en funktion som tar emot en lista som innehåller heltal och en (1) nivå av nestlade listor, 
även dessa med heltal.

Iterera igenom listan och summera alla siffror i förälder listan. Varje gång du stöter på en barn 
lista summera siffrorna i denna och skriv ut barnlistans summa. Addera barnlistornas summa till 
förälderlistans totala summa.

Listor att testa med:

[1, 2, 3, 4]
[1, 2, [6, 7, 8], 5, 7, 9]
[[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2]
"""

def list_sum(a_list) :
    """ Sum numbers in list and return the sum """
    res = 0
    for item in a_list:
        if isinstance(item, int):
            res += item
        elif isinstance(item, list):
            res += list_sum(item)
    
    return res

if __name__ == "__main__":
    result = list_sum(['1', 2, 3, 4])
    print("Summan är " + str(result))
    result = list_sum([1, 2, [6, 7, 8], 5, 7, 9])
    print("Summan är " + str(result))
    result = list_sum([[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2])
    print("Summan är " + str(result))
    result = list_sum(['1', 2, 3, 4])
    print("Summan är " + str(result))
    result = list_sum([1, 2, [6, 7, [1, 2]], 5, 7, 9])
    print("Summan är " + str(result))
    