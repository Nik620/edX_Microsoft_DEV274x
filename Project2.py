# Originally completed May 20, 2020
#original list of animals
farm = ['cat', 'goat', 'cat']

#define function
def list_o_matic(string):
    if string == "":
        return print(farm.pop(), "popped from the list\n")
    elif string in farm:
        farm.remove(string)
        return print("1 instance of",string,"removed from list\n")
    else:
        farm.append(string)
        return print("1 instance of",string,"appended to list\n")

#initialization
print("look at all the aminals", farm)
string = (input("enter the name of an animal: ")).lower()

#primary program flow
while True:
    if string == "quit":
        break
    else:
        list_o_matic(string)
        if farm == []:
            break
    print("look at all the aminals", farm)
    string = (input("enter the name of an animal: ")).lower()

#program conclusion
print("Goodbye!")
