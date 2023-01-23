""" Showing recursion, find all vowels """


def all_vowels(str):
    if not str: # or str == ""
        return []
    print(str[0])
    return all_vowels(str[1:])

  
print(all_vowels("oopython")) # should be 4