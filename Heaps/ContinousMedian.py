# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
import heapq
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.minHeap = []
        self.maxHeap = []

    def insert(self, number):
        #insertion
        if not self.minHeap or number > self.minHeap[0] :
            heapq.heappush(self.minHeap, number)
        else :
            self.insertMaxHeap(number)

        #rebalncing
        if len(self.minHeap) == len(self.maxHeap) + 2 :
            self.insertMaxHeap(heapq.heappop(self.minHeap))
        elif len(self.maxHeap) == len(self.minHeap) + 2 :
            heapq.heappush(self.minHeap, self.getMaxHeap())

        #updating median
        if len(self.minHeap) == len(self.maxHeap) :
            self.median = (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap) :
            self.median = self.minHeap[0]
        else :
            self.median = -self.maxHeap[0]
            
        
    
    def getMaxHeap(self):
        return -1 * heapq.heappop(self.maxHeap)

    def insertMaxHeap(self, number) :
        heapq.heappush(self.maxHeap, -1 * number)

    def getMedian(self):
        print(self.minHeap, self.maxHeap, self.median)
        return self.median
