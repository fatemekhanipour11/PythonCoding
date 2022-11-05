from os import system

a = input("your words: ").split(" ")
print(a)
morse_code = {"A": ".-", "B": "-...", "C": "-.-.",
              "D": "-..", "E": ".", "F": "..-.",
              "G": "--.", "H": "....", "I": "..",
              "J": ".---", "K": "-.-", "L": ".-..",
              "M": "--", "N": "-.", "O": "---",
              "P": ".--.", "Q": "--.-", "R": ".-.",
              "S": "...", "T": "-", "U": "..-",
              "V": "..-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..",
              " ": "   "}
for i in a:
    i = i.upper()

    for x in i:
        print(morse_code[x], end=" ")
        morse = morse_code[x]
        # morse = morse.replace(".", "•")
        # morse = morse.replace("-", "−")
    print("     ", end=" ")
