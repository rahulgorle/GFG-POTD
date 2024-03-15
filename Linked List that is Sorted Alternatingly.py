class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        arr = []
        while h1:
            arr.append(h1.data)
            h1 = h1.next
        sorte = sorted(arr)
        for i in range(len(sorte)):
            print(sorte[i], end= ' ')
