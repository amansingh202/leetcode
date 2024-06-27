class HashTable:
    def __init__(self):
        self.MAX = 10
        self.data = [None for i in range(self.MAX)]

    def gethash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX
    
    def get_probe_range(self, index):
        return [*range(index, len(self.arr))] + [* range(0, index)]
    
    def __getitem__(self, key):
        h = self.gethash(key)

        if self.arr[h] is None:
            return
        
        prob_range = self.get_probe_range(h)

        for prob_index in prob_range:
            element = self.arr[prob_index]

            if element is None:
                return
            
            if element[0] == key:
                return element[1]
            
    def __setitem__(self, key, val):
        h = self.gethash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)  


    def find_slot(self, key, index):
        prob_range = self.get_probe_range(index) 

        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index

            if self.arr[prob_index][0] == key:
                return prob_index

        raise Exception("Hashmap full")    

    def __delitem__(self, key):
        h = self.gethash(key)
        prob_range = self.get_probe_range(key)

        for prob in prob_range:
            if self.arr[prob] is None:
                return
            
            if self.arr[prob][0] == key:
                self.arr[prob] = None

        print(self.arr)

