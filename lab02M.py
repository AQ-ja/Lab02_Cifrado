import base64


def DecimalBits(txt):
    res = ''.join(format(ord(i), '08b') for i in txt)
    return(str(res))


def BitsDecimal(bits):
    binary_int = int(bits, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return(ascii_text)


def StrToBase64(txt):
    message_bytes = txt.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return(base64_message)


def Base64ToString():
    base64_message = input("ingrese:\n")
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return(message)


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

        print(" ".join([str(_) for _ in result]))
    else:
        print(
            "Las dos cadenas de caracteres deben de contener la misma cantidad de elementos")


print("Bienvenido al Laboratorio No.2\n Que desea hacer: \n")
print(" 1. Convertir una cadena de caracteres a bits\n 2. Convertir una cadena de bits a caracteres\n 3. Convertir una cadena de caracteres en Base 64\n 4. Convertir una cadena de Base64 a caracteres\n 5. Operacion XOR entre dos cadenas de bits\n 0. Salir\n")
try:
    op = int(input())
    if op > 0 and op < 6:
        if op == 1:
            textoPlano = input(("Ingrese el texto a pasar a bits: \n"))
            print("El texto plano a bits : "+DecimalBits(textoPlano))
        if op == 2:
            bitsText = input(("Ingrese la cadena de bits a pasar a texto:\n"))
            print(BitsDecimal(bitsText))
        if op == 3:
            tex = input("Ingrese el texto a convertir a base64:\n")
            print(StrToBase64(tex))
        if op == 4:
            print(Base64ToString())
        if op == 5:
            XOR()

    else:
        print("Gracias por usar el programa")

except ValueError:
    print("Ingrese un numero")
