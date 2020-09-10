# Originally completed May 12, 2020

# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [] copy and paste in edX assignment page
quote = input("enter a 1 sentence quote, non-alpha separate words: ").lower()
word = ""
i = 0
for ltr in quote:
    if ltr.isalpha():
        word += ltr
        if i == len(quote) - 1:
            if word[0] > "g":
                print(word.upper())
    else:
        if word != "":
            if word[0] > "g":
                print(word.upper())
        word = ""
    i += 1
