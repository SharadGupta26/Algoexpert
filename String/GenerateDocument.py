'''
Given two strings : characters and document.
Check if you can make document string using characters.
You can always create empty string document
'''

def generateDocument(characters, document):
    data = {}
    for c in characters :
        if c in data :
            data[c] += 1
        else :
            data[c] = 1
    for c in document : 
        if c not in data or data[c] == 0 :
            return False
        data[c] -= 1
    return True
