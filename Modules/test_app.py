print("---------------------------------------------------------------------------------------------------------")
print("Enter Your Answer -a,b,c")
from test_class import Question

que_no = [
    "A man presses more weight on earth at :\na : Sitting position\nb : Standing Position\nc : Lying Position\n",
    "Young's modulus is the property of :\na : Solid only\nb : Liquid only\nc : Both Solid and Liquid\n",
    "Product of Force and Velocity is called :\na : Momentum\nb : Work\nc : Power\n"
]
questions = [
    Question(que_no[0],"b"),
    Question(que_no[1],"a"),
    Question(que_no[2],"c")

]

def run_test(questions):
    score = 0
    for question in questions:
        print("---------------------------------------------------------------------------------------------------------")
        answer = input(question.prompt + "Answer : ") #.prompt is a string type so here the varabale is converted into string
        if answer == question.answer:
            score += 1
    print("Result = You got " + str(score) +"/" + str(len(questions)) + " correct. ")
run_test(questions)
