n=float(input("Enter a number: "))
m=float(input("Enter another number: "))
z=n+m
print(f"The sum was: {z}")

# Round
print(f"The rounded sum is: {round(z)}")

# Comma separated
print(f"{z:,}")

# Rounding in formatted upto 2 decimals
# print(round(z,2))
print(f"{z:.2f}")