from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)
    filtered = []

    lenY = len(image)
    lenX = len(image[0])

    top = len(kernel)//2
    left = len(kernel[0])//2

    for i in range(0, lenY, stride[0]):
        new_lin = []
        for j in range(0, lenX, stride[1]):
            S = 0
            SK = 0
            for ki in range(len(kernel)):
                for kj in range(len(kernel[ki])):
                    y = i-top+ki
                    x = j-left+kj
                    SK += kernel[ki][kj]
                    
                    if y < 0 or y >= lenY or x < 0 or x >= lenY:
                        continue
                    S += image[y][x] * kernel[ki][kj]
            #----
            if SK != 0:
                S /= SK
            
            if S < 0:
                S = 0
            if S > 255:
                S = 255
            #----
            new_lin.append(S)
        filtered.append(new_lin)

    return filtered

Kernel = Kernel("minion.png", filter_function)

init()