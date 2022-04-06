# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
'''
Implement LRU cache class with size = maxSize
if key already exist in cache, same key is to be updated and no new key is to be created.
If size == max, then remove least accessed key from cache
'''
class Node :
	def __init__(self, key, value) :
		self.key = key
		self.value = value
		self.prev = None
		self.next = None
		
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.head = None
        self.tail = None
        self.data = {}
        self.size = 0

    def removeTailKey(self) :
        self.data.pop(self.tail.key, None)
        self.tail = self.tail.prev
        self.size -= 1
        if self.size == 0 :
            self.head = None
            self.tail = None
        
    def setHead(self, node) :
        if not self.head :
            self.head = node
        else :
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
            
    def insertKeyValuePair(self, key, value):
        if self.size == self.maxSize and key not in self.data:
            self.removeTailKey()
        if key in self.data :
            node = self.data[key]
            node.value = value
        else :
            node = Node(key, value)
            self.size += 1
        self.data[key] = node
        self.setHead(node)
        if not self.tail :
            self.tail = node
        

    def adjustNode(self, node) :
        if node == self.tail and node.prev:
            self.tail = node.prev
            self.tail.next = None
            
        if node.prev :
            node.prev.next = node.next 
        
        if node.next :
            node.next.prev = node.prev
            
    def getValueFromKey(self, key):
        if key not in self.data :
            return None
        node = self.data[key]
        self.adjustNode(node)
        self.setHead(node)
        return node.value

    def getMostRecentKey(self):
        return self.head.key

