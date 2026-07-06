'''
This program prints a text surrounded by symbols.
'''
def main(): 
    '''This program prints a text surrounded by symbols.'''
    text = input()
    symbol = ("*")
    time = 2 + len(text)
    print(symbol * time)
    print(f"{symbol}{text}{symbol}")
    print(symbol * time)
main()