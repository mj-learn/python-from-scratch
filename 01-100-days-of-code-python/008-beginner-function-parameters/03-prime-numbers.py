def prime_checker(number):
    prime = "It's a prime number."
    not_prime = "It's not a prime number."

    # Trial Division
    if number <= 1:
        print(not_prime)
        return

    if number <= 3:
        print(prime)
        return

    if number % 2 == 0 or number % 3 == 0:
        print(not_prime)
        return

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            print(not_prime)
            return
        i += 6

    print(prime)


# Tested with 7575334519, 686902007802107, 4471432732904659, 71272669736357291
# Solution in tutorial is much slower than trial division

# Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)
