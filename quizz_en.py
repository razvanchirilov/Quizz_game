from random import choice

# introduction quiz to participants
print("\n")
print("Hi, this is a quizz!")
print("\n")
print("Would you like to participate?")
print("\n")
print ("Answer YES or NO!")
print("\n")

# check if the player is ready to play or not
while True:
    # player's answer
    answer= str(input("Your answer is: ").lower())
    print("\n")
    if answer == "yes":
        print("Are you ready?")
        break
    elif answer == "no":
        print("Ok we'll wait for you when you're ready!")  
        exit()  
    else:
        print("I think you wrote something else, please answer with 'YES' or 'NO'.")
   

# the first question is asked

print("The first question in the quiz is:\n ")


# list of questions in the quiz
quizz_list = [
    "It has a fluffy top, it tastes nice, the sauce is peppery and the salami is a bit bitey. ",
    "It has no leaves, it'not a flower, in the woods and on the fields, in the gardens and on the hillside it's always standing on one foot. What is it? ",
    "What falls into the water and doesn't makes splash? ",
    "I have countless shirts, you're sobbing! "
]
quizz_list.sort()

# create a new match list against the list of questions to validate if I have only unique guesses
# if the randomly chosen question from the list of questions is in the list_of_queries ==> pass (i.e. it doesn't display my question), if not it takes the other conditions in turn
verification_list = []

# this variable stores correct answers
store_correct_answers = []
# this variable quantifies correct answers
count_correct_answers = 0

# this variable stores wrong answers
store_wrong_answers = []
# this variable quantifies wrong answers
count_wrong_answers = 0

# loop questions until the list is exhausted
while True:
    random_question = choice(quizz_list)
    if random_question in verification_list:
        pass
    else:
        print(random_question)
        print("\n") 
        print("Do you know what it is?")
        print("\n")
        gamer_answer = str(input("Your answer is: "))
        if random_question == "It has a fluffy top, it tastes nice, the sauce is peppery and the salami is a bit bitey. " and gamer_answer == "pizza":
            count_correct_answers += 1
            store_correct_answers.append(gamer_answer)
            print(f"Well done you have " + str(count_correct_answers) + " point/points!")
            verification_list.append(random_question)
            verification_list.sort()
            if quizz_list == verification_list:
                print("Game over! Thanks for participating!")
                print(f"Player, you have "+ str(count_correct_answers) +" correct answers and "+ str(count_wrong_answers) + " wrong answers. Train your mind! Good Luck!!! \n")
                exit() 
            print("Do you think you know how to answer the next question?\n")           
        elif random_question == "It has no leaves, it'not a flower, in the woods and on the fields, in the gardens and on the hillside it's always standing on one foot. What is it? " and gamer_answer == "mushroom":
            count_correct_answers += 1
            store_correct_answers.append(gamer_answer)
            print(f"Well done you have " + str(count_correct_answers) + " point/points!")
            verification_list.append(random_question)
            verification_list.sort()
            if quizz_list == verification_list:
                print("The game is over! Thanks for participating!")
                print(f"Player, you have "+ str(count_correct_answers) +" correct answers and "+ str(count_wrong_answers) + " wrong answers. Train your mind! Good Luck!!! \n")
                exit()  
            print("Do you think you know how to answer the next question?\n")      
        elif random_question == "What falls into the water and doesn't makes splash? " and gamer_answer == "leaf":
            count_correct_answers += 1
            store_correct_answers.append(gamer_answer)
            print(f"Well done you have " + str(count_correct_answers) + " point/points!")
            verification_list.append(random_question)
            verification_list.sort()
            if quizz_list == verification_list:
                print("The game is over! Thanks for participating!")
                print(f"Player, you have "+ str(count_correct_answers) +" correct answers and "+ str(count_wrong_answers) + " wrong answers. Train your mind! Good Luck!!! \n")
                exit()
            print("Do you think you know how to answer the next question?\n")           
        elif random_question == "I have countless shirts, you're sobbing! " and gamer_answer == "onion":
            count_correct_answers += 1
            store_correct_answers.append(gamer_answer)
            print(f"Well done you have " + str(count_correct_answers) + " point/points!")
            verification_list.append(random_question)
            verification_list.sort()
            if quizz_list == verification_list:
                print("The game is over! Thanks for participating!")
                print(f"Player, you have "+ str(count_correct_answers) +" correct answers and "+ str(count_wrong_answers) + " wrong answers. Train your mind! Good Luck!!! \n")
                exit()
            print("Do you think you know how to answer the next question?\n")
            continue    
        else:
            if gamer_answer != "pizza" or gamer_answer != "mushroom" or gamer_answer != "leaf" or gamer_answer != "onion":
                store_wrong_answers.append(gamer_answer)
                count_wrong_answers += 1
                print("\n")
                print("Wrong! This is not the correct answer!")
                verification_list.append(random_question)
                verification_list.sort()
                if quizz_list == verification_list:
                    print("The game is over! Thanks for participating")
                    print(f"Player, you have "+ str(count_correct_answers) +" correct answers and "+ str(count_wrong_answers) + " wrong answers. Train your mind! Good Luck!!! \n")
                    exit()
                print("Next question is: ")
                print("\n")
