import cowsay
import sys

a = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux']

cowsay.cow("Hello")
print(a,"\n\nChoose a character and type the message in ''.\neg: tux 'Good Morning Sachin': ")
userInput = ''

while userInput != 'ok':
    try:
        userInput = input("Go on or type 'ok' to exit: ")
        animal, msg = userInput.split(maxsplit=1)
        msg = msg.strip("'")
        if  animal in a:
            print(cowsay.get_output_string(animal, msg))
            break
        else:
            print("please follow the format and spelling, or press ctrl + (c or d) to exit")
            continue
    except:
        if userInput == 'ok':
            break
        print('enter the input in correct format')