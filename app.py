from tkinter import *
from chat import get_similarity, bot_name

# Updated lighter color scheme
BG_COLOR = "#2C3E50"  # Soft dark slate background
TEXT_COLOR = "#ECF0F1"  # Off-white text
ACCENT_COLOR = "#1ABC9C"  # Turquoise for highlights
INPUT_BG = "#34495E"  # Lighter slate for input fields
BUTTON_BG = "#3498DB"  # Bright blue button background
DIVIDER_COLOR = "#8E44AD"  # Vibrant purple divider

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 14 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Question Similarity Checker")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=700, bg=BG_COLOR)  # Larger window for better spacing

        # Head label with accent color
        head_label = Label(self.window, bg=BG_COLOR, fg=ACCENT_COLOR,
                           text="Question Similarity Checker", font=FONT_BOLD, pady=15)
        head_label.place(relwidth=1)

        # Stylish divider
        line = Label(self.window, bg=DIVIDER_COLOR)
        line.place(relwidth=0.9, rely=0.07, relheight=0.005, relx=0.05)

        # Text widget for results with border effect
        self.text_widget = Text(self.window, width=20, height=2, bg=INPUT_BG, fg=TEXT_COLOR,
                                font=FONT, padx=10, pady=10, borderwidth=2, relief="flat")
        self.text_widget.place(relheight=0.65, relwidth=0.9, rely=0.09, relx=0.05)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scrollbar with matching style
        scrollbar = Scrollbar(self.text_widget, bg=INPUT_BG, troughcolor=BG_COLOR, borderwidth=0)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom frame for inputs
        bottom_frame = Frame(self.window, bg=BG_COLOR)
        bottom_frame.place(relwidth=1, rely=0.76, relheight=0.24)

        # Question 1 entry with label (increased height)
        q1_label = Label(bottom_frame, text="Q1:", bg=BG_COLOR, fg=ACCENT_COLOR, font=FONT_BOLD)
        q1_label.place(relwidth=0.1, relheight=0.1, rely=0.05, relx=0.05)
        self.q1_entry = Entry(bottom_frame, bg=INPUT_BG, fg=TEXT_COLOR, font=FONT, 
                              insertbackground=ACCENT_COLOR, borderwidth=2, relief="flat")
        self.q1_entry.place(relwidth=0.75, relheight=0.1, rely=0.05, relx=0.15)  # Height increased to 0.1
        self.q1_entry.focus()
        self.q1_entry.bind("<Return>", self._on_enter_pressed)

        # Question 2 entry with label (increased height)
        q2_label = Label(bottom_frame, text="Q2:", bg=BG_COLOR, fg=ACCENT_COLOR, font=FONT_BOLD)
        q2_label.place(relwidth=0.1, relheight=0.1, rely=0.18, relx=0.05)
        self.q2_entry = Entry(bottom_frame, bg=INPUT_BG, fg=TEXT_COLOR, font=FONT, 
                              insertbackground=ACCENT_COLOR, borderwidth=2, relief="flat")
        self.q2_entry.place(relwidth=0.75, relheight=0.1, rely=0.18, relx=0.15)  # Height increased to 0.1
        self.q2_entry.bind("<Return>", self._on_enter_pressed)

        # Compare button with hover effect
        compare_button = Button(bottom_frame, text="Compare", font=FONT_BOLD, bg=BUTTON_BG, fg=TEXT_COLOR,
                                activebackground=ACCENT_COLOR, activeforeground=BG_COLOR, borderwidth=2, 
                                relief="flat", command=self._compare_questions)
        compare_button.place(relx=0.35, rely=0.35, relheight=0.1, relwidth=0.3)
        compare_button.bind("<Enter>", lambda e: compare_button.config(bg="#E74C3C"))  # Coral hover
        compare_button.bind("<Leave>", lambda e: compare_button.config(bg=BUTTON_BG))

    def _on_enter_pressed(self, event):
        self._compare_questions()

    def _compare_questions(self):
        q1 = self.q1_entry.get()
        q2 = self.q2_entry.get()
        if not q1 or not q2:  
            return

        # Clear the entry fields
        self.q1_entry.delete(0, END)
        self.q2_entry.delete(0, END)

        # Get similarity response
        response = get_similarity(q1, q2) + "\n\n"
        
        # Insert response into text widget
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, response)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()