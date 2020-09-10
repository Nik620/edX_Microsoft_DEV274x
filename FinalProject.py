# Originally completed May 25/2020
#function to collect input of 5 unique element names
def get_names():
    guess_list = []
    while len(guess_list) != 5:
        guess = input("Enter the name of an element: ")
        if len(guess) == 0:
            print('please enter a value')
        elif guess.title() in guess_list:
            print(guess.lower(),"was already entered\t\t<--no duplicates allowed")
        else:
            guess_list.append(guess.title())
    return guess_list

#import & open data
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
elements1_20 = open('elements1_20.txt','r')
print("\n")

#create list of elements
element = elements1_20.readline().strip('\n')
element_list = []
while element:
    element_list.append(element)
    element = elements1_20.readline().strip('\n')
    
#retrieve input
print("List any 5 of the first 20 elements in the periodic table:")
user_guesses = get_names()

#quiz sorting
correct = []
correct_line = ""
incorrect = []
incorrect_line = ""
for i in range(len(user_guesses)):
    if user_guesses[i] in element_list:
        correct.append(user_guesses[i])
        correct_line += user_guesses[i] + " "
    else:
        incorrect.append(user_guesses[i])
        incorrect_line += user_guesses[i] + " "
        
#results
print("")
print(int(len(correct)/5*100),"% correct")
print("Found:",correct_line)
print("Not Found:",incorrect_line)

elements1_20.close()
