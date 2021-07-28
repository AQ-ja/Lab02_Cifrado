import base64
import matplotlib.pyplot as plt
from pygal import Histogram
from pygal.style import Style
import numpy as np
import random


def DecimalBits(txt):
    res = ''.join(format(ord(i), '08b') for i in txt)
    return(str(res))


def bitsToString(bits):
    bitsInt = int(bits, 2)
    bitNum = bitsInt.bit_length() + 7 // 8

    bitArray = bitsInt.to_bytes(bitNum, "big")
    stringBit = bitArray.decode()
    return(stringBit)


def StrToBase64(txt):
    strBit = txt.encode('ascii')
    strBase = base64.b64encode(strBit)
    base64Convert = strBase.decode('ascii')
    return(base64Convert)


def Base64ToString():
    mensaje64 = input("Ingrese la cadena de base64 a convertir a texto:\n")
    mssBit = mensaje64.encode('ascii')
    mssBytes = base64.b64decode(mssBit)
    strMss = mssBytes.decode('ascii')
    return(strMss)


def XOR():
    s1 = input("Ingrese la primera cadena de bits:\n")
    s2 = input("Ingrese la segunda cadena de bits:\n")
    listS1 = []
    listS2 = []
    result = []
    for i in s1:
        listS1.append(i)
    for x in s2:
        listS2.append(x)

    if len(listS1) == len(listS2):

        for y in range(len(listS1)):
            result.append((int(listS1[y]) ^ int(listS2[y])))
        res = " ".join([str(_) for _ in result])
        return res
    else:
        print(
            "Las dos cadenas de caracteres deben de contener la misma cantidad de elementos")


print("Bienvenido al Laboratorio No.2\n Que desea hacer: \n")
print(" 1. Convertir una cadena de caracteres a bits\n 2. Convertir una cadena de bits a caracteres\n 3. Convertir una cadena de caracteres en Base 64\n 4. Convertir una cadena de Base64 a caracteres\n 5. Operacion XOR entre dos cadenas de bits\n 6. Crear histograma de una cadena de bits\n 7. Crear histograma (bigrama)\n 8. Crear histograma (trigrama)\n 9. Crear histogramas de dos cadenas operadas por XOR\n 0. Salir\n")
try:
    op = int(input())
    if op > 0 and op < 10:
        if op == 1:
            print("Ha seleccionado la opcion 1\n")
            textoPlano = input(("Ingrese el texto a pasar a bits: \n"))
            print("El texto plano a bits : "+DecimalBits(textoPlano))
        if op == 2:
            print("Ha seleccionado la opcion 2\n")
            bitsText = input(("Ingrese la cadena de bits a pasar a texto:\n"))
            print("El resultado es:\n", bitsToString(bitsText))
        if op == 3:
            print("Ha seleccionado la opcion 3\n")
            tex = input("Ingrese el texto a convertir a base64:\n")
            print("El texto convertido a base 64 es:\n", StrToBase64(tex))
        if op == 4:
            print("Ha seleccionado la opcion 4\n")
            print("El texto convertido de base64 a caracteres es:\n",
                  Base64ToString())
        if op == 5:
            print("Ha seleccionado la opcion 5\n")
            print("La operción XOR entre dos cadenas de bits es:\n", XOR())
        if op == 6:
            print("Ha seleccionado la opcion 6\n")

            s1 = input("Ingrese la cadena de bits\n")
            listS1 = []
            for i in s1:
                listS1.append(i)

            intervalos = ['0', '1']
            n, bins, patches = plt.hist(listS1)
            plt.xlabel("Valores")
            plt.ylabel("Frecuencia")
            plt.title("Histograma")
            plt.show()

        if op == 7:
            print("Ha seleccionado la opcion 7\n")

            s1 = input("Ingrese la cadena de bits\n")
            listS1 = []

            for i in range(len(s1)):
                if i % 2 == 0:

                    n = 2
                    end = i+n
                    listS1.append(s1[i:end])

            intervalos = ['00', '01', '10', '11']
            n, bins, patches = plt.hist(listS1)
            plt.xlabel("Valores")
            plt.ylabel("Frecuencia")
            plt.title("Histograma")
            plt.show()
        if op == 8:
            print("Ha seleccionado la opcion 8\n")

            s1 = input("Ingrese la cadena de bits\n")
            listS1 = []

            for i in range(len(s1)):
                if i % 3 == 0:

                    n = 3
                    end = i+n
                    listS1.append(s1[i:end])
            intervalos = ['000', '001', '010',
                          '011', '100', '101', '110', '111']
            n, bins, patches = plt.hist(listS1)
            plt.xlabel("Valores")
            plt.ylabel("Frecuencia")
            plt.title("Histograma")
            plt.show()

        if op == 9:
            print("Ha seleccionado la opcion 9\n")

            listS1 = []
            listBigrama = []
            listTri = []
            result = []
            resultBigrams = []
            resultTri = []

            s1 = input("Ingrese la cadena de bits\n")
            listY = []

            for i in range(len(s1)):
                listY.append(random.randint(0, 1))

            for i in s1:
                listS1.append(i)

            for y in range(len(listS1)):
                result.append((int(listS1[y]) ^ int(listY[y])))
                res = " ".join([str(_) for _ in result])
            print(listS1)
            print(listY)
            print(result)
            # Bits
            # Histograma

            # Bigrama
            for i in range(len(s1)):
                if i % 2 == 0:

                    n = 2
                    end = i+n
                    resultBigrams.append(s1[i:end])
            # Trigrama
            for i in range(len(s1)):

                if i % 3 == 0:

                    n = 3
                    end = i+n
                    resultTri.append(s1[i:end])

            # intervalos = ['0', '1']

            print(listS1)
            print(listY)
            print(result)
            print(resultBigrams)
            print(resultTri)

            intervalosHistograma = ['0', '1']
            n, bins, patches = plt.hist(result)
            plt.xlabel("Valores")
            plt.ylabel("Frecuencia")
            plt.title("Histograma")
            plt.show()

            intervalosBig = ['00', '01', '10', '11']
            n, bins, patches = plt.hist(resultBigrams)
            plt.xlabel("Valores")
            plt.ylabel("Frecuencia")
            plt.title("Histograma bigrama")
            plt.show()

            intervalosTrig = ['000', '001', '010',
                              '011', '100', '101', '110', '111']
            n, bins, patches = plt.hist(resultTri)
            plt.xlabel("Valores")
            plt.ylabel("Frecuencia")
            plt.title("Histograma Trigrama")
            plt.show()

    else:
        print("Gracias por usar el programa")

except ValueError:
    print("IDebe de ingresar un numero")
