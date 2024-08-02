n = 1000000000
print(f"{n:_}")  # Output: 1_000_000_000
print(f"{n:,}")  # Output: 1,000,000,000

f = 1324.54244362
print(f"{f:.0f}")  # Output: 1324
print(f"{f:.2f}")  # Output: 1324.54
print(f"{f:,.3f}")  # Output: 1,324.54
print(f"{f:_.3f}")  # Output: 1_324.54

var = "Hello"
print(f"{var:>20}: World!")  # Output:                Hello: World!
print(f"{var:<20}: World!")  # Output: Hello               : World!
print(f"{var:^20}: World!")  # Output:        Hello        : World!
print(f"{var:_>20}: World!")  # Output: _______________Hello: World!
print(f"{var:#<20}: World!")  # Output: Hello###############: World!
print(f"{var:.^20}: World!")  # Output: .......Hello........: World!

a = 5
b = 10
my_var = "Bob says hi"
print(f"{a + b}")  # Output: 15
print(f"{a + b = }")  # Output: a + b = 15
print(f"{bool(a) = }")  # Output: bool(a) = True
print(f"{my_var = }")  # Output: my_var = "Bob says hi"
