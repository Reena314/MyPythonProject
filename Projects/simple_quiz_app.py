# def quiz_app():
#     print("\n===== SIMPLE QUIZ APP =====\n")

#     # Questions and answers stored in a list of dictionaries
#     questions = [
#         {
#             "question": "1. What is the capital of France?",
#             "options": ["A. Berlin", "B. Paris", "C. London", "D. Madrid"],
#             "answer": "B"
#         },
#         {
#             "question": "2. What is 5 + 7?",
#             "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
#             "answer": "C"
#         },
#         {
#             "question": "3. Who wrote 'Harry Potter'?",
#             "options": ["A. J.K. Rowling", "B. Elon Musk", "C. Shakespeare", "D. Newton"],
#             "answer": "A"
#         }
#     ]

#     score = 0  # Track score

#     # Loop through each question
#     for q in questions:
#         print(q["question"])
#         for option in q["options"]:
#             print(option)

#         user_answer = input("Your answer (A/B/C/D): ").upper()

#         if user_answer == q["answer"]:
#             print("Correct!\n")
#             score += 1
#         else:
#             print(f"Wrong! Correct answer is {q['answer']}\n")

#     print(f"Your final score: {score} out of {len(questions)}")

# # Run the quiz
# quiz_app()


def quiz():
    print("=========quiz questions========")
    
    Questions = [
        {
            'question': 'what is the answer of 5 + 7',
            'options' : ['A. 11', 'B. 12 ','C. 13'],
            'answer'  : 'B'
        },
        {
            'question': 'what is the answer of 5 * 7',
            'options' : ['A. 35', 'B. 36 ','C. 38'],
            'answer'  : 'A'
        }
        
    ]
    score = 0
    for q in Questions:
        print(q['question'])
        for option in q['options']:
            print(option)
            
        user_answer = input("your answer is A/B/C/D :" ).upper()
            
        if user_answer == q["answer"]:
                print ("correct")
                score += 1
        else:
                print(f"wrong ! correct answer is {q['answer']}")
                
    print(f"your final score : {score} out of {len(Questions)}")
            
quiz()           
