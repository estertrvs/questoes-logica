def fibonacci(num):
    a, b = 0, 1
    fib_sequence = [a]

    while b <= num:
        fib_sequence.append(b)
        a, b = b, a + b

    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
print(fibonacci(numero))
