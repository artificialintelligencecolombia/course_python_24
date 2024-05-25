# Here we are going to create the QuizBrain class. Its functions are:
# Asking the questions to the user
# Checking if the answer is correct
# Checking if we are at the end of the quiz
# It's going to contain the method next_question() for pull up the next question from the list depending on the question number the user is

class QuizBrain():
    def __init__(self, questions_list):
        self.question_number = 0 # Keep track which question the user is currently on
        self.questions_list = questions_list # list of questions
        
    # Define the method
    def next_question(self):
        # Access the current question (each question is an obj from question_banck list)
        # Each question_list obj has as attrs: 'text' and 'answer'
        current_question = self.questions_list[self.question_number]
        
        # Increment the question number by one (so instead of start from 0, starts from 1)
        self.question_number += 1
        
        # Display the question and get the answer
        input(f"Q.{self.question_number}: {current_question.text} [True|False]: ")
        
        