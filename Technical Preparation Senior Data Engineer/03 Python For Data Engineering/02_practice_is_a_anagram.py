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
    
    elif sorted(word_1.lower()) == sorted(word_2.lower()):

        return True

print(anagram("amor","amor"))


#all: it was my second attempt i have a error in the code so i use the last example