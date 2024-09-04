def fibonacci(n):
    # Inicializa a sequência com os dois primeiros números de Fibonacci
    fib_sequence = [0, 1]
    
    # Continua calculando a sequência até que o último número seja maior ou igual a n
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def is_in_fibonacci(n):
    # Calcula a sequência de Fibonacci até n
    fib_sequence = fibonacci(n)
    
    # Verifica se n está na sequência
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = int(input("Informe um número: "))
resultado = is_in_fibonacci(numero)
print(resultado)
