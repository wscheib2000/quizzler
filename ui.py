import tkinter as tk

THEME_COLOR = "#375362"
PADDING={'padx': 20, 'pady': 20}

class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # self.score_lbl = 

        self.canvas = tk.Canvas(self.window, bg='white', width=300, height=200)
        self.question_text = self.canvas.create_text(150, 100, text='Placeholder')
        self.canvas.grid(row=1, column=0, columnspan=2, **PADDING)

        self.true_img = tk.PhotoImage(file='./images/true.png')
        self.true_button = tk.Button(self.window, image=self.true_img)
        self.true_button.grid(row=2, column=0, **PADDING)

        self.false_img = tk.PhotoImage(file='./images/false.png')
        self.false_button = tk.Button(self.window, image=self.false_img)
        self.false_button.grid(row=2, column=1, **PADDING)

        self.window.mainloop()