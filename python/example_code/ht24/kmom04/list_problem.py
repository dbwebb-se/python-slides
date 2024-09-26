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

def sublist_sum(sublist):
    """ Sum numbers in list and return the sum """
    return sum(sublist)

def list_sum_old(a_list):
    """ Sum numbers in list and return the sum """
    res = 0
    for item in a_list:
        res += item
   
    return res

def list_sum(a_list) :
    """ Sum numbers in list and return the sum """
    res = 0
    for item in a_list:
        if isinstance(item, int):
            res += item
        elif isinstance(item, list):
            res += sublist_sum(item)
    
    return res

def list_sum2(a_list) :
    """ Sum numbers in list and return the sum """
    res = 0
    for item in a_list:
        if isinstance(item, int):
            res += item
        elif isinstance(item, list):
            res += list_sum2(item)
    
    return res

if __name__ == "__main__":
    print("Listor")
    result = list_sum([1, 2, 3, 4])
    #result = sublist_sum([1, 2, 3, 4])
    print("Summan är " + str(result)) # 10
    result = list_sum(['1', 2, 3, 4])
    print("Summan är " + str(result)) # 9
    result = list_sum([])
    print("Summan är " + str(result)) # 0
    
    print("Listor med underlistor")
    result = list_sum([1, 2, [6, 7, 8], 5, 7, 9])
    print("Summan är " + str(result)) # 45
    result = list_sum([1, 2, [], 5, 7, 9])
    print("Summan är " + str(result)) # 24
    result = list_sum([[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2])
    print("Summan är " + str(result)) # 76
    result = list_sum2([1, 2, [6, 7, [1, 2]], 5, 7, 9])
    print("Summan är " + str(result)) # 40
    