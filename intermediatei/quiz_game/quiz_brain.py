# Here we are going to create the QuizBrain class. Its functions are:
# Asking the questions to the user
# Checking if the answer is correct
# Checking if we are at the end of the quiz
# It's going to contain the method next_question() for pull up the next question from the list depending on the question number the user is

class QuizBrain():
    def __init__(self, questions_list):
        self.question_number = 0 # Keep track which question the user is currently on
        self.questions_list = questions_list # list of questions
        self.score = 0 # User's score
        
    # Define the method
    # Access the current question (each question is an obj from question_bank list)
    # Each question_list obj has as attrs: 'text' and 'answer'
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        
        # Increment the question number by one (so instead of start from 0, starts from 1)
        self.question_number += 1
        
        # Display the question and get the answer from user
        usr_answer = input(f"Q.{self.question_number}: {current_question.text} (True|False): ")

        self.check_answers(usr_answer, current_question.answer)
        
    # Method that processes all questions in the list by calling next_question() until the end is reached   
    def still_has_questions(self):
            len_question_list = len(self.questions_list)
            while self.question_number < len_question_list:
                self.next_question()
            
            # Final of the quizz
            print(f"You,ve completed the quizz. Congratulations. \n Your final score is {self.score}/{self.question_number}")
                
    def check_answers(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Correct answer")
            self.score += 1
        else:
            print("Wrong answer")    
        print(f"Score: {self.score}/{self.question_number}\n")