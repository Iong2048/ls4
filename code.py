print("your input: ", end="")
name = input()

def my_uppercase(str):
    distance = ord('A') - ord('a')
    for ch in str:
        if ch > 'a' and ch < 'z':
            print(chr(ord(ch) + distance), end="")
        else:
            print(ch, end="")