import tkinter as tk
from tkinter import ttk, messagebox
import json, random, os
from datetime import datetime


def with_timer(duration: int):
    """
    Décorateur pour imposer un timer sur une fonction.
    Si le joueur ne répond pas dans 'duration' secondes,
    on considère la question comme ratée.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Démarrer un compte à rebours
            self.time_left = duration
            self.update_timer_label()

            # planifier une action automatique quand le temps est écoulé
            self.after(duration * 1000, lambda: self._time_expired(func))
            
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


# -------------------------
# QUESTIONS (sample)
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


LEADERBOARD_FILE = "leaderboard.json"
POINTS_CORRECT = 10
POINTS_INCORRECT = -5
QUESTIONS_PER_PART = 10

# -------------------------
# Utility : leaderboard persistence
# -------------------------
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
    """
    delta is a dict: {'points': int, 'good': int, 'bad': int, 'lost': int}
    Accumulate values for the player_key.
    """
    board = load_leaderboard()
    if player_key not in board:
        board[player_key] = {
            "total_points": 0,
            "total_good": 0,
            "total_bad": 0,
            "total_lost": 0,
            "last_seen": None
        }
    p = board[player_key]
    p["total_points"] += delta.get("points", 0)
    p["total_good"] += delta.get("good", 0)
    p["total_bad"] += delta.get("bad", 0)
    p["total_lost"] += delta.get("lost", 0)
    p["last_seen"] = datetime.utcnow().isoformat() + "Z"
    save_leaderboard(board)

# -------------------------
# Tkinter App
# -------------------------
class DataQuizzApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DataQuizz")
        self.geometry("900x600")
        self.resizable(False, False)

        # styling
        self.style = ttk.Style(self)
        # default theme often 'clam' is available; set fonts
        try:
            self.style.theme_use('clam')
        except Exception:
            pass
        default_font = ("Helvetica", 11)
        self.option_add("*Font", default_font)
        self.style.configure("TButton", padding=6)
        self.style.configure("Title.TLabel", font=("Helvetica", 18, "bold"))
        self.style.configure("Small.TLabel", font=("Helvetica", 10))
        self.style.configure("FeedbackGreen.TLabel", foreground="green")
        self.style.configure("FeedbackRed.TLabel", foreground="red")

        # state
        self.player_name = ""
        self.player_firstname = ""
        self.player_key = ""  # unique key used in leaderboard, e.g. "Firstname Lastname"
        self.round_num = 0

        # per-round counters
        self.questions_pool = []
        self.current_round_questions = []
        self.current_index = 0
        self.score = 0
        self.good_answers = 0
        self.bad_answers = 0
        self.points_lost = 0
        self.selected = tk.IntVar(value=-1)

        # frames
        self.frame_login = ttk.Frame(self, padding=20)
        self.frame_quiz = ttk.Frame(self, padding=12)
        self.frame_result = ttk.Frame(self, padding=12)
        self.frame_leaderboard = ttk.Frame(self, padding=12)

        self._build_login()
        self._build_quiz()
        self._build_result()
        self._build_leaderboard()

        # show login first
        self._show_frame(self.frame_login)

        self.timer_label = ttk.Label(self.frame_login, text="Temps restant: 15s", font=('Helvetica', 12, 'bold'))
        self.timer_label.pack(pady=(10,0))


    # -------------------------
    # Login / Welcome
    # -------------------------
    def _build_login(self):
        for w in self.frame_login.winfo_children():
            w.destroy()
        lbl = ttk.Label(self.frame_login, text="Bienvenue sur DataQuizz", style="Title.TLabel")
        lbl.pack(pady=(8,16))

        frm = ttk.Frame(self.frame_login)
        frm.pack(pady=8)

        ttk.Label(frm, text="Prénom :").grid(row=0, column=0, sticky="e", padx=6, pady=6)
        self.entry_firstname = ttk.Entry(frm, width=30)
        self.entry_firstname.grid(row=0, column=1, pady=6)

        ttk.Label(frm, text="Nom :").grid(row=1, column=0, sticky="e", padx=6, pady=6)
        self.entry_name = ttk.Entry(frm, width=30)
        self.entry_name.grid(row=1, column=1, pady=6)

        self.start_btn = ttk.Button(self.frame_login, text="Commencer", command=self._on_start_click)
        self.start_btn.pack(pady=(18,6))

        self.help_label = ttk.Label(self.frame_login, text="Entrer votre prénom et nom puis cliquez sur Commencer", style="Small.TLabel")
        self.help_label.pack()

    def _on_start_click(self):
        fn = self.entry_firstname.get().strip()
        ln = self.entry_name.get().strip()
        if not fn or not ln:
            messagebox.showwarning("Informations manquantes", "Merci d'indiquer votre prénom et votre nom.")
            return
        self.player_firstname = fn
        self.player_name = ln
        # player key
        self.player_key = f"{self.player_firstname} {self.player_name}"
        self.round_num = 1
        messagebox.showinfo("Bienvenue", f"Bienvenue sur DataQuizz, {self.player_firstname} !\nBonne chance 🎯")
        self._start_new_round()
        self._show_frame(self.frame_quiz)

    # -------------------------
    # Quiz UI
    # -------------------------
    def _build_quiz(self):
        for w in self.frame_quiz.winfo_children():
            w.destroy()

        # header
        hdr = ttk.Frame(self.frame_quiz)
        hdr.pack(fill="x", pady=(0,8))
        self.lbl_player = ttk.Label(hdr, text="", style="Small.TLabel")
        self.lbl_player.pack(side="left", padx=6)
        self.lbl_round = ttk.Label(hdr, text="", style="Small.TLabel")
        self.lbl_round.pack(side="right", padx=6)

        # question area
        self.q_area = ttk.Frame(self.frame_quiz, padding=8, relief="flat")
        self.q_area.pack(fill="both", expand=True)

        self.lbl_theme = ttk.Label(self.q_area, text="", style="Small.TLabel")
        self.lbl_theme.grid(row=0, column=0, sticky="w", pady=(4,8), padx=6)
        self.lbl_question = ttk.Label(self.q_area, text="", wraplength=760, font=("Helvetica", 14, "bold"))
        self.lbl_question.grid(row=1, column=0, columnspan=2, sticky="w", padx=6, pady=(0,12))

        # radio buttons
        self.option_vars = []
        for i in range(4):
            rb = ttk.Radiobutton(self.q_area, text=f"Option {i+1}", variable=self.selected, value=i, command=self._on_select)
            rb.grid(row=2 + i, column=0, sticky="w", padx=12, pady=4)
            self.option_vars.append(rb)

        # feedback and progress
        self.lbl_feedback = ttk.Label(self.q_area, text="", style="Small.TLabel")
        self.lbl_feedback.grid(row=2, column=1, sticky="w", padx=6, pady=4)
        self.progress = ttk.Progressbar(self.q_area, mode="determinate", length=300)
        self.progress.grid(row=7, column=0, sticky="w", padx=6, pady=12)

        # score / controls
        ctrl = ttk.Frame(self.frame_quiz)
        ctrl.pack(fill="x", pady=(6,0))
        self.lbl_score = ttk.Label(ctrl, text="Score: 0", style="Small.TLabel")
        self.lbl_score.pack(side="left", padx=6)
        self.btn_next = ttk.Button(ctrl, text="Suivant", command=self._on_next_clicked)
        self.btn_next.pack(side="right", padx=6)
        self.btn_quit = ttk.Button(ctrl, text="Abandonner", command=self._on_quit)
        self.btn_quit.pack(side="right", padx=6)

    def _on_select(self):
        # enable next
        self.btn_next.state(["!disabled"])
        self.lbl_feedback.config(text="")

    def _start_new_round(self):
        # reset per-round counters
        self.current_index = 0
        self.score = 0
        self.good_answers = 0
        self.bad_answers = 0
        self.points_lost = 0
        self.selected.set(-1)
        self.current_round_questions = [generate_question() for _ in range(QUESTIONS_PER_PART)]

        # update UI labels
        self.lbl_player.config(text=f"Joueur: {self.player_key}")
        self.lbl_round.config(text=f"Partie {self.round_num}")
        self.progress["maximum"] = QUESTIONS_PER_PART
        self.progress["value"] = 0
        self.lbl_score.config(text=f"Score: {self.score}")
        # show the first question
        self._show_question()

    @with_timer(3600)  # 15 secondes par question
    def _show_question(self):
        if self.current_index >= len(self.current_round_questions):
            # round finished
            self._finish_round()
            return
        q = self.current_round_questions[self.current_index]
        theme = q.get("theme", "")
        self.lbl_theme.config(text=f"Thème: {theme}")
        self.lbl_question.config(text=f"Q{self.current_index + 1}. {q['question']}")
        # set options
        for i, opt in enumerate(q["options"]):
            self.option_vars[i].config(text=opt)
        # clear selection and feedback
        self.selected.set(-1)
        self.lbl_feedback.config(text="")
        self.btn_next.state(["!disabled"])
        self.progress["value"] = self.current_index
        self.lbl_score.config(text=f"Score: {self.score}")

    def _on_next_clicked(self):
        if self.selected.get() == -1:
            messagebox.showinfo("Choix requis", "Veuillez sélectionner une option avant de continuer.")
            return
        q = self.current_round_questions[self.current_index]
        sel = self.selected.get()
        correct = q.get("answer")
        if sel == correct:
            self.score += POINTS_CORRECT
            self.good_answers += 1
            self.lbl_feedback.config(text=f"Bonne réponse ! +{POINTS_CORRECT}", foreground="green")
        else:
            self.score += POINTS_INCORRECT
            self.bad_answers += 1
            self.points_lost += abs(POINTS_INCORRECT)
            correct_text = q["options"][correct]
            self.lbl_feedback.config(text=f"Réponse incorrecte. Réponse correcte : {correct_text} ({POINTS_INCORRECT})", foreground="red")
        # update and go next
        self.lbl_score.config(text=f"Score: {self.score}")
        self.current_index += 1
        self.progress["value"] = self.current_index
        # short delay so feedback is visible
        self.after(600, self._show_question)

    def _finish_round(self):
        # show result frame for the round
        self._update_result_frame()
        self._show_frame(self.frame_result)

    def _on_quit(self):
        # ask confirm
        if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter ?"):
            self.destroy()
    
    """Met à jour le label du timer toutes les secondes."""

    def update_timer_label(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Temps restant: {self.time_left}s")
            self.time_left -= 1
            self.after(1000, self.update_timer_label)
    
    """Appelé quand le temps d'une question est écoulé."""

    def _time_expired(self, func):
        if self.selected.get() == -1:  # pas de réponse choisie
            self.lbl_feedback.config(text="⏰ Temps écoulé ! -5 points", foreground="red")
            self.score -= 5
            self.current_index += 1
            self.progress['value'] = self.current_index
            self.after(800, self._show_question)

    # -------------------------
    # Result UI (per round)
    # -------------------------
    def _build_result(self):
        for w in self.frame_result.winfo_children():
            w.destroy()
        lbl = ttk.Label(self.frame_result, text="Résumé de la partie", style="Title.TLabel")
        lbl.pack(pady=(8,12))
        self.lbl_round_summary = ttk.Label(self.frame_result, text="", font=("Helvetica", 12))
        self.lbl_round_summary.pack(pady=6)
        self.lbl_round_details = ttk.Label(self.frame_result, text="", font=("Helvetica", 10))
        self.lbl_round_details.pack(pady=6)
        btn_frame = ttk.Frame(self.frame_result)
        btn_frame.pack(pady=(10,6))
        self.btn_continue = ttk.Button(btn_frame, text="Continuer (partie suivante)", command=self._continue_next_round)
        self.btn_continue.grid(row=0, column=0, padx=8)
        self.btn_back_home = ttk.Button(btn_frame, text="Retour accueil", command=self._back_to_home)
        self.btn_back_home.grid(row=0, column=1, padx=8)
        self.btn_show_board = ttk.Button(self.frame_result, text="Afficher Leaderboard", command=self._show_leaderboard)
        self.btn_show_board.pack(pady=(8,4))

    def _update_result_frame(self):
        # percent for this round
        max_points = QUESTIONS_PER_PART * POINTS_CORRECT
        percent = int((self.score / max_points) * 100) if max_points != 0 else 0
        # mention
        if self.score >= max_points:
            mention = "Amazing 🎉"
        elif percent > 70:
            mention = "Great job! 👍"
        else:
            mention = "Keep learning! 💪"
        # round summary text
        summary = f"Partie {self.round_num} - Score: {self.score} / {max_points} ({percent}%) — {mention}"
        details = (f"Bonnes réponses: {self.good_answers}\n"
                   f"Mauvaises réponses: {self.bad_answers}\n"
                   f"Points perdus cette partie: {self.points_lost}")
        self.lbl_round_summary.config(text=summary)
        self.lbl_round_details.config(text=details)
        # update leaderboard cumulative for this player
        delta = {"points": self.score, "good": self.good_answers, "bad": self.bad_answers, "lost": self.points_lost}
        update_leaderboard(self.player_key, delta)

    def _continue_next_round(self):
        self.round_num += 1
        self._start_new_round()
        self._show_frame(self.frame_quiz)

    def _back_to_home(self):
        # reset small state, go to login
        self.entry_firstname.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self._show_frame(self.frame_login)

    # -------------------------
    # Leaderboard UI
    # -------------------------
    def _build_leaderboard(self):
        for w in self.frame_leaderboard.winfo_children():
            w.destroy()
        lbl = ttk.Label(self.frame_leaderboard, text="Leaderboard (Historique)", style="Title.TLabel")
        lbl.pack(pady=(8,12))
        self.lb_tree = ttk.Treeview(self.frame_leaderboard, columns=("points", "good", "bad", "lost", "last"), show="headings", height=12)
        self.lb_tree.heading("points", text="Points")
        self.lb_tree.heading("good", text="Bonnes")
        self.lb_tree.heading("bad", text="Mauvaises")
        self.lb_tree.heading("lost", text="Points perdus")
        self.lb_tree.heading("last", text="Dernière partie")
        self.lb_tree.column("points", width=80, anchor="center")
        self.lb_tree.column("good", width=80, anchor="center")
        self.lb_tree.column("bad", width=80, anchor="center")
        self.lb_tree.column("lost", width=100, anchor="center")
        self.lb_tree.column("last", width=180, anchor="center")
        self.lb_tree.pack(padx=6, pady=6, fill="both")

        btn_frame = ttk.Frame(self.frame_leaderboard)
        btn_frame.pack(pady=(8,6))
        ttk.Button(btn_frame, text="Recharger", command=self._populate_leaderboard).grid(row=0, column=0, padx=6)
        ttk.Button(btn_frame, text="Retour", command=lambda: self._show_frame(self.frame_result)).grid(row=0, column=1, padx=6)

    def _populate_leaderboard(self):
        # refresh content
        for r in self.lb_tree.get_children():
            self.lb_tree.delete(r)
        board = load_leaderboard()
        # sort by points desc
        entries = sorted(board.items(), key=lambda x: x[1].get("total_points", 0), reverse=True)
        for player_key, data in entries:
            self.lb_tree.insert("", "end", values=(
                data.get("total_points", 0),
                data.get("total_good", 0),
                data.get("total_bad", 0),
                data.get("total_lost", 0),
                data.get("last_seen", "")
            ), text=player_key)
        # show names in leftmost column (text) by adding a label per row: Treeview doesn't show the text column when show="headings",
        # so we will also add a small label above the widget listing names for simplicity:
        # (Alternatively we could reconfigure treeview to include '#0' but keep simple for now)
        # To label players, we'll add a small list on the left:
        # Clear any previous name-list (pack_forget / recreate)
        # But to keep it concise, we will show names as Treeview 'iid' => set tags, and user can hover to see.
        # To make the player names visible, we will insert the full row as: values + include player_key at the end of values
        # For readability, replace the row to include the player name in the first column as a prefixed string
        # (We'll instead show a popup with name when double-clicked.)
        self.lb_tree.bind("<Double-1>", self._on_leaderboard_double)

    def _on_leaderboard_double(self, event):
        item = self.lb_tree.selection()
        if not item:
            return
        row = item[0]
        vals = self.lb_tree.item(row, "values")
        # We don't have the player name in values; show a simple message explaining the selected row
        messagebox.showinfo("Leaderboard", f"Ligne sélectionnée : {vals}")

    def _show_leaderboard(self):
        # rebuild to ensure fresh layout
        self._build_leaderboard()
        self._populate_leaderboard()
        self._show_frame(self.frame_leaderboard)

    # -------------------------
    # Frame switching
    # -------------------------
    def _show_frame(self, frame):
        # hide all frames and show the requested one
        for f in (self.frame_login, self.frame_quiz, self.frame_result, self.frame_leaderboard):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

# -------------------------
# Run
# -------------------------
if __name__ == "__main__":
    app = DataQuizzApp()
    app.mainloop()
