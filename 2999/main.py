def main() :
    text = input()
    symbol = ("*")
    time = 2 + (len(text))  # Example repetition count
    print(symbol * time)
    print(f"{symbol}{text}{symbol}")
    print(symbol * time)
main()