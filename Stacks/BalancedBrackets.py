def balancedBrackets(string):
    data = []
    for i in string :
        if i not in ['(', '{', '[', ')', '}', ']'] :
            continue
        if i in ['(', '{', '['] :
            data.append(i)
            continue
        if not data :
            return False
        if i == ')' and data[-1] == '(' :
            data.pop()
        elif i == '}' and data[-1] == '{' :
            data.pop()
        elif i == ']' and data[-1] == '[' :
            data.pop()
        else :
            return False
    if data :
        return False
    else :
        return True


# same approach but cleaner code 
def balancedBrackets(string):
    data = []
    closing = ")}]"
    opening = "({["
    matching = {")" : "(", "}" : "{", "]" : "["}
    for i in string :
        if i in opening:
            data.append(i)
        elif i in closing :
            if not data :
                return False
            if data[-1] == matching[i] :
                data.pop()
            else :
                return False
    if data :
        return False
    else :
        return True