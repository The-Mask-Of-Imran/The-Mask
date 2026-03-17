import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
from api_manager import ApiManager   # ← নতুন ফাইল ইমপোর্ট

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class TheMask:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("The Mask – সেখাসেন নির্মাণের সুরক্ষা")
        self.root.geometry("980x740")

        self.api = ApiManager()          # ← সব API লজিক এখানে

        # চ্যাট
        self.chat = ctk.CTkTextbox(self.root, wrap="word", state="disabled", font=("Arial", 14))
        self.chat.pack(padx=20, pady=(20, 10), fill="both", expand=True)

        # ইনপুট
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.entry = ctk.CTkEntry(input_frame, placeholder_text="বাংলায় লিখুন...", font=("Arial", 14), height=45)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.send_message())

        send_btn = ctk.CTkButton(input_frame, text="পাঠান", width=100, height=45, command=self.send_message)
        send_btn.pack(side="right", padx=5)

        stop_btn = ctk.CTkButton(input_frame, text="⛔ প্রসেস বন্ধ", width=130, height=45, fg_color="red", command=self.stop_process)
        stop_btn.pack(side="right")

        settings_btn = ctk.CTkButton(self.root, text="⚙️ সেটিংস", width=130, height=35, command=self.open_settings)
        settings_btn.place(relx=0.96, rely=0.03, anchor="ne")

        self.add_message("✅ সব প্রোভাইডার + অটো সুইচিং চালু। সেটিংসে গিয়ে API যোগ করো।", "assistant")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def open_settings(self):
        self.api.open_settings_window(self.root)

    def send_message(self):
        text = self.entry.get().strip()
        if not text: return
        self.add_message(text, "user")
        self.entry.delete(0, "end")
        threading.Thread(target=self.process, args=(text,), daemon=True).start()

    def process(self, user_input):
        self.add_message("🔄 চিন্তা করছি...", "system")
        response = self.api.call_llm(user_input)
        self.add_message(response, "assistant")

    def stop_process(self):
        self.add_message("⛔ প্রসেস বন্ধ করা হয়েছে।", "system")

    def add_message(self, msg, who):
        self.chat.configure(state="normal")
        prefix = "তুমি: " if who == "user" else "The Mask: "
        self.chat.insert("end", f"{prefix}{msg}\n\n")
        self.chat.configure(state="disabled")
        self.chat.see("end")

    def on_closing(self):
        if messagebox.askokcancel("বন্ধ করব?", "সত্যিই বন্ধ করতে চাও?"):
            self.root.destroy()

if __name__ == "__main__":
    TheMask()