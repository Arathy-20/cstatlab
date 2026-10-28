import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("x**2")
plt.grid()
plt.show()


import numpy as np

arr = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],

    [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]
])

print("Input:\n", arr)
print("Diagonals:\n", np.diagonal(arr, axis1=1, axis2=2))

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Input:\n", arr)
print("Flattened:", arr.flatten())

import math
n = 10
a = (1 + math.sqrt(5)) / 2
for i in range(n):
    print(round((a**i - (1-a)**i) / math.sqrt(5)), end=" ")

import numpy as np

a = np.array([[1, 2], [3, 4]])
print("Input:\n", a)
print("Inverse:\n", np.linalg.inv(a))


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Input:", a, b)
print("Inner:", np.inner(a, b))
print("Outer:\n", np.outer(a, b))
print("Cross:", np.cross(a, b))

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Input:\n", a, "\n", b)
print("Kronecker Product:\n", np.kron(a, b))


import numpy as np

a = np.array([[1, 2], [3, 4]])
print("Input:\n", a)
print("List:", a.tolist())\

import numpy as np

a = np.array([[1, 2], [3, 4]])
print("Input:\n", a)
q, r = np.linalg.qr(a)
print("Q:\n", q)
print("R:\n", r)


import numpy as np

a = np.array([[1, 2], [3, 4]])
print("Input:\n", a)
v, w = np.linalg.eig(a)
print("Eigenvalues:", v)
print("Eigenvectors:\n", w)

import numpy as np

a = np.array([1, 4, 9, 16, 25])
print("Input:", a)
print("Difference:", np.diff(a, n=2))


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Input:", a, b)
print("Result:", np.einsum('i,i->', a, b))


import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8])

print("Input:", a, b)
print("Pearson Correlation:\n", np.corrcoef(a, b))


import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("Input:", a)
print("Mean:", np.mean(a))
print("Variance:", np.var(a))
print("Standard Deviation:", np.std(a))


import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4, 5])
print("Input:", a)
plt.plot(a)
plt.show()


import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print("Input:\n", a)
np.savetxt("data.csv", a, delimiter=",", fmt="%d")
print("CSV file created")


import pandas as pd

df = pd.DataFrame({'Name':['A','B','A','B'],
                   'Subject':['Math','Math','CS','CS'],
                   'Marks':[80,70,90,85]})
print("Input:\n", df)
print("Pivot Table:\n", df.pivot_table(
    values='Marks', index='Name', columns='Subject'))
print("Cross Tabulation:\n", pd.crosstab(df['Name'], df['Subject']))


s = input("Enter brackets: ")
while "()" in s or "{}" in s or "[]" in s:
    s = s.replace("()", "").replace("{}", "").replace("[]", "")
print("Valid" if s == "" else "Invalid")


grades = {'A': 90, 'B': 80, 'C': 70}
print("Grades:", grades)
print("Average:", sum(grades.values()) / len(grades))


s = input("Enter a string: ")
v = c = w = q = 0

for i in s.lower():
    if i in "aeiou":
        v += 1
    elif i.isalpha():
        c += 1
    elif i == "?":
        q += 1

w = len(s.split())



a = [[0, 0, 3], [0, 4, 0], [5, 0, 0]]
d = {(i, j): a[i][j] for i in range(3) for j in range(3) if a[i][j]}
print("Input:", a)
print("Sparse Matrix:", d)



f = open("data.txt", "r")
s = f.read()
f.close()

print("Words:", len(s.split()))
print("Sentences:", s.count(".") + s.count("?") + s.count("!"))
print("Uppercase:", sum(c.isupper() for c in s))
print("Lowercase:", sum(c.islower() for c in s))
print("Special symbols:", sum(not c.isalnum() and not c.isspace() for c in s))
