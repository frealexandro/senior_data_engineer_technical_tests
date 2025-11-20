# /*
#  * Write a function that takes two words (Strings) and returns
#  * true or false (Bool) depending on whether they are anagrams or not.
#  * - An anagram consists of forming a word by rearranging ALL
#  *   the letters of another original word.
#  * - It is NOT necessary to check if both words exist.
#  * - Two identical words are not anagrams.
#  */


def angrama (palabra_1,palabra_2):

    if palabra_1.lower() == palabra_2.lower():
        return False
    
    return sorted(palabra_1.lower()) == sorted(palabra_2.lower())



anagram_w =angrama("hola" , "haloja")

print(anagram_w)


#all: it was my fist attempt i use chat gpt to solve a part