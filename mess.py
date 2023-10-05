def collatz_sequence(n):
    terms = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        terms += 1
    return terms

def collatz_checker(limit):
    for num in range(1, min(limit + 1, 10001)):
        terms = collatz_sequence(num)
        is_conjecture_true = terms > 1  # Corrected condition

        if not is_conjecture_true:
            print(f"Collatz conjecture is false for {num}")

# Check Collatz conjecture for positive numbers up to 10,000
limit = 10000
collatz_checker(limit)
