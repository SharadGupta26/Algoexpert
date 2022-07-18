

def caesarCipherEncryptor(string, key):
    ans = ''
    
    for c in string :
        a = ord(c) - ord('a')
        a = ((a + key) % 26) + ord('a')
        ans += chr(a)
    return ans
