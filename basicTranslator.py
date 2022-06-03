# Vowels will convert into "X"

def translate(wordList):
    translation = ""
    for letter in wordList:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter your Word: ")))


