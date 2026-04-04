import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
from datetime import datetime
from api_manager import ApiManager
import sqlite3
from tools import ToolManager
from memory_manager import MemoryManager
from voice_engine import VoiceEngine
from debug_logger import debug_logger
from local_brain import local_brain
from language_engine import language_engine
import time
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class TheMask:
    def __init__(self):
        # স্ক্রিন সাইজ চেক করে উইন্ডো সাইজ সেট করা
        screen_width = self.root.winfo_screenwidth() if hasattr(self, 'root') else 1920
        screen_height = self.root.winfo_screenheight() if hasattr(self, 'root') else 1080
        
        self.root = ctk.CTk()
        self.root.title("The Mask – ১৪+ API + ডিটেইলস লগিং")
        
        # উইন্ডো সাইজ - স্ক্রিনের 80% কিন্তু টাস্কবারের উপরে থাকবে
        win_width = min(1280, int(screen_width * 0.8))
        win_height = min(850, int(screen_height * 0.8))
        win_x = (screen_width - win_width) // 2
        win_y = (screen_height - win_height) // 2
        self.root.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")
        self.root.minsize(900, 600)  # মিনিমাম সাইজ

        self.api = ApiManager()
        self.tools = ToolManager()
        self.memory = MemoryManager()
        self.voice = VoiceEngine(self)

        # ডাটাবেস সেটআপ
        self.setup_database()

        self.chat_history = []
        self.message_logs = {}

        self.setup_ui()
        self.load_history()
        self.add_message("আসসালামু আলাইকুম! আমি **The Mask**\n🔹 ১৪+ প্রোভাইডার\n🔹 ভয়েস + API Routing\n🔹 ডিটেইলস লগিং সিস্টেম\n🔹 লোকাল ব্রেইন + ট্রান্সলেশন", "assistant")

        threading.Thread(target=self.auto_check_apis, daemon=True).start()
        self.root.mainloop()

    def change_voice(self, choice):
        result = self.voice.set_voice(choice)
        self.status_var.set(result)

    def setup_ui(self):
        self.main_container = ctk.CTkFrame(self.root)
        self.main_container.pack(fill="both", expand=True)

        self.sidebar = ctk.CTkFrame(self.main_container, width=280, corner_radius=0, fg_color="#0f0f0f")
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar, text="🎭 The Mask", font=("Arial", 28, "bold"), text_color="#00ff88").pack(pady=(40, 10))
        ctk.CTkLabel(self.sidebar, text="14+ API Provider", font=("Arial", 12), text_color="#888").pack(pady=(0, 30))

        ctk.CTkButton(self.sidebar, text="➕ New Chat", height=45, fg_color="#00aa00", command=self.new_chat).pack(pady=8, padx=25, fill="x")
        ctk.CTkButton(self.sidebar, text="⚙️ API Settings", height=45, command=self.open_settings).pack(pady=8, padx=25, fill="x")

        self.theme_var = tk.BooleanVar(value=True)
        ctk.CTkSwitch(self.sidebar, text="Dark Mode", variable=self.theme_var, command=self.toggle_theme).pack(pady=30, padx=25)

        # Voice Selector
        ctk.CTkLabel(self.sidebar, text="🎤 ভয়েস সিলেক্ট", font=("Arial", 14)).pack(pady=(20, 5))
        self.voice_var = tk.StringVar(value="পুরুষ (Pradeep)")
        ctk.CTkOptionMenu(self.sidebar, values=["পুরুষ (Pradeep)", "নারী (Tanishaa)", "সাবলীল (Nabanita)"],
                          variable=self.voice_var, command=self.change_voice, width=200).pack(pady=5)

        # Right Frame
        right_frame = ctk.CTkFrame(self.main_container)
        right_frame.pack(side="right", fill="both", expand=True)

        self.chat_display = ctk.CTkTextbox(right_frame, wrap="word", state="normal", font=("Segoe UI", 14), corner_radius=12)
        self.chat_display.pack(padx=20, pady=(20, 10), fill="both", expand=True)
        self.chat_display.configure(state="disabled")

        self.status_var = tk.StringVar(value="✅ প্রস্তুত | 52+ API Active")
        ctk.CTkLabel(right_frame, textvariable=self.status_var, font=("Consolas", 12), text_color="#00ff88").pack(pady=(0, 10))

        input_frame = ctk.CTkFrame(right_frame)
        input_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.entry = ctk.CTkEntry(input_frame, placeholder_text="বাংলায় লিখুন...", font=("Arial", 14), height=50, corner_radius=25)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.mic_btn = ctk.CTkButton(input_frame, text="🎤", width=60, height=50, fg_color="#0066ff", command=self.start_voice)
        self.mic_btn.pack(side="right", padx=(0, 8))

        self.send_btn = ctk.CTkButton(input_frame, text="📤", width=60, height=50, fg_color="#00aa00", command=self.send_message)
        self.send_btn.pack(side="right")

        self.entry.bind("<Return>", lambda e: self.send_message())

    def toggle_theme(self):
        ctk.set_appearance_mode("light" if self.theme_var.get() else "dark")

    def new_chat(self):
        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", "end")
        self.chat_display.configure(state="disabled")
        self.chat_history = []
        self.message_logs = {}
        self.add_message("✨ নতুন চ্যাট শুরু হয়েছে।", "assistant")

    def open_settings(self):
        """সেটিংস উইন্ডো - সামনে আনার জন্য"""
        self.api.open_settings_window(self.root)

    def start_voice(self):
        threading.Thread(target=self.voice.listen_and_transcribe, daemon=True).start()

    def setup_database(self):
        self.conn = sqlite3.connect("TheMask.db", check_same_thread=False)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS conversations 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      user_msg TEXT, 
                      assistant_msg TEXT, 
                      time TEXT)''')
        try:
            c.execute("ALTER TABLE conversations ADD COLUMN log_session TEXT")
        except sqlite3.OperationalError:
            pass
        self.conn.commit()

    def load_history(self):
        try:
            c = self.conn.cursor()
            c.execute("SELECT user_msg, assistant_msg, log_session FROM conversations ORDER BY id DESC LIMIT 15")
            rows = c.fetchall()
            for user, ass, log_session in rows:
                self.add_message(user, "user")
                self.add_message(ass, "assistant", log_session)
                if log_session:
                    self.message_logs[ass] = log_session
        except sqlite3.OperationalError:
            c.execute("SELECT user_msg, assistant_msg FROM conversations ORDER BY id DESC LIMIT 15")
            rows = c.fetchall()
            for user, ass in rows:
                self.add_message(user, "user")
                self.add_message(ass, "assistant")

    def save_to_db(self, user_msg, ass_msg, log_session):
        try:
            c = self.conn.cursor()
            c.execute("INSERT INTO conversations (user_msg, assistant_msg, time, log_session) VALUES (?, ?, ?, ?)",
                      (user_msg, ass_msg, datetime.now().isoformat(), log_session))
            self.conn.commit()
        except Exception as e:
            print(f"DB save error: {e}")

    def send_message(self, text=None):
        if text is None:
            text = self.entry.get().strip()
        if not text:
            return
        self.add_message(text, "user")
        self.entry.delete(0, "end")
        threading.Thread(target=self.process, args=(text,), daemon=True).start()

    def process(self, user_input):
        # নতুন সেশন শুরু
        session_id = debug_logger.start_session(user_input)
        
        try:
            # ধাপ ১: ইনপুট রেকর্ড
            debug_logger.add_step("📝 ইনপুট গ্রহণ", {"প্রশ্ন": user_input[:100]})
            
            # ধাপ ২: লোকাল ব্রেইন এনালাইসিস
            debug_logger.add_step("🧠 লোকাল ব্রেইন এনালাইসিস", {"স্ট্যাটাস": "চলছে..."})
            intent = local_brain.analyze_intent(user_input, debug_logger, session_id)
            debug_logger.add_step("✅ লোকাল ব্রেইন ফলাফল", intent)
            
            # ধাপ ৩: ট্রান্সলেশন (বাংলা → ইংরেজি) - যদি প্রয়োজন হয়
            debug_logger.add_step("🔄 ট্রান্সলেশন", {"থেকে": "বাংলা", "যাচ্ছে": "ইংরেজি"})
            english_prompt = language_engine.translate_to_english(user_input)
            debug_logger.add_step("✅ ট্রান্সলেশন সম্পূর্ণ", {"ইংরেজি": english_prompt[:100]})
            
            # ধাপ ৪: মেমোরি সার্চ
            debug_logger.add_step("🔍 মেমোরি সার্চ", {"কোয়েরি": user_input})
            memory_data = self.memory.retrieve_relevant(user_input, n_results=3)
            debug_logger.add_step("✅ মেমোরি রেজাল্ট", {"পাওয়া হয়েছে": len(memory_data) if memory_data else 0})
            
            # ধাপ ৫: API কল (ফলব্যাক সহ) - ইংরেজি প্রম্পট পাঠানো
            debug_logger.add_step("🌐 API রাউটিং শুরু", {"স্ট্যাটাস": f"{len(self.api.saved_apis)}টি API থেকে নির্বাচন"})
            response, api_info = self.api.call_llm_with_fallback(english_prompt, debug_logger, session_id)
            
            if not response or "❌" in response:
                response = "❌ কোনো API কাজ করেনি। সেটিংস চেক করুন।"
            else:
                # ধাপ ৬: উত্তর ট্রান্সলেশন (ইংরেজি → বাংলা)
                debug_logger.add_step("🔄 উত্তর ট্রান্সলেশন", {"থেকে": "ইংরেজি", "যাচ্ছে": "বাংলা"})
                bengali_response = language_engine.translate_to_bengali(response)
                debug_logger.add_step("✅ উত্তর ট্রান্সলেশন সম্পূর্ণ", {"বাংলা": bengali_response[:100]})
                response = bengali_response
            
            # ধাপ ৭: লোকাল ব্রেইন ভেরিফিকেশন
            debug_logger.add_step("🔍 লোকাল ব্রেইন ভেরিফিকেশন", {"স্ট্যাটাস": "উত্তর চেক করা হচ্ছে"})
            is_correct, reason = local_brain.verify_response(user_input, response, debug_logger, session_id)
            if not is_correct:
                debug_logger.add_step("⚠️ ভেরিফিকেশন ব্যর্থ", {"কারণ": reason})
                # এখানে রিট্রাই লজিক যোগ করা যেতে পারে
            
            # ধাপ ৮: উত্তর প্রদান
            debug_logger.add_step("📤 উত্তর প্রদান", {"উত্তরের দৈর্ঘ্য": len(response)})
            debug_logger.end_session(success=True, response=response[:200])
            
            # UI তে মেসেজ যোগ করা
            self.root.after(0, lambda: self.add_message(response, "assistant", session_id))
            self.save_to_db(user_input, response, session_id)
            
            # API ইনফো স্ট্যাটাস বার এ দেখানো
            if api_info:
                self.root.after(0, lambda: self.status_var.set(f"✅ {api_info.get('provider', '')} #{api_info.get('api_number', '?')} ব্যবহার হয়েছে"))
            else:
                self.root.after(0, lambda: self.status_var.set("✅ উত্তর প্রস্তুত"))
            
            # ভয়েস আউটপুট
            threading.Thread(target=self.voice.speak, args=(response,), daemon=True).start()
            
        except Exception as e:
            debug_logger.add_step("❌ এরর", {"এরর মেসেজ": str(e)[:100]})
            debug_logger.end_session(success=False)
            self.root.after(0, lambda: self.add_message(f"সরি, সমস্যা হয়েছে: {str(e)}", "assistant"))
            self.root.after(0, lambda: self.status_var.set(f"❌ এরর: {str(e)[:50]}"))

    def add_message(self, msg, who, log_session=None):
        msg_id = datetime.now().isoformat()
        self.chat_display.configure(state="normal")

        if who == "user":
            self.chat_display.insert("end", f"🧑 **আপনি:** {msg}\n\n", "user")
        else:
            self.chat_display.insert("end", f"🤖 **The Mask:** {msg}\n", "assistant")
            if log_session:
                self.chat_display.insert("end", f"   [🔍 ডিটেইলস দেখুন] ", ("detail", msg_id))
                self.message_logs[msg_id] = log_session
                self.chat_display.tag_config("detail", foreground="#00ccff", underline=True)
                self.chat_display.tag_bind("detail", "<Button-1>", lambda e, mid=msg_id: self.show_details(mid))
            self.chat_display.insert("end", "\n\n")

        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")

        self.chat_display.tag_config("user", foreground="#aaffaa")
        self.chat_display.tag_config("assistant", foreground="#ffffff")

    def show_details(self, msg_id):
        """ডিটেইলস বাটন ক্লিক করলে লগ দেখানো - সামনে আনার জন্য"""
        session_id = self.message_logs.get(msg_id)
        if not session_id:
            messagebox.showinfo("ডিটেইলস", "এই মেসেজের জন্য কোনো লগ পাওয়া যায়নি।")
            return
        
        log_text = debug_logger.format_for_display(session_id)
        
        # নতুন উইন্ডোতে লগ দেখানো
        detail_win = ctk.CTkToplevel(self.root)
        detail_win.title("প্রসেসিং ডিটেইলস")
        detail_win.geometry("800x600")
        detail_win.lift()
        detail_win.focus_force()
        detail_win.attributes('-topmost', True)
        detail_win.after(100, lambda: detail_win.attributes('-topmost', False))
        
        text_area = ctk.CTkTextbox(detail_win, wrap="word", font=("Consolas", 12))
        text_area.pack(fill="both", expand=True, padx=20, pady=20)
        text_area.insert("1.0", log_text)
        text_area.configure(state="disabled")

    def auto_check_apis(self):
        while True:
            time.sleep(3600)
            self.api.test_all_apis()
            active = len([a for a in self.api.saved_apis if "🟢" in a.get('status', '')])
            self.status_var.set(f"✅ প্রস্তুত | {active} Active")


if __name__ == "__main__":
    TheMask()