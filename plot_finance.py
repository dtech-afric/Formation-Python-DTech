import tkinter as tk
from tkinter import ttk, messagebox
import json, random, os
from datetime import datetime

# -------------------------
# Config
# -------------------------
QUESTIONS_PER_PART = 10
POINTS_CORRECT = 10
POINTS_INCORRECT = -5
LEADERBOARD_FILE = "leaderboard.json"
MAX_TIME = 15  # secondes par question

# -------------------------
# Utility functions
# -------------------------
def generate_question(theme=None):
    """
    Simule la génération d'une question par IA
    """
    sample_q = [
        {"question": "Quel algorithme est utilisé pour la régression linéaire ?",
         "options": ["KMeans", "Linear Regression", "Decision Tree", "SVM"], "answer": 1, "theme": "Data Science"},
        {"question": "Que signifie EDA ?", "options": ["Exploratory Data Analysis", "Enhanced Data Access",
                                                      "Encoded Data Array", "Estimated Data Average"], "answer": 0,
         "theme": "Data Science"},
        {"question": "Qu'est-ce que le 'cloud computing' ?", "options": ["Matériel informatique",
                                                                        "Services via Internet",
                                                                        "Langage de programmation",
                                                                        "Protocole réseau"], "answer": 1,
         "theme": "Culture Numérique"},
        {"question": "Quel type de réseau est utilisé pour classer des images ?",
         "options": ["RNN", "CNN", "SVM", "KNN"], "answer": 1, "theme": "Intelligence Artificielle"}
    ]
    return random.choice(sample_q)

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_leaderboard(board):
    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(board, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Erreur sauvegarde leaderboard:", e)

def update_leaderboard(player_key, delta):
    board = load_leaderboard()
    if player_key not in board:
        board[player_key] = {"total_points": 0, "total_good": 0, "total_bad": 0, "total_lost": 0,
                             "last_seen": None}
    p = board[player_key]
    p["total_points"] += delta.get("points", 0)
    p["total_good"] += delta.get("good", 0)
    p["total_bad"] += delta.get("bad", 0)
    p["total_lost"] += delta.get("lost", 0)
    p["last_seen"] = datetime.utcnow().isoformat() + "Z"
    save_leaderboard(board)

# -------------------------
# Application
# -------------------------
class DataQuizzApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DataQuizz")
        self.geometry("950x650")
        self.resizable(False, False)

        # State
        self.player_name = ""
        self.player_firstname = ""
        self.player_key = ""
        self.round_num = 0
        self.questions_pool = []
        self.current_round_questions = []
        self.current_index = 0
        self.score = 0
        self.good_answers = 0
        self.bad_answers = 0
        self.points_lost = 0
        self.selected = tk.IntVar(value=-1)
        self.time_left = MAX_TIME

        # Frames
        self.frame_login = ttk.Frame(self, padding=20)
        self.frame_quiz = ttk.Frame(self, padding=12)
        self.frame_result = ttk.Frame(self, padding=12)
        self.frame_leaderboard = ttk.Frame(self, padding=12)

        self._build_login()
        self._build_quiz()
        self._build_result()
        self._build_leaderboard()

        self._show_frame(self.frame_login)

    # -------------------------
    # Login
    # -------------------------
    def _build_login(self):
        ttk.Label(self.frame_login, text="Bienvenue sur DataQuizz", font=("Helvetica", 20, "bold")).pack(pady=16)
        frm = ttk.Frame(self.frame_login)
        frm.pack(pady=12)
        ttk.Label(frm, text="Prénom :").grid(row=0, column=0, sticky="e", padx=6)
        self.entry_firstname = ttk.Entry(frm, width=30)
        self.entry_firstname.grid(row=0, column=1)
        ttk.Label(frm, text="Nom :").grid(row=1, column=0, sticky="e", padx=6)
        self.entry_name = ttk.Entry(frm, width=30)
        self.entry_name.grid(row=1, column=1)
        ttk.Button(self.frame_login, text="Commencer", command=self._on_start_click).pack(pady=12)

    def _on_start_click(self):
        fn = self.entry_firstname.get().strip()
        ln = self.entry_name.get().strip()
        if not fn or not ln:
            messagebox.showwarning("Informations manquantes", "Merci d'indiquer votre prénom et votre nom.")
            return
        self.player_firstname = fn
        self.player_name = ln
        self.player_key = f"{fn} {ln}"
        self.round_num = 1
        messagebox.showinfo("Bienvenue", f"Bienvenue sur DataQuizz, {fn} ! 🎯")
        self._start_new_round()
        self._show_frame(self.frame_quiz)

    # -------------------------
    # Quiz UI
    # -------------------------
    def _build_quiz(self):
        self.lbl_player = ttk.Label(self.frame_quiz, text="", font=("Helvetica", 12))
        self.lbl_player.pack(anchor="w", pady=(0,4))
        self.lbl_round = ttk.Label(self.frame_quiz, text="", font=("Helvetica", 12))
        self.lbl_round.pack(anchor="e", pady=(0,4))

        self.lbl_theme = ttk.Label(self.frame_quiz, text="", font=("Helvetica", 10, "italic"))
        self.lbl_theme.pack(anchor="w", pady=(4,2))
        self.lbl_question = ttk.Label(self.frame_quiz, text="", font=("Helvetica", 14, "bold"), wraplength=800)
        self.lbl_question.pack(anchor="w", pady=(0,8))

        self.option_vars = []
        for i in range(4):
            rb = ttk.Radiobutton(self.frame_quiz, text=f"Option {i+1}", variable=self.selected, value=i,
                                 command=self._on_select)
            rb.pack(anchor="w", pady=4)
            self.option_vars.append(rb)

        # Timer bar
        self.timer_canvas = tk.Canvas(self.frame_quiz, width=400, height=20, bg="#eee")
        self.timer_bar = self.timer_canvas.create_rectangle(0, 0, 400, 20, fill="#4CAF50")
        self.timer_canvas.pack(pady=(6,10))

        # Feedback and controls
        self.lbl_feedback = ttk.Label(self.frame_quiz, text="", font=("Helvetica", 12))
        self.lbl_feedback.pack()
        ctrl = ttk.Frame(self.frame_quiz)
        ctrl.pack(pady=8)
        self.lbl_score = ttk.Label(ctrl, text="Score: 0", font=("Helvetica", 12))
        self.lbl_score.pack(side="left", padx=6)
        ttk.Button(ctrl, text="Suivant", command=self._on_next_clicked).pack(side="right", padx=6)
        ttk.Button(ctrl, text="Abandonner", command=self._on_quit).pack(side="right", padx=6)

    def _on_select(self):
        self.lbl_feedback.config(text="")

    def _start_new_round(self):
        self.current_index = 0
        self.score = 0
        self.good_answers = 0
        self.bad_answers = 0
        self.points_lost = 0
        self.selected.set(-1)
        self.current_round_questions = [generate_question() for _ in range(QUESTIONS_PER_PART)]
        self.lbl_player.config(text=f"Joueur: {self.player_key}")
        self.lbl_round.config(text=f"Partie {self.round_num}")
        self.lbl_score.config(text=f"Score: {self.score}")
        self.time_left = MAX_TIME
        self._show_question()

    def _show_question(self):
        if self.current_index >= len(self.current_round_questions):
            self._finish_round()
            return
        q = self.current_round_questions[self.current_index]
        self.lbl_theme.config(text=f"Thème: {q['theme']}")
        self.lbl_question.config(text=f"Q{self.current_index+1}. {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.option_vars[i].config(text=opt)
        self.selected.set(-1)
        self.lbl_feedback.config(text="")
        self._update_timer_bar()
        self._countdown()

    # -------------------------
    # Timer
    # -------------------------
    def _update_timer_bar(self):
        ratio = self.time_left / MAX_TIME
        self.timer_canvas.coords(self.timer_bar, 0, 0, 400 * ratio, 20)
        self.timer_canvas.itemconfig(self.timer_bar, fill="#4CAF50" if ratio > 0.3 else "#F44336")

    def _countdown(self):
        if self.time_left > 0:
            self._update_timer_bar()
            self.time_left -= 1
            self.after(1000, self._countdown)
        else:
            self._time_expired()

    def _time_expired(self):
        self.lbl_feedback.config(text=f"⏰ Temps écoulé ! {POINTS_INCORRECT} points", foreground="red")
        self.score += POINTS_INCORRECT
        self.points_lost += abs(POINTS_INCORRECT)
        self.current_index += 1
        self.lbl_score.config(text=f"Score: {self.score}")
        self.after(800, self._show_question)

    # -------------------------
    # Next / Finish
    # -------------------------
    def _on_next_clicked(self):
        if self.selected.get() == -1:
            messagebox.showinfo("Choix requis", "Veuillez sélectionner une option avant de continuer.")
            return
        q = self.current_round_questions[self.current_index]
        sel = self.selected.get()
        correct = q["answer"]
        if sel == correct:
            self.score += POINTS_CORRECT
            self.good_answers += 1
            self.lbl_feedback.config(text=f"Bonne réponse ! +{POINTS_CORRECT}", foreground="green")
        else:
            self.score += POINTS_INCORRECT
            self.bad_answers += 1
            self.points_lost += abs(POINTS_INCORRECT)
            self.lbl_feedback.config(text=f"Réponse incorrecte. Correct: {q['options'][correct]} ({POINTS_INCORRECT})",
                                     foreground="red")
        self.lbl_score.config(text=f"Score: {self.score}")
        self.current_index += 1
        self.time_left = MAX_TIME
        self.after(600, self._show_question)

    def _finish_round(self):
        delta = {"points": self.score, "good": self.good_answers, "bad": self.bad_answers, "lost": self.points_lost}
        update_leaderboard(self.player_key, delta)
        messagebox.showinfo("Fin de partie", f"Score: {self.score} points")
        self.round_num += 1
        self._start_new_round()

    def _on_quit(self):
        if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter ?"):
            self.destroy()


# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app = DataQuizzApp()
    app.mainloop()
