def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def verify_collatz_conjecture(limit):
    for i in range(1, limit + 1):
        sequence = collatz_sequence(i)
        if sequence[-1] != 1:
            print(f"Collatz conjecture is not true for {i}")
            return
    print("Collatz conjecture is true for all tested numbers.")

# Verify for the first 10,000 positive integers
verify_collatz_conjecture(10000)
