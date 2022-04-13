def char_range(letter1, letter2):
    for i in range(ord(letter1) + 1, ord(letter2)):
        print(chr(i), end=" ")


char1 = input()
char2 = input()

char_range(char1, char2)