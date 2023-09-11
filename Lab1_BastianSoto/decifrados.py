import requests
import json

headers = {'Content-Type': 'text/plain',}
response = requests.get('http://finis.malba.cl/GetMsg', headers=headers)
print(response.text)
data = json.loads(response.text)
msg = data.get("msg", "")
print(msg)

def decifrado_rot(texto, n):
    resultado = ""
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            resultado += chr(((ord(caracter) - ord('a') + n) % 26) + ord('a'))
        elif 'A' <= caracter <= 'Z':
            resultado += chr(((ord(caracter) - ord('A') + n) % 26) + ord('A'))
        else:
            resultado += caracter
    return resultado

def decifrado_vigenere(texto, clave):
    texto_decifrado1 = ""
    clave_extendida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]
    for i in range(len(texto)):
        if texto[i].isalpha():
            desplazamiento_clave = ord(clave_extendida[i].upper()) - ord('A')

            if texto[i].islower():
                # Cifrar letra minúscula
                texto_decifrado1 += chr(((ord(texto[i]) - ord('a') - desplazamiento_clave) % 26) + ord('a'))
            else:
                # Cifrar letra mayúscula
                texto_decifrado1 += chr(((ord(texto[i]) - ord('A') - desplazamiento_clave) % 26) + ord('A'))
        else:
            # Mantener caracteres no alfabéticos sin cambios
            texto_decifrado1 += texto[i]

    return texto_decifrado1

##Desafio 1
#decifrado texto personal
#rot 7
texto = input("Texto: ")
texto_decifrado = decifrado_rot(texto, - 7)
#vinegere
texto_original1 = texto_decifrado
clave = "cvqnoteshrwnszhhksorbqcoas"
texto_decifrado1 = decifrado_vigenere(texto_original1, clave)
#rot 15
texto_final = decifrado_rot(texto_decifrado1, - 15)
print("Mensaje cifrado final:", texto_final)

#Desafio 2
#decifrado del texto de la pagina
#rot 7
texto1 = msg
texto_decifrado1 = decifrado_rot(texto1, - 7)
#vinegere
texto_original2 = texto_decifrado1
clave1 = "aobkqolrzsrigpknkufezioer"
texto_decifrado2 = decifrado_vigenere(texto_original2, clave1)
#rot 15
texto_final1 = decifrado_rot(texto_decifrado2, - 15)
print("Mensaje cifrado final:", texto_final1)
