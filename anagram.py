#CONFIRMING ANAGRAM
def confirmAnagram(firstWord, secondWord):
    
    if (len(firstWord) == len(secondWord)):
        string1 = sorted(firstWord)
        string2 = sorted(secondWord)

        if (string1 == string2):
            print('True') # This is going to return True, if the condition is met
            print("%s and %s" % (firstWord, secondWord) + " are anagrams \n")
        else:
            print("False") # This is going to return False, if the condition is not met
            print("%s and %s" % (firstWord, secondWord) + " are not anagrams \n")
    else:
        print( "Number of letters are not the same" )

confirmAnagram("secure", "rescue" )