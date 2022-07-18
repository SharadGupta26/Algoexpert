'''
Given string, perform run length encoding.

If given characters 10 or more than 10, split encoding

{
  "string": "AAAAAAAAAAAAABBCCCCDD"
}

o/p - 9A4A2B4C2D
'''

def runLengthEncoding(string):
    ans = ""
    count = 1
    for i in range(len(string) - 1) :
        if string[i] == string[i + 1] :
            count += 1
        else :
            ans = ans + str(count) + string[i]
            count = 1
        if count == 10 :
            ans = ans + str(count-1) + string[i]
            count = 1

    return ans + str(count) + string[-1]
