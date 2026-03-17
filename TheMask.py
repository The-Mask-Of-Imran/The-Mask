import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import openai
import json
import os
import sqlite3
import threading
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class TheMask:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("The Mask – সেখাসেন নির্মাণের সুরক্ষা")
        self.root.geometry("960x720")

        self.api_key = ""
        self.provider = "OpenRouter"
        self.model = "anthropic/claude-sonnet-4.6"

        self.load_config()

        # চ্যাট
        self.chat = ctk.CTkTextbox(self.root, wrap="word", state="disabled", font=("Arial", 14))
        self.chat.pack(padx=20, pady=(20, 10), fill="both", expand=True)

        # ইনপুট
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.entry = ctk.CTkEntry(input_frame, placeholder_text="বাংলায় লিখুন...", font=("Arial", 14), height=45)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.send_message())

        send_btn = ctk.CTkButton(input_frame, text="পাঠান", width=120, height=45, command=self.send_message)
        send_btn.pack(side="right")

        # সেটিংস
        settings_btn = ctk.CTkButton(self.root, text="⚙️ সেটিংস", width=130, height=35, command=self.open_settings)
        settings_btn.place(relx=0.96, rely=0.03, anchor="ne")

        self.add_message("The Mask চালু হয়েছে। এখন যেকোনো প্রশ্ন করো।", "assistant")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def load_config(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.api_key = data.get("api_key", "")
                self.model = data.get("model", "anthropic/claude-sonnet-4.6")
        except:
            pass

    def save_config(self):
        data = {"api_key": self.api_key, "model": self.model}
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def open_settings(self):
        win = ctk.CTkToplevel(self.root)
        win.title("সেটিংস")
        win.geometry("580x520")
        win.lift()
        win.attributes("-topmost", True)

        ctk.CTkLabel(win, text="মডেল সিলেক্ট করো", font=("Arial", 14)).pack(pady=(20,5))
        models = ["anthropic/claude-sonnet-4.6", "anthropic/claude-opus-4.6", "google/gemini-2.0-flash", "xai/grok-2-1212"]
        self.model_var = tk.StringVar(value=self.model)
        ctk.CTkOptionMenu(win, values=models, variable=self.model_var, width=500).pack(pady=5)

        ctk.CTkLabel(win, text="API Key", font=("Arial", 14)).pack(pady=(20,5))
        key_entry = ctk.CTkEntry(win, width=500, show="*", placeholder_text="sk-or-...")
        key_entry.insert(0, self.api_key)
        key_entry.pack(pady=5)

        def save():
            self.api_key = key_entry.get().strip()
            self.model = self.model_var.get()
            self.save_config()
            win.destroy()
            self.add_message("✅ সেটিংস সেভ হয়েছে।", "system")
        ctk.CTkButton(win, text="সংরক্ষণ করুন", command=save).pack(pady=30)

    def send_message(self):
        text = self.entry.get().strip()
        if not text: return
        self.add_message(text, "user")
        self.entry.delete(0, "end")
        threading.Thread(target=self.process, args=(text,), daemon=True).start()

    def add_message(self, msg, who):
        self.chat.configure(state="normal")
        prefix = "তুমি: " if who == "user" else "The Mask: "
        self.chat.insert("end", f"{prefix}{msg}\n\n")
        self.chat.configure(state="disabled")
        self.chat.see("end")

    def process(self, user_input):
        if not self.api_key:
            self.add_message("সেটিংসে API Key দাও!", "assistant")
            return

        self.add_message("চিন্তা করছি...", "assistant")

        # নতুন thread-safe ডাটাবেস কানেকশন
        conn = sqlite3.connect("TheMask.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS conversations 
                     (id INTEGER PRIMARY KEY, user_msg TEXT, assistant_msg TEXT, time TEXT)''')
        conn.commit()

        try:
            # স্মার্ট প্রম্পট — LLM নিজে বুঝবে সিম্পল না কমপ্লেক্স
            system_prompt = """তুমি The Mask। সবসময় বাংলায় উত্তর দাও।
প্রশ্ন যদি সাধারণ হয় (পরিচয়, হ্যালো, ছোট তথ্য) তাহলে সরাসরি সুন্দর উত্তর দাও।
শুধুমাত্র বড় কাজ (সফটওয়্যার বানানো, অটোমেশন, রিসার্চ) এর জন্য সাব-টাস্কে ভাঙো + রিফ্লেক্ট করো।
এখন ব্যবহারকারীর প্রশ্ন: """

            client = openai.OpenAI(api_key=self.api_key, base_url="https://openrouter.ai/api/v1")
            resp = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": system_prompt},
                          {"role": "user", "content": user_input}],
                temperature=0.7
            )
            answer = resp.choices[0].message.content

            # ডাটাবেস সেভ (thread-safe)
            c.execute("INSERT INTO conversations (user_msg, assistant_msg, time) VALUES (?, ?, ?)",
                      (user_input, answer, datetime.now().isoformat()))
            conn.commit()

            self.add_message(answer, "assistant")

        except Exception as e:
            self.add_message(f"❌ এরর: {str(e)}", "assistant")
        finally:
            conn.close()

    def on_closing(self):
        if messagebox.askokcancel("বন্ধ করব?", "সত্যিই বন্ধ করতে চাও?"):
            self.root.destroy()

if __name__ == "__main__":
    TheMask()