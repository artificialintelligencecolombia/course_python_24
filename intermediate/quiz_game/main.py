# Import required modules
from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain

# Create a empty list that will store all questions objs from question_data list
# Note: I created 2 list for both methods of creating the question_bank list. BOTH ARE CORRECT.
question_bank1 = []
question_bank2 = []

# Method 1
for i in question_data:
    question_bank1.append(Question(i["text"], i["answer"]))

# Method 2
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank2.append(new_question)
    
# Create a quiz obj from the QuizBrain class
quizz = QuizBrain(question_bank2)
# Call the quizz obj method calles next_question
quizz.next_question()