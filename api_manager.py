import openai
import json
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import google.generativeai as genai
import warnings

# FutureWarning suppress (google.generativeai deprecated)
warnings.filterwarnings("ignore", category=FutureWarning, module="google.generativeai")

class ApiManager:
    def __init__(self):
        self.saved_apis = []
        self.current_index = 0
        self.load_apis()

    def load_apis(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                self.saved_apis = json.load(f).get("apis", [])
        except:
            self.saved_apis = []

    def save_apis(self):
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump({"apis": self.saved_apis}, f, ensure_ascii=False, indent=4)

    def open_settings_window(self, parent):
        win = ctk.CTkToplevel(parent)
        win.title("API ম্যানেজার – Provider + Model + অটো সুইচ")
        win.geometry("820x800")
        win.lift ()
        win.transient(parent)

        ctk.CTkLabel(win, text="প্রোভাইডার সিলেক্ট করো", font=("Arial", 14, "bold")).pack(pady=10)
        providers = ["OpenRouter", "OpenAI", "Google Gemini", "xAI Grok", "Local Ollama"]
        self.prov_var = tk.StringVar(value="OpenRouter")
        ctk.CTkOptionMenu(win, values=providers, variable=self.prov_var, width=550,
                          command=self.update_model_list).pack(pady=5)

        ctk.CTkLabel(win, text="মডেল সিলেক্ট করো (ফ্রি ↑ A-Z → পেইড ↓ A-Z)", 
                     font=("Arial", 14, "bold")).pack(pady=(15,5))
        self.model_var = tk.StringVar()
        self.model_dropdown = ctk.CTkOptionMenu(win, variable=self.model_var, width=550)
        self.model_dropdown.pack(pady=5)
        self.update_model_list()

        ctk.CTkLabel(win, text="API Key", font=("Arial", 14, "bold")).pack(pady=(20,5))
        self.key_entry = ctk.CTkEntry(win, width=550, show="*", 
                                      placeholder_text="sk-or-v1-XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.key_entry.pack(pady=5)

        ctk.CTkButton(win, text="🔍 Test & Add", fg_color="green", 
                      command=self.test_and_add).pack(pady=15)

        ctk.CTkLabel(win, text="সেভ করা API লিস্ট (মাস্কড)", font=("Arial", 14, "bold")).pack(pady=10)
        self.list_frame = ctk.CTkScrollableFrame(win, height=280)
        self.list_frame.pack(fill="x", padx=20)
        self.refresh_list()

    def update_model_list(self, *args):
        provider = self.prov_var.get()
        if provider == "OpenRouter":
            models = [
                "openrouter/free [Smart Router] (free)",
                "stepfun/step-3.5-flash:free [Fast Reasoning & Coding - 196B] (free)",
                "stepfun/step-3-flash:free [Ultra Fast] (free)",
                "arcee-ai/trinity-large-preview:free [General - 70B+] (free)",
                "meta-llama/llama-3.3-70b-instruct:free [Instruction - 70B] (free)",
                "nvidia/nemotron-3-super-120b-a12b:free [Reasoning - 120B] (free)",
                "qwen/qwen3-coder-480b:free [Coding - 480B] (free)",
                "openrouter/hunter-alpha [Vision + Tools] (free)",
                "────────── PAID MODELS ──────────",
                "anthropic/claude-3.5-sonnet-20240620 [Coding + Reasoning]",
                "deepseek/deepseek-v3 [Best Coding]",
                "google/gemini-2.5-flash [Fast Multimodal]",
                "google/gemini-3.1-pro-preview [Long Context]",
                "openai/gpt-5.4-pro [Agentic Frontier]",
                "openai/gpt-4o [Multimodal]",
                "openai/o1-preview [Deep Reasoning]",
                "x-ai/grok-4.20-beta [Uncensored]",
                "x-ai/grok-4.20-multi-agent-beta [Agentic]",
                "qwen/qwen2.5-coder-32b-instruct [Coding Strong]",
                # আরও অনেক মডেল আছে (তোমার পুরো লিস্টের মতো)
            ]
            self.model_dropdown.configure(values=models)
            self.model_var.set(models[0])

        # অন্য প্রোভাইডারের লিস্ট (সংক্ষেপে)
        elif provider in ["OpenAI", "Google Gemini", "xAI Grok", "Local Ollama"]:
            self.model_dropdown.configure(values=["Default Model"])
            self.model_var.set("Default Model")

    def test_and_add(self):
        provider = self.prov_var.get()
        model = self.model_var.get().split(" [")[0].strip()
        key = self.key_entry.get().strip()

        if not key:
            messagebox.showerror("Error", "API Key দাও")
            return

        masked = key[:6] + "..." + key[-5:]
        status = "🔴 Failed"

        try:
            if provider == "Google Gemini":
                genai.configure(api_key=key)
                genai.GenerativeModel(model).generate_content("Test")
                status = "🟢 Active"
            else:
                headers = {}
                if provider == "OpenRouter":
                    headers = {
                        "HTTP-Referer": "https://themask.app",
                        "X-Title": "The Mask"
                    }

                client = openai.OpenAI(
                    api_key=key,
                    base_url="https://openrouter.ai/api/v1" if provider == "OpenRouter" else None,
                    default_headers=headers
                )
                client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": "Test"}],
                    max_tokens=10
                )
                status = "🟢 Active"

        except Exception as e:
            status = f"🔴 {str(e)[:70]}"

        self.saved_apis.append({"provider": provider, "model": model, "key": key, "masked": masked, "status": status})
        self.save_apis()
        self.refresh_list()
        messagebox.showinfo("Result", f"{provider} | {model}\n{status}")

    def delete_api(self, index):
        if messagebox.askyesno("Confirm", "এই API ডিলিট করবেন?"):
            del self.saved_apis[index]
            self.save_apis()
            self.refresh_list()

    def refresh_list(self):
        for w in self.list_frame.winfo_children():
            w.destroy()

        for i, api in enumerate(self.saved_apis):
            frame = ctk.CTkFrame(self.list_frame)
            frame.pack(fill="x", pady=4, padx=5)

            ctk.CTkLabel(frame, text=f"{api['provider']} | {api['model'][:30]}").pack(side="left", padx=5)
            ctk.CTkLabel(frame, text=api['masked']).pack(side="left", padx=15)
            ctk.CTkLabel(frame, text=api['status']).pack(side="left", padx=10)

            # Delete Button
            ctk.CTkButton(frame, text="🗑 Delete", width=70, fg_color="red", 
                          command=lambda idx=i: self.delete_api(idx)).pack(side="right", padx=5)

    def call_llm(self, prompt):
        if not self.saved_apis:
            return "❌ কোনো API নেই।"
        for _ in range(len(self.saved_apis) * 2):
            api = self.saved_apis[self.current_index]
            try:
                model = api['model']
                headers = {"HTTP-Referer": "https://themask.app", "X-Title": "The Mask"} if api['provider'] == "OpenRouter" else {}

                if api['provider'] == "Google Gemini":
                    genai.configure(api_key=api['key'])
                    return genai.GenerativeModel(model).generate_content(prompt).text
                else:
                    client = openai.OpenAI(api_key=api['key'], base_url="https://openrouter.ai/api/v1" if api['provider'] == "OpenRouter" else None, default_headers=headers)
                    resp = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
                    return resp.choices[0].message.content
            except:
                self.current_index = (self.current_index + 1) % len(self.saved_apis)
        return "❌ সব API চেষ্টা করা হয়েছে।"


if __name__ == "__main__":
    print("✅ ApiManager v4.0 loaded with Delete + Headers Fix!")