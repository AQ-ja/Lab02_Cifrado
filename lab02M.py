

def DecimalBits(txt):
    res = ''.join(format(ord(i), '08b') for i in textoPlano)
    return(str(res))


def BitsDecimal(bits):
    binary_int = int(bits, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return(ascii_text)



textoPlano = input(("Ingrese el texto a pasar a bits: \n"))

print("El texto plano a bits : "+DecimalBits(textoPlano))

bitsText=input(("Ingrese la cadena de bits a pasar a texto:\n"))
print(BitsDecimal(bitsText))



