def omitir_vocales(cadena):
    vocales = 'aeiouAEIOU'
    resultado = ''
    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    return resultado

# Solicitar cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Resultado con las vocales omitidas
resultado = omitir_vocales(texto)

# Imprimir el resultado
print("Texto con las vocales omitidas:", resultado)
