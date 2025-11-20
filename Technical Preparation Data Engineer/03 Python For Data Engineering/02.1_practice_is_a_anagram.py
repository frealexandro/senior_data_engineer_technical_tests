# /*
#  * Write a function that takes two words (Strings) and returns
#  * true or false (Bool) depending on whether they are anagrams or not.
#  * - An anagram consists of forming a word by rearranging ALL
#  *   the letters of another original word.
#  * - It is NOT necessary to check if both words exist.
#  * - Two identical words are not anagrams.
#  */


def anagram(word_1,word_2):
    
    if word_1.lower() == word_2.lower():
        return False

    if sorted(word_1.lower()) ==  sorted(word_2.lower()):
        
        return True 
    

value = anagram("amor","mora")

print(value)

#all: it was my second attempt i really complete the code by my own, practice all you needed , its a part of the process