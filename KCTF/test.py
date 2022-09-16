from itertools import product
URL = ""
groupA = ['a', 'B', 'C', 'D'] 
groupB = ['A', 'B', 'C', 'd']
a = ['B', 'C', 'D']
b = ['A', 'B', 'C']
A = list()
B = list()
for i in range(1, len(a)):
    A = list(map(''.join, product(a, repeat = 2)))
    B = list(map(''.join, product(b, repeat = 2)))
print(A)
print(B)
for i in range(len(A)):
    URL = "a"
    m = list(A[i])
    n = list(B[i])
    for k in range(2):
            URL = URL + n[k] + m[k]
    URL = URL + "d"
    print(URL)
for i in range(len(A)):
    URL = "d"
    m = list(A[i])
    n = list(B[i])
    for k in range(2):
            URL = URL + m[k] + n[k]
    URL = URL + "a"
    print(URL)
