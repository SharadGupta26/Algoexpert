'''
Given an array building heights and a direction.
Return index of buildings which can see sunsets.
Any building can see sunset only if its height is greater than all buildings ahead of it.

Direction West = left of array
Direction East = right of array
'''

def sunsetViews(buildings, direction):
    ans = []
    i = 0 if direction == "WEST" else len(buildings) - 1
    
    while i >= 0 and i < len(buildings) :
        if not ans :
            ans.append(i) 
        elif buildings[i] > buildings[ans[-1]] :
            ans.append(i)
        if direction == "WEST" :
            i += 1
        else :
            i -= 1
        
    return sorted(ans)
