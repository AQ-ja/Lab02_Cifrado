import matplotlib.pyplot as plt
from pygal import Histogram
from pygal.style import Style
import numpy as np

s1 = input("Ingrese la cadena de bits\n")
listS1 = []
for i in s1:
    listS1.append(i)

# for x in range(len(listS1)):
total0 = 0
total1 = 0
for x in range(len(listS1)):
    if "0" in listS1[x]:
        total0 += 1
    if "1" in listS1[x]:
        total1 += 1


if "0" in listS1[0]:
    print("SI")

for i in range(0, len(listS1)):
    listS1[i] = int(listS1[i])

# print(listS1)
# Resultado divir por el total de caracteres y multiplicar por 100
# print((len(listS1)))
# print(total0)
# print(total1)

intervalos = [0, 1]
n, bins, patches = plt.hist(listS1)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
