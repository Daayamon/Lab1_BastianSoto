import requests

def cifrado_rot(texto, n):
    resultado = ""
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            resultado += chr(((ord(caracter) - ord('a') + n) % 26) + ord('a'))
        elif 'A' <= caracter <= 'Z':
            resultado += chr(((ord(caracter) - ord('A') + n) % 26) + ord('A'))
        else:
            resultado += caracter
    return resultado

def cifrado_vigenere(texto, clave):
    texto_cifrado1 = ""
    clave_extendida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]
    for i in range(len(texto)):
        if texto[i].isalpha():
            desplazamiento_clave = ord(clave_extendida[i].upper()) - ord('A')

            if texto[i].islower():
                # Cifrar letra minúscula
                texto_cifrado1 += chr(((ord(texto[i]) - ord('a') + desplazamiento_clave) % 26) + ord('a'))
            else:
                # Cifrar letra mayúscula
                texto_cifrado1 += chr(((ord(texto[i]) - ord('A') + desplazamiento_clave) % 26) + ord('A'))
        else:
            # Mantener caracteres no alfabéticos sin cambios
            texto_cifrado1 += texto[i]

    return texto_cifrado1



##Desafio 1 cifrados
#rot 7
texto = input("Texto: ")
texto_decifrado = cifrado_rot(texto, 15)
#vinegere
texto_original1 = texto_decifrado
clave = "cvqnoteshrwnszhhksorbqcoas"
texto_decifrado1 = cifrado_vigenere(texto_original1, clave)
#rot 15
texto_final = cifrado_rot(texto_decifrado1, 7)
print("Mensaje cifrado final:", texto_final)

headers = {'Content-Type': 'text/plain',}
data = {"msg": texto_final}

response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)
