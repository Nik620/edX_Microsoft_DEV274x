# Originally completed May 21/2020
#word_mixer program
def word_mixer(word_list):
    word_list.sort()
    new_words = []
    if len(word_list) > 5:
        while len(word_list) > 5:
            new_words.append(word_list.pop(-5))
            new_words.append(word_list.pop(0))
            new_words.append(word_list.pop(-1))
        return new_words
    else:
        new_words = word_list
        return new_words
        

#input & creation of word list, removing unnecessary punctuation
string = input("enter a saying or poem: ")
split_string = string.split()
j = 0
temp = []
length = len(split_string)

#loop to clean up string
for i in split_string:
    if "," in i:
        temp = list(i)
        temp.remove(",")
        i = "".join(temp)
    if "." in i:
        temp = list(i)
        temp.remove(".")
        i = "".join(temp)
    if ":" in i:
        temp = list(i)
        temp.remove(":")
        i = "".join(temp)
    if ";" in i:
        temp = list(i)
        temp.remove(";")
        i = "".join(temp)
    split_string[j] = i
    temp = []
    j += 1

#loop to capitalize and lower words
for i in range(0,length):
    if len(split_string[i]) <= 3:
        split_string[i] = split_string[i].lower()
    elif len(split_string[i]) >= 7:
        split_string[i] = split_string[i].upper()
        
    
#calling word_mixer
print("\n")
print(" ".join(word_mixer(split_string)))
