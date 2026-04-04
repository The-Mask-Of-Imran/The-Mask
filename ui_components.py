import customtkinter as ctk
import tkinter as tk
from PIL import Image

class UIComponents:
    def __init__(self, root):
        self.root = root

    def add_logo(self):
        try:
            logo_path = r"image\logo\the_mask_logo.png"
            logo = ctk.CTkImage(light_image=Image.open(logo_path), dark_image=Image.open(logo_path), size=(300, 100))
            label = ctk.CTkLabel(self.root, image=logo, text="")
            label.pack(pady=(15, 8))
            return label
        except Exception as e:
            print(f"Logo লোড করতে সমস্যা: {e}")
            return None

    def create_chat_area(self):
        chat = ctk.CTkTextbox(self.root, wrap="word", state="disabled", font=("Arial", 14), corner_radius=12)
        chat.pack(padx=25, pady=(10, 5), fill="both", expand=True)
        return chat

    def create_status_bar(self):
        status_var = tk.StringVar(value="✅ প্রস্তুত")
        status_label = ctk.CTkLabel(self.root, textvariable=status_var, font=("Consolas", 13, "bold"), text_color="#00ff88")
        status_label.pack(pady=(0, 12))
        return status_var, status_label

    def create_input_area(self, send_callback, mic_callback):
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(fill="x", padx=25, pady=(0, 20))

        entry = ctk.CTkEntry(input_frame, placeholder_text="বাংলায় লিখুন বা মাইকে ক্লিক করুন...", font=("Arial", 14), height=48, corner_radius=12)
        entry.pack(side="left", fill="x", expand=True, padx=(0, 12))
        
        mic_btn = ctk.CTkButton(input_frame, text="🎤", width=60, height=48, font=("Arial", 18), corner_radius=12, fg_color="#0066ff", command=mic_callback)
        mic_btn.pack(side="right", padx=(0, 8))
        
        send_btn = ctk.CTkButton(input_frame, text="পাঠান", width=80, height=48, font=("Arial", 14, "bold"), corner_radius=12, command=send_callback)
        send_btn.pack(side="right")

        entry.bind("<Return>", lambda e: send_callback())
        return entry, send_btn, mic_btn