from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)
    filtered = image[:]
    return filtered

Kernel = Kernel("minion.png", filter_function)

init()

# pegar os valores da matriz e fazer as contas
