def inverter_string(string):
    string_invertida = ""
    # Percorre a string de trás para frente
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# Exemplo de uso:
entrada = input("Informe uma string para ser invertida: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
