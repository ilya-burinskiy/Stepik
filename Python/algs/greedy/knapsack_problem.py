import collections

class Item:

    def __init__(self, cost, weight):
        self.cost = cost
        self.weight = weight
        self.cost_per_weight = cost // weight

    def __repr__(self):
        return repr((self.cost, self.weight, self.cost_per_weight))

class ItemIterator(collections.abc.Iterator):

    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        return self._collection[self._cursor]

class Items(collections.abc.Iterable):

    def __init__(self, collection=None):
        self._collection = collection or []
        if collection is not None:
            for i in collection:
                self.put(i)

    def put(self, item: tuple):
        self._collection.append(Item(item[0], item[1]))

    def __iter__(self):
        self._collection.sort(key=lambda x: x.cost_per_weight, reverse=True)
        return ItemIterator(self._collection, -1)

class Knapsack:

    def __init__(self, W):
        self.W = W
        self.C = 0

    def put(self, item_part, item_part_cost):
        self.W -= item_part
        self.C += item_part_cost


def knapsack_problem(knapsack: Knapsack, items: Items):
    for item in items:
        if knapsack.W > 0:
            if knapsack.W >= item.weight:
                knapsack.put(item.weight, item.cost)
            else:
                knapsack.put(knapsack.W, knapsack.W * item.cost_per_weight)
        else:
            break



def main():
    inquiries, W = input().split()
    inquiries, W = int(inquiries), int(W)

    knapsack = Knapsack(W)
    items = Items()
    for _ in range(inquiries):
        w, c = input().split()
        w, c = int(w), int(c)
        items.put((w, c))

    knapsack_problem(knapsack, items)
    print("%.3f" %(knapsack.C))

if __name__ == "__main__":
    main()