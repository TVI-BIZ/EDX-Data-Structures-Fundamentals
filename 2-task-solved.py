# python3
import time

import sys
import threading

start_time = time.time()


def compute_height(n, parents):
 nodeDict = {}


class TreeHeight:
    def height(self, node):
        if node == -1:
            return 0
        if self.parent[node] in self.heights:
            self.heights[node] = self.heights[self.parent[node]] + 1
        else:
            self.heights[node] = self.height(self.parent[node]) + 1
        return self.heights[node]

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.heights = {}

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            maxHeight = max(maxHeight, self.height(vertex))
        return maxHeight;


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())
    #print("--- %s seconds ---" % (time.time() - start_time))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
