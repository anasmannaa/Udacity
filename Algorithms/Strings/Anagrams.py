# Code

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other
    DON'T USE str1 == str2 in your code and find another way!

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here
    str1 = sorted(str1.replace(" ", "").lower())
    str2 = sorted(str2.replace(" ", "").lower())

    if len(str1) != len(str2):
        return False
    
    result = True
    
    for i in range(len(str1) - 1):
        if str1[i] != str2[i]:
            result = False
            break
    return result

    pass
 
# Test Cases

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
