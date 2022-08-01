# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self) :
        self.data = []
        self.minData = []
        self.maxData = []
    
    def peek(self):
        return self.data[-1]

    def pop(self):
        val = self.data.pop()
        if self.minData[-1] == val :
            self.minData.pop()
        if self.maxData[-1] == val :
            self.maxData.pop()
        return val

    def push(self, number):
        self.data.append(number)
        if self.minData :
            if number <= self.minData[-1] :
                self.minData.append(number)
        else :
            self.minData.append(number)
        if self.maxData:
            if number >= self.maxData[-1] :
                self.maxData.append(number)
        else :
            self.maxData.append(number)

    def getMin(self):
        return self.minData[-1]

    def getMax(self):
       return self.maxData[-1]
