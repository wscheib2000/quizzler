import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 16, 'italic')

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = tk.Label(self.window, text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Arial', 12, 'normal'))
        self.score_lbl.grid(row=0, column=1)

        self.canvas = tk.Canvas(self.window, bg='white', width=300, height=200)
        self.question_text = self.canvas.create_text(150, 100, width=280, justify='center', text='Placeholder', font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = tk.PhotoImage(file='./images/true.png')
        self.true_button = tk.Button(self.window, image=self.true_img, command=lambda: self.check_answer('True'))
        self.true_button.grid(row=2, column=0)

        self.false_img = tk.PhotoImage(file='./images/false.png')
        self.false_button = tk.Button(self.window, image=self.false_img, command=lambda: self.check_answer('False'))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.true_button.config(state='normal')
            self.false_button.config(state='normal')

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'You\'ve completed the quiz!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}')
    
    def check_answer(self, answer: str):
        self.give_feedback(self.quiz.check_answer(answer))
        self.score_lbl.config(text=f'Score: {self.quiz.score}')

    def give_feedback(self, is_right: bool):
        self.canvas.config(bg='green' if is_right else 'red')
        self.window.after(1000, self.get_next_question)
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')