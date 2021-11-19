from questions import Question


question_text = ["is majd cool? \n (a) yes \n (b) no \n (c) no\n\n",
                 "is majd cool? \n (a) yes \n (b) no \n (c) no\n\n",
                 "is majd cool? \n (a) yes \n (b) no \n (c) no\n\n",
                 ]

questions = [Question(question_text[0], "a"),
             Question(question_text[1], "a"),
             Question(question_text[2], "a"),
             ]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
