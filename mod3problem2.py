#JTKIM
#4/22/19

wordList = ["Sunday", "Monday", "Tuesday"]
def reverse(words):
    return [words[-1]] + reverse(words[:-1]) if words else []
print(reverse(wordList))

