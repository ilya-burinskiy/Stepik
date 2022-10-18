from abc import ABC, abstractmethod

class Heap(ABC):
    
    def __init__(self, array=None):
        self._H = array or []
        self._size = len(self._H)
        self._build_heap()

    def __len__(self):
        return self._size

    def __str__(self):
        return ''.join(str(self._H[i]) for i in range(self._size))

    def _parent(self, idx):
        parent = (idx - 1) // 2 
        return parent
        
    def _left_child(self, idx):
        return 2 * idx + 1

    def _right_child(self, idx):
        return 2 * idx + 2

    def _build_heap(self):
        for i in range(self._size // 2 - 1, -1, -1):
            self._sift_down(i)

    @abstractmethod
    def _sift_up(self, idx):
        pass

    @abstractmethod
    def _sift_down(self, idx):
        pass

    @abstractmethod
    def insert(self, x):
        pass


class MinHeap(Heap):

    def __init__(self, array=None):
        super().__init__(array)

    def _sift_up(self, idx):
        while idx > 0 and self._H[self._parent(idx)] > self._H[idx]:
            self._H[idx], self._H[self._parent(idx)] = \
                    self._H[self._parent(idx)], self._H[idx]
            idx = self._parent(idx)
            
    def _sift_down(self, idx):
        min_ = idx
        l = self._left_child(idx)
        r = self._right_child(idx)

        if l < self._size and self._H[l] < self._H[min_]:
            min_ = l
        if r < self._size and self._H[r] < self._H[min_]:
            min_ = r
        if min_ != idx:
            self._H[idx], self._H[min_] = self._H[min_], \
                                                self._H[idx]
            
            self._sift_down(min_)

    def heap_min(self):
        if self._size > 0:
            return self._H[0]

    def insert(self, x):
        self._size += 1
        self._H.append(x)
        self._sift_up(self._size - 1)

    def extract_min(self):
        res = self._H[0]
        self._H[0] = self._H[self._size - 1]
        self._size -= 1
        self._sift_down(0)
        self._H.pop()

        return res

    def remove(self, idx):
        if idx < self._size:
            self._H[idx] = -float('inf')
            self._sift_up(idx)
            self.extract_min()
        else:
            raise IndexError

    def change_priority(self, idx, newp):
        if idx < self._size:
            old_p = self._H[idx]
            self._H[idx] = newp
            if newp < old_p:
                self._sift_up(idx)
            else:
                self._sift_up(idx)
        else:
            raise IndexError

class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def _sift_up(self, idx):
        while idx > 0 and self._H[self._parent(idx)] < self._H[idx]:
            self._H[idx], self._H[self._parent(idx)] = \
                    self._H[self._parent(idx)], self._H[idx]
            idx = self._parent(idx)
            
    def _sift_down(self, idx):
        max_ = idx
        l = self._left_child(idx)
        r = self._right_child(idx)

        if l < self._size and self._H[l] > self._H[max_]:
            max_ = l
        if r < self._size and self._H[r] > self._H[max_]:
            max_ = r
        if max_ != idx:
            self._H[idx], self._H[max_] = self._H[max_], \
                                                self._H[idx]
            
            self._sift_down(max_)

    def heap_max(self):
        if self._size > 0:
            return self._H[0]

    def insert(self, x):
        self._size += 1
        self._H.append(x)
        self._sift_up(self._size - 1)

    def extract_max(self):
        res = self._H[0]
        self._H[0] = self._H[self._size - 1]
        self._size -= 1
        self._sift_down(0)
        self._H.pop()

        return res

    def remove(self, idx):
        if idx < self._size:
            self._H[idx] = float('inf')
            self._sift_up(idx)
            self.extract_max()
        else:
            raise IndexError

    def change_priority(self, idx, newp):
        if idx < self._size:
            oldp = self._H[idx]
            if newp < oldp:
                self._sift_down(idx)
            else:
                self._sift_up(idx)
        else:
            raise IndexError

