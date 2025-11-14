import math as m
import random as rd

def S(x, w, b):
    result = 0
    for i in range(len(x)):
        z = x[i] * w[i]
        result += z
    return result + b

def sigmoid(S):
    return 1/(1 + m.e**-S)

t = 0.5

x = [2,4.1,0.3,1.6,2.3]
w = [-0.09226562469274496, -0.058123268450022365, 0.5144415945952738, 0.18876678314226863, -0.32605476674339606]
b = rd.random()

lr = 0.2

epochs = 100
for i in range(epochs):
    params = sigmoid(S(x, w, b))
    for i in range(len(x)):
        peso = (params-t) * params*(1-params) * x[i]
        w[i] = w[i] - lr * peso

    bias = (params-t) * params * (1-params)
    b = b - lr * bias

    print(sigmoid(S(x, w, b)))
    pass
print(w)