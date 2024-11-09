from MCQ_Class_CWWTECHproject import MCQ

# List of Questions and options to choose from
Question = [
    "1. What is the sum of 5 and 7? \n (a)12 \n (b)6 \n (c)5 \n (d)9\n\n",
    "2. What is the product of 5 and 7? \n (a)12 \n (b)6 \n (c)35 \n (d)19\n\n",
    "3. Who is the president of USA \n (a)Donald Trump \n (b) liz truzz \n (c)Dan Fodio"
    " \n (d)Buhari\n\n",
    "4. How many days are in a week \n (a)5 \n (b)6 \n (c)7 \n (d)8\n\n",
    "5. How many consonants are there in the english alphabet \n (a)20 \n (b)21 \n (c)22 \n (d)23\n\n",
]

# List of answers to the questions
obj_questions = [
    MCQ(Question[0], "a"),
    MCQ(Question[1], "c"),
    MCQ(Question[2], "a"),
    MCQ(Question[3], "c"),
    MCQ(Question[4], "b")

]


# function that receives user input, check if it is correct, calculate the score and
# returns the value


def user_score():
    total_score = 0
    for question in obj_questions:
        answer = input(question.ask)
        if answer == question.answer:
            total_score += 1
    print(f"You got {total_score} of {len(obj_questions)} correctly! ")
    return total_score


'''
def ratio():
    fish = user_score() / len(obj_questions)
    if fish >= 0.5:
        print("You Passed! ")
    else:
        print("You failed")
        
ratio()
'''


def factors():
    ratio = user_score() / len(obj_questions)
    return ratio
# print(f"You got {user_score(obj_questions)} of {len(obj_questions)} correctly!")


# f"you got {user_score(obj_questions)} of {len(obj_questions)}

def grade():
    # student_grade = factors()
    # student_grade = user_score(obj_questions) / len(obj_questions)
    if factors() >= 0.5:
        print("You got above the pass mark You passed")
    else:
        print("You failed")


def result():
    grade()


result()
