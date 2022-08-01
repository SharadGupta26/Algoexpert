'''
Given an string, generate all possible valid Ip address.

an Ip address is valid if
It is saperated in four parts
Each part is within range of 0-255
any part contains leading zero.
'''

def validIPAddresses(string):
    ans = []
    generate(string, 0, '', ans)
    return ans

def generate(string, decimalsPlaced, ip,  ans) :
    if decimalsPlaced == 3 and isValid(string):
        ans.append(ip  + string)
        return
    for i in range(min(3, len(string))) :
        prefix = string[0:i+1]
        suffix = string[i+1 : len(string)]  
        if isValid(prefix) :
            generate(suffix, decimalsPlaced + 1, ip + prefix + '.', ans)

def isValid(string) :
    if not string :
        return False
    if len(string) > 1 and string[0] == '0' :
        return False
    if int(string) > 255 :
        return False    
    return True
