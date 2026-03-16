import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CodingRPG(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Coding RPG")
        self.geometry("500x500")

        # Player stats
        self.level = 1
        self.xp = 0

        # UI Elements
        self.title_label = ctk.CTkLabel(self, text="🧠 Coding RPG", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.level_label = ctk.CTkLabel(self, text=f"Level: {self.level}")
        self.level_label.pack()

        self.xp_label = ctk.CTkLabel(self, text=f"XP: {self.xp}/{self.xp_needed()}")
        self.xp_label.pack()

        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.pack(pady=10)
        self.update_progress()

        # Quest entry
        self.quest_entry = ctk.CTkEntry(self, placeholder_text="Enter quest...")
        self.quest_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(self, text="Add Quest", command=self.add_quest)
        self.add_button.pack()

        # Quest list
        self.quest_frame = ctk.CTkFrame(self)
        self.quest_frame.pack(pady=20, fill="both", expand=True)

        self.quests = []

    def xp_needed(self):
        return self.level * 100

    def update_progress(self):
        self.progress.set(self.xp / self.xp_needed())

    def update_labels(self):
        self.level_label.configure(text=f"Level: {self.level}")
        self.xp_label.configure(text=f"XP: {self.xp}/{self.xp_needed()}")
        self.update_progress()

    def gain_xp(self, amount):

        self.xp += amount

        if self.xp >= self.xp_needed():
            self.xp -= self.xp_needed()
            self.level += 1

        self.update_labels()

    def add_quest(self):

        quest_text = self.quest_entry.get()

        if quest_text == "":
            return

        quest_container = ctk.CTkFrame(self.quest_frame)
        quest_container.pack(pady=5, padx=10, fill="x")

        quest_label = ctk.CTkLabel(quest_container, text=quest_text)
        quest_label.pack(side="left", padx=10)

        complete_button = ctk.CTkButton(
            quest_container,
            text="Complete (+20 XP)",
            width=120,
            command=lambda: self.complete_quest(quest_container)
        )
        complete_button.pack(side="right", padx=10)

        self.quest_entry.delete(0, "end")

    def complete_quest(self, quest_widget):

        quest_widget.destroy()
        self.gain_xp(20)


if __name__ == "__main__":
    app = CodingRPG()
    app.mainloop()