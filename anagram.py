#CONFIRMING ANAGRAM
def confirmAnagram(firstWord, secondWord):
    if (len(firstWord) == len(secondWord)):
        string1 = sorted(firstWord)
        string2 = sorted(secondWord)

        if (string1 == string2):
            print('True') # This is going to return True, if the condition is met
        else:
            print("False") # This is going to return False, if the condition is met
    else:
        print( "%s and %s" % (firstWord, secondWord) + " are not anagram \n" )

confirmAnagram("secure", "rescue")