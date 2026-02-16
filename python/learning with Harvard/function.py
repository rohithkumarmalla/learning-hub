"""def hello(to):
    print(f"hello!, {to}")

name=input("Enter your name: ")
hello(name)
"""

# Calling hello first 
def main():
    name = input("enter your name: ")
    hello() # Didn't passed the argument
def hello(to="World"): # Default value
    print(f"Hello! {to}")
main()