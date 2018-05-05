class PriorityQueue:

    def __init__(self):
        self.__queue = list()

    def insert(self, item, priority):
        self.__queue.append((item, priority))

    def empty(self):
        if not len(self.__queue):
            return True
        return False

    def get_max(self, get_prio=False):
        if self.empty():
            raise Exception ('Queue is Empty!')

        prio = float('-inf')
        h_index = -1
        for i in range(len(self.__queue)):
            if prio < self.__queue[i][1]:
                prio = self.__queue[i][1]
                item = self.__queue[i][0]
                h_index = i

        self.__queue.pop(h_index)
        if not get_prio:
            return item
        return item, prio

    def get_min(self, get_prio=False):
        if self.empty():
            raise Exception ('Queue is Empty!')

        prio = float('inf')
        h_index = -1
        for i in range(len(self.__queue)):
            if prio > self.__queue[i][1]:
                prio = self.__queue[i][1]
                item = self.__queue[i][0]
                h_index = i

        self.__queue.pop(h_index)
        if not get_prio:
            return item
        return item, prio


# Driver Code
'''
p = PriorityQueue()
p.insert(12, 90)
p.insert('abf', 12)
p.insert('wer', 122)
p.insert('azaz', 1111)
p.insert('tgb', 67)

print(p.get_max())
print(p.get_max())
print(p.get_max())
print(p.get_max())
print(p.get_max())
'''
