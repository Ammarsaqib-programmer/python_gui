import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  
class ModernExpertSystem(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("System Diagnostics v2.0")
        self.geometry("500x400")
        self.resizable(False, False)

        self.questions = [
            ("Does the computer turn on?", "power_on"),
            ("Is the power light on?", "power_light"),
            ("Is the fan running?", "fan_running"),
            ("Is the screen blank?", "screen_blank"),
            ("Do you hear beeping?", "beeping"),
            ("Is the system very slow?", "system_slow"),
            ("Unexpected shutdowns?", "shutdowns"),
            ("Is internet working?", "internet_working"),
            ("Is Wi-Fi connected?", "wifi_connected")
        ]
        self.current_step = 0
        self.facts = {}

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="HARDWARE DIAGNOSTIC", font=("Roboto", 24, "bold"), text_color="#3b8ed0")
        self.title_label.pack(pady=(30, 10))

        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.set(0)
        self.progress.pack(pady=10)

        self.card = ctk.CTkFrame(self, corner_radius=15, width=400, height=150)
        self.card.pack(pady=20, padx=40, fill="both", expand=True)

        self.question_label = ctk.CTkLabel(self.card, text="", font=("Roboto", 16), wraplength=350)
        self.question_label.place(relx=0.5, rely=0.4, anchor="center")

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=(0, 40))

        self.yes_btn = ctk.CTkButton(self.btn_frame, text="YES", font=("Roboto", 14, "bold"), 
                                     fg_color="#2fa572", hover_color="#106a43", width=120, height=40,
                                     command=lambda: self.process_answer(True))
        self.yes_btn.grid(row=0, column=0, padx=10)

        self.no_btn = ctk.CTkButton(self.btn_frame, text="NO", font=("Roboto", 14, "bold"), 
                                    fg_color="#ea5455", hover_color="#9e1e1e", width=120, height=40,
                                    command=lambda: self.process_answer(False))
        self.no_btn.grid(row=0, column=1, padx=10)

        self.show_question()

    def show_question(self):
        if self.current_step < len(self.questions):
            q_text, _ = self.questions[self.current_step]
            self.question_label.configure(text=q_text)
            progress_val = self.current_step / len(self.questions)
            self.progress.set(progress_val)
        else:
            self.diagnose()

    def process_answer(self, answer):
        _, key = self.questions[self.current_step]
        self.facts[key] = answer
        self.current_step += 1
        self.show_question()

    def diagnose(self):
        f = self.facts
        self.progress.set(1)
        
        if not f['power_on'] and not f['power_light'] and not f['fan_running']:
            res = "🔴 POWER SUPPLY FAILURE\nCheck cable connections or replace PSU."
        elif f['power_on'] and f['screen_blank'] and f['fan_running']:
            res = "🖥️ DISPLAY ISSUE\nCheck HDMI/DisplayPort or Monitor power."
        elif f['power_on'] and f['beeping']:
            res = "📟 RAM/POST ERROR\nReseat your RAM sticks or check BIOS codes."
        elif f['system_slow'] and f['shutdowns']:
            res = "🔥 THERMAL/MALWARE ISSUE\nClean your fans or run a virus scan."
        elif not f['internet_working'] and f['wifi_connected']:
            res = "🌐 DNS/ROUTER ISSUE\nReset router or flush your DNS cache."
        else:
            res = "🔍 UNKNOWN ISSUE\nFurther hardware inspection required."

        self.show_result_popup(res)

    def show_result_popup(self, message):
        result_window = ctk.CTkToplevel(self)
        result_window.title("Analysis Complete")
        result_window.geometry("400x200")
        result_window.attributes("-topmost", True)
        
        lbl = ctk.CTkLabel(result_window, text=message, font=("Roboto", 14), pady=20, wraplength=350)
        lbl.pack()
        
        close_btn = ctk.CTkButton(result_window, text="Exit", command=self.quit)
        close_btn.pack(pady=10)

if __name__ == "__main__":
    app = ModernExpertSystem()
    app.mainloop()
