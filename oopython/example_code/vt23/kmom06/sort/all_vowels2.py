""" Showing recursion, find all vowels """


def all_vowels(str):
    if not str: # or str == ""
        return []
    res = all_vowels(str[1:])
    #print(res + [str[0]])
    if str[0] in 'aoueiy':
        # Add the vowel to the rest of the result
        return res + [str[0]]
    return res


#print(all_vowels("oopython")) # should be 4 ['o', 'o', 'y', 'o']
print(all_vowels("abcde")) # should be 2 ['e', 'a']