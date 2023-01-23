""" Showing recursion, find all vowels """


def all_vowels(str):
    if not str: # or str == ""
        return []
    res = all_vowels(str[1:])
    if str[0] in ['a','o','u','e','i','y']:
        # Add the vowel to the rest of the result
        return res + [str[0]]
    return res


#print(all_vowels("oopython")) # should be 4
print(all_vowels("abcde")) # should be 2