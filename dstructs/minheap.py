import copy

class HeapMin:

    def __init__(self, array: list):
        self.__build_heap(array)

    def get_min(self):
        return self.__H[0]

    def insert(self, value: int):
        self.__size += 1
        self.__H.append(value)
        self.__sift_up(self.__size - 1)

    def extract_min(self):
        res = self.__H[0]
        self.__H[0] = self.__H[self.__size - 1]
        self.__size -= 1
        self.__sift_down(0)

        self.__H.pop()

        return res

    def remove(self, idx):
        self.__H[idx] = -float('inf')
        self.__sift_up(idx)
        self.extract_min()

    def change_priority(self, idx, new_p):
        old_p = self.__H[idx]
        self.__H[idx] = new_p
        if new_p < old_p:
            self.__sift_up(idx)
        else:
            self.__sift_down(idx)


    def __build_heap(self, array):
        self.__size = len(array)           
        self.__H = array

        for i in range(self.__size // 2 - 1, -1, -1):
            self.__sift_down(i)

    def __parent(self, idx):
        parent = (idx - 1) // 2 
        return parent
        
    def __left_child(self, idx):
        return 2 * idx + 1

    def __right_child(self, idx):
        return 2 * idx + 2

    def __sift_up(self, idx):
        while idx > 0 and self.__H[self.__parent(idx)] > self.__H[idx]:
            self.__H[self.__parent(idx)], self.__H[idx] = \
                self.__H[idx], self.__H[self.__parent(idx)]

            idx = self.__parent(idx)


    def __sift_down(self, idx):
        smallest = idx
        left = self.__left_child(idx)
        right = self.__right_child(idx)

        if left < self.__size and self.__H[left] < self.__H[smallest]:
            smallest = left
        if right < self.__size and self.__H[right] < self.__H[smallest]:
            smallest = right
        if smallest != idx:
            self.__H[idx], self.__H[smallest] = self.__H[smallest], \
                                                self.__H[idx]
            
            self.__sift_down(smallest)
    
    def __str__(self):
        return ''.join(str(self.__H[i]) for i in range(self.__size))
        