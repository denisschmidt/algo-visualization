from random import shuffle
import numpy as np
from pyparsing import col
import matplotlib.pyplot as plt
import matplotlib.cbook as cb


class HamCycle:
    def __init__(self, rows, cols, max_size=6, shuffle=True, display=True) -> None:
        """
        R, C: (Rows, Columns) in the array
        max_size: The maximum subarray size allowed, recommended 6 <= max_size <= 40 because of sub-cycle calc. times
        shuffle: Shuffles kernel windows before merging subcycles (if true makes fullcycle appear more random)
        display: If true plots the subdivided regions, subcycles and full cycles for the array
        """
        self.rows = rows
        self.cols = cols
        self.max_size = max_size

        print("Subdividing array")
        self.subarrays = self.subdivide(rows - 1, cols - 1, max_size)
        if display:
            self.show_subcycle_regions()

    def subdivide(self, rows, cols, max_size):
        """
        splits array into subarrays that:
            1. have an even number of nodes
            2. have less than max_size nodes
            
        returns a list of [(y1, x1, y2, x2), ...] representing the bounds of the subarrays
        """
        def size(y1, x1, y2, x2):
            return (y2 - y1 + 1) * (x2 - x1 + 1)

        def DFS(y1, x1, y2, x2):
            nonlocal max_size
            if size(y1, x1, y2, x2) <= max_size:
                return [(y1, x1, y2, x2)]

            # divide along horizontal
            if y2 - y1 > x2 - x1:
                y = (y1 + y2) // 2
                if (y - y1) & 1:
                    return DFS(y1, x1, y, x2) + DFS(min(y + 1, y2), x1, y2, x2)
                return DFS(y1, x1, max(y - 1, y1), x2) + DFS(y, x1, y2, x2)

            # divide along vertical
            x = (x1 + x2) // 2
            return DFS(y1, x1, y2, x) + DFS(y1, min(x + 1, x2), y2, x2)

        return DFS(0, 0, rows, cols)

    def show_subcycle_regions(self):
        A = [[0] * self.cols for _ in range(self.rows)]
        subs = self.subarrays[:]
        shuffle(subs)
        for k, (y1, x1, y2, x2) in enumerate(subs):
            for i in range(y1, y2 + 1):
                for j in range(x1, x2 + 1):
                    A[i][j] = k
        print(A)
        plt.figure('subarray regions')
        plt.title("Subdivisions of Array")
        plt.imshow(A)
        plt.show()
        plt.savefig('images/subarray_regions.png')


if __name__ == '__main__':
    plt.close('all')
    rows = 10
    cols = 8
    ham = HamCycle(rows, cols, max_size=36, shuffle=True, display=True)
