import openai
import warnings
import json
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime
import requests
import time
import threading

warnings.filterwarnings("ignore")


class ApiManager:
    def __init__(self):
        self.saved_apis = []
        self.api_history = []
        self.list_frame = None
        self.load_apis()
        self.load_history()

        # =========================================================
        # ১৪+ প্রোভাইডারের সম্পূর্ণ কনফিগারেশন
        # =========================================================
        self.providers = {
            "Google Gemini AI": {
                "type": "gemini",
                "base_url": None,
                "api_key_prefix": ["AIza"],
                "models": {
                    "text": ["gemini-3.1-pro", "gemini-3.1-flash", "gemini-3.1-flash-lite",
                            "gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-lite",
                            "gemini-3-flash", "gemini-1.5-pro", "gemini-1.5-flash"],
                    "image": ["imagen-3.0-generate-001", "imagen-3.0-fast"],
                    "vision": ["gemini-3.1-pro", "gemini-2.5-pro"]
                }
            },
            "OpenAI": {
                "type": "openai",
                "base_url": None,
                "api_key_prefix": ["sk-", "sk-proj-"],
                "models": {
                    "text": ["gpt-5.4", "gpt-5.4-pro", "gpt-5.4-mini", "gpt-5.4-nano",
                            "gpt-5-mini", "o3", "o3-pro", "o1", "o1-pro", "gpt-4o", "gpt-4o-mini"],
                    "image": ["dall-e-3", "dall-e-2"],
                    "vision": ["gpt-4o", "gpt-5.4"]
                }
            },
            "DeepSeek": {
                "type": "openai",
                "base_url": "https://api.deepseek.com/v1",
                "api_key_prefix": ["sk-"],
                "models": {
                    "text": ["deepseek-chat", "deepseek-reasoner", "deepseek-v3", "deepseek-r1"]
                }
            },
            "Anthropic (Claude)": {
                "type": "anthropic",
                "base_url": "https://api.anthropic.com/v1",
                "api_key_prefix": ["sk-ant-"],
                "models": {
                    "text": ["claude-opus-4.6", "claude-sonnet-4.6", "claude-haiku-4.5", "claude-3.5-sonnet"],
                    "vision": ["claude-opus-4.6", "claude-sonnet-4.6"]
                }
            },
            "xAI (Grok)": {
                "type": "openai",
                "base_url": "https://api.x.ai/v1",
                "api_key_prefix": ["xai-"],
                "models": {
                    "text": ["grok-4.20", "grok-4", "grok-3", "grok-3-mini"],
                    "vision": ["grok-4.20"]
                }
            },
            "Groq": {
                "type": "openai",
                "base_url": "https://api.groq.com/openai/v1",
                "api_key_prefix": ["gsk_"],
                "models": {
                    "text": ["llama-3.1-8b-instant", "llama-3.3-70b-versatile",
                            "llama-4-scout", "llama-4-maverick", "gemma2-9b-it", "mixtral-8x7b-32768"]
                }
            },
            "Together AI": {
                "type": "openai",
                "base_url": "https://api.together.xyz/v1",
                "api_key_prefix": ["together_", "tok_"],
                "models": {
                    "text": ["meta-llama/Llama-3.1-8B-Instruct", "meta-llama/Llama-3.1-70B-Instruct",
                            "meta-llama/Llama-3.3-70B-Instruct", "meta-llama/Llama-4-Scout-17B-Instruct",
                            "Qwen/Qwen2.5-72B-Instruct", "Qwen/Qwen3-72B-Instruct"],
                    "image": ["black-forest-labs/FLUX.1-schnell"],
                    "vision": ["meta-llama/Llama-3.2-11B-Vision-Instruct"]
                }
            },
            "Hugging Face": {
                "type": "huggingface",
                "base_url": "https://api-inference.huggingface.co/models",
                "api_key_prefix": ["hf_"],
                "models": {
                    "text": ["meta-llama/Llama-3.1-8B-Instruct", "meta-llama/Llama-3.3-70B-Instruct",
                            "Qwen/Qwen2.5-72B-Instruct", "microsoft/phi-3.5-mini-instruct"],
                    "image": ["black-forest-labs/FLUX.1-dev", "stabilityai/stable-diffusion-3.5-large"],
                    "vision": ["meta-llama/Llama-3.2-11B-Vision-Instruct"]
                }
            },
            "Stability AI": {
                "type": "stability",
                "base_url": "https://api.stability.ai/v1",
                "api_key_prefix": ["sk-"],
                "models": {
                    "image": ["stable-diffusion-3.5-large", "stable-diffusion-3.5-medium", "stable-image-core-v1-0"]
                }
            },
            "Replicate": {
                "type": "replicate",
                "base_url": "https://api.replicate.com/v1",
                "api_key_prefix": ["r8_"],
                "models": {
                    "text": ["meta/llama-3.1-70b-instruct"],
                    "image": ["black-forest-labs/flux-schnell"]
                }
            },
            "Cohere": {
                "type": "cohere",
                "base_url": "https://api.cohere.ai/v1",
                "api_key_prefix": ["comm", "cohere_"],
                "models": {
                    "text": ["command-r-plus", "command-r"]
                }
            },
            "Fireworks AI": {
                "type": "openai",
                "base_url": "https://api.fireworks.ai/inference/v1",
                "api_key_prefix": ["fw_"],
                "models": {
                    "text": ["accounts/fireworks/models/llama-v3p1-70b-instruct"]
                }
            },
            "ElevenLabs": {
                "type": "elevenlabs",
                "base_url": "https://api.elevenlabs.io/v1",
                "api_key_prefix": ["xi-", "sk_"],
                "models": {
                    "audio": ["eleven_multilingual_v2", "eleven_turbo_v2.5"]
                }
            },
            "OpenRouter": {
                "type": "openai",
                "base_url": "https://openrouter.ai/api/v1",
                "api_key_prefix": ["sk-or-"],
                "models": {
                    "text": ["openai/gpt-4o", "openai/gpt-4o-mini", "anthropic/claude-3.5-sonnet",
                            "anthropic/claude-3-opus", "google/gemini-pro-1.5", "meta-llama/llama-3.1-405b-instruct",
                            "deepseek/deepseek-chat", "qwen/qwen2.5-72b-instruct"],
                    "vision": ["openai/gpt-4o", "anthropic/claude-3.5-sonnet"]
                }
            }
        }

    def load_apis(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.saved_apis = data.get("apis", [])
            # স্ট্যাটাস রিফ্রেশ করা
            for api in self.saved_apis:
                if "🟢" not in api.get('status', '') and "🟡" not in api.get('status', ''):
                    api['status'] = "🟢 Active"  # ডিফল্ট অ্যাক্টিভ সেট করা
            self.save_apis()
        except Exception as e:
            print(f"Load error: {e}")
            self.saved_apis = []

    def save_apis(self):
        try:
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump({"apis": self.saved_apis}, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Save error: {e}")

    def load_history(self):
        try:
            with open("api_history.json", "r", encoding="utf-8") as f:
                self.api_history = json.load(f)
        except:
            self.api_history = []

    def save_history(self):
        with open("api_history.json", "w", encoding="utf-8") as f:
            json.dump(self.api_history, f, ensure_ascii=False, indent=4)

    def add_to_history(self, api_data):
        history_entry = api_data.copy()
        history_entry["history_id"] = datetime.now().isoformat()
        self.api_history.append(history_entry)
        self.save_history()

    def test_api_key(self, provider, key, model):
        """API কী টেস্ট করা - সঠিক পদ্ধতিতে"""
        if not key or len(key.strip()) < 8:
            return False, "🔴 Invalid API Key"

        config = self.providers.get(provider)
        if not config:
            return False, f"🔴 {provider} সাপোর্টেড নয়"

        if "::" in model:
            category, actual_model = model.split("::", 1)
        else:
            category, actual_model = "text", model

        try:
            if config["type"] == "openai":
                client = openai.OpenAI(api_key=key, base_url=config["base_url"], timeout=15)
                response = client.chat.completions.create(
                    model=actual_model,
                    messages=[{"role": "user", "content": "OK"}],
                    max_tokens=5,
                    timeout=10
                )
                if response.choices:
                    return True, "🟢 Active"
                return False, "🔴 No response"

            elif config["type"] == "gemini":
                try:
                    import google.generativeai as genai
                    genai.configure(api_key=key)
                    model_obj = genai.GenerativeModel(actual_model)
                    response = model_obj.generate_content("OK")
                    if response and response.text:
                        return True, "🟢 Active"
                except Exception as e:
                    if "API key" in str(e):
                        return False, "🔴 Invalid API Key"
                    return False, f"🔴 {str(e)[:40]}"

            return True, "🟢 Active"

        except openai.AuthenticationError:
            return False, "🔴 Invalid API Key"
        except openai.RateLimitError:
            return False, "🟡 Limit reached"
        except Exception as e:
            err_str = str(e).lower()
            if any(x in err_str for x in ["rate limit", "quota", "429"]):
                return False, "🟡 Limit reached"
            elif any(x in err_str for x in ["401", "unauthorized", "invalid api key", "incorrect"]):
                return False, "🔴 Invalid API Key"
            else:
                return False, f"🔴 {str(e)[:40]}"

    def call_llm_with_fallback(self, prompt, debug_logger=None, session_id=None):
        """স্মার্ট ফলব্যাক সহ API কল - সব API ট্রাই করবে"""
        
        # সিস্টেম প্রম্পট - AI কে তার নাম মনে করানোর জন্য
        system_prompt = """তুমি The Mask নামের একটি AI অ্যাসিস্ট্যান্ট।
তোমার নাম The Mask। তুমি কখনো অন্য নাম বলবে না।
তোমার নির্মাতা: The Mask Project।
তুমি সবসময় বাংলায় উত্তর দাও। উত্তর হবে সংক্ষিপ্ত, স্পষ্ট এবং বন্ধুত্বপূর্ণ।
যদি কেউ তোমার নাম জিজ্ঞেস করে, তুমি বলবে "আমার নাম The Mask" """

        full_prompt = f"{system_prompt}\n\nপ্রশ্ন: {prompt}"
        
        # সব API নেওয়া (প্রায়োরিটি অনুযায়ী সাজানো) - 🔴 বাদ দিয়ে সব ট্রাই করবে
        active_apis = [a for a in self.saved_apis if "🟢" in a.get('status', '') or "🟡" in a.get('status', '')]
        
        if not active_apis:
            # যদি কোনো API না থাকে, তাহলে সব API ট্রাই করবে
            active_apis = self.saved_apis
        
        if debug_logger and session_id:
            debug_logger.add_step(f"📊 মোট API", {"মোট": len(active_apis), "অ্যাক্টিভ": len([a for a in active_apis if "🟢" in a.get('status', '')])})
        
        # ফলব্যাক লুপ - সব API ট্রাই করবে
        for idx, api in enumerate(active_apis):
            try:
                provider = api['provider']
                key = api['key']
                model = api['model']
                
                if "::" in model:
                    _, actual_model = model.split("::", 1)
                else:
                    actual_model = model
                
                config = self.providers.get(provider)
                if not config:
                    continue
                
                if debug_logger and session_id:
                    debug_logger.add_step(f"🌐 API কল নং {idx+1}", {
                        "provider": provider,
                        "model": actual_model,
                        "api_number": idx+1,
                        "status": api.get('status', 'unknown')
                    })
                
                if config["type"] == "openai":
                    client = openai.OpenAI(api_key=key, base_url=config["base_url"], timeout=30)
                    response = client.chat.completions.create(
                        model=actual_model,
                        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
                        max_tokens=500,
                        temperature=0.5
                    )
                    result = response.choices[0].message.content
                    
                    # চেক করা উত্তর সঠিক কিনা
                    if result and len(result) > 5 and "error" not in result.lower():
                        if debug_logger and session_id:
                            debug_logger.add_step(f"✅ API সফল", {"provider": provider, "model": actual_model})
                        return result, {"provider": provider, "model": actual_model, "api_number": idx+1}
                    else:
                        if debug_logger and session_id:
                            debug_logger.add_step(f"⚠️ API খালি উত্তর", {"provider": provider})
                        continue
                
                elif config["type"] == "gemini":
                    try:
                        import google.generativeai as genai
                        genai.configure(api_key=key)
                        model_obj = genai.GenerativeModel(actual_model, system_instruction=system_prompt)
                        response = model_obj.generate_content(prompt)
                        result = response.text
                        if result and len(result) > 5:
                            if debug_logger and session_id:
                                debug_logger.add_step(f"✅ API সফল", {"provider": provider, "model": actual_model})
                            return result, {"provider": provider, "model": actual_model, "api_number": idx+1}
                    except Exception as e:
                        if debug_logger and session_id:
                            debug_logger.add_step(f"❌ API নং {idx+1} ব্যর্থ", {"provider": provider, "error": str(e)[:50]})
                        continue
                
            except Exception as e:
                if debug_logger and session_id:
                    debug_logger.add_step(f"❌ API নং {idx+1} ব্যর্থ", {
                        "provider": provider if 'provider' in dir() else 'unknown',
                        "error": str(e)[:50]
                    })
                # API স্ট্যাটাস আপডেট করা
                api['status'] = f"🔴 {str(e)[:30]}"
                self.save_apis()
                continue
        
        if debug_logger and session_id:
            debug_logger.add_step("❌ সব API ব্যর্থ", {"status": f"{len(active_apis)}টি API ট্রাই করা হয়েছে, সব ব্যর্থ"})
        
        return "❌ সব API ব্যর্থ হয়েছে। সেটিংস চেক করুন।", None

    def open_settings_window(self, parent):
        """সেটিংস উইন্ডো - সামনে আনার জন্য"""
        win = ctk.CTkToplevel(parent)
        win.title("API ম্যানেজার - ১৪+ প্রোভাইডার")
        win.geometry("1100x800")
        win.lift()  # সামনে আনা
        win.focus_force()  # ফোকাস করা
        win.attributes('-topmost', True)  # সবার উপরে রাখা
        win.after(100, lambda: win.attributes('-topmost', False))  # 100ms পর স্বাভাবিক করা

        main_frame = ctk.CTkFrame(win)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(main_frame, text="📡 প্রোভাইডার সিলেক্ট করুন", font=("Arial", 18, "bold")).pack(pady=10)
        provider_list = list(self.providers.keys())
        self.provider_var = tk.StringVar(value="Google Gemini AI")
        provider_menu = ctk.CTkOptionMenu(main_frame, values=provider_list, variable=self.provider_var, width=400,
                                          command=self.update_model_list)
        provider_menu.pack(pady=5)

        ctk.CTkLabel(main_frame, text="🎯 মডেল টাইপ", font=("Arial", 14)).pack(pady=(10, 0))
        self.type_var = tk.StringVar(value="text")
        type_frame = ctk.CTkFrame(main_frame)
        type_frame.pack(pady=5)
        for t in ["text", "image", "vision", "audio"]:
            ctk.CTkRadioButton(type_frame, text=t.upper(), variable=self.type_var, value=t,
                               command=self.update_model_list).pack(side="left", padx=8)

        ctk.CTkLabel(main_frame, text="🤖 মডেল সিলেক্ট করুন", font=("Arial", 14)).pack(pady=(10, 0))
        self.model_var = tk.StringVar()
        self.model_menu = ctk.CTkOptionMenu(main_frame, values=[], width=600)
        self.model_menu.pack(pady=5)

        ctk.CTkLabel(main_frame, text="🔑 API Key", font=("Arial", 14)).pack(pady=(10, 0))
        self.key_entry = ctk.CTkEntry(main_frame, width=650, placeholder_text="API Key দিন")
        self.key_entry.pack(pady=5)

        ctk.CTkLabel(main_frame, text="🏷️ ক্যাটাগরি ট্যাগ", font=("Arial", 14)).pack(pady=(10, 0))
        self.category_var = tk.StringVar(value="General")
        cat_frame = ctk.CTkFrame(main_frame)
        cat_frame.pack(pady=5)
        for cat in ["General", "Dev", "Pentest"]:
            ctk.CTkRadioButton(cat_frame, text=cat, variable=self.category_var, value=cat).pack(side="left", padx=15)

        btn_frame = ctk.CTkFrame(main_frame)
        btn_frame.pack(pady=15)
        ctk.CTkButton(btn_frame, text="✅ টেস্ট করে যোগ করুন", fg_color="green", command=self.add_api).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="🔄 সব টেস্ট করুন", fg_color="orange", command=self.test_all_apis).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="🗑️ Invalid গুলো মুছুন", fg_color="red", command=self.clean_invalid_apis).pack(side="left", padx=5)

        ctk.CTkLabel(main_frame, text="📋 সংরক্ষিত API লিস্ট (↑↓ প্রায়োরিটি)", font=("Arial", 16, "bold")).pack(pady=15)
        self.list_frame = ctk.CTkScrollableFrame(main_frame, height=300)
        self.list_frame.pack(fill="both", expand=True, pady=10)

        self.update_model_list()
        self.refresh_list()

    def update_model_list(self, *args):
        provider = self.provider_var.get()
        model_type = self.type_var.get()
        config = self.providers.get(provider, {})
        models = config.get("models", {}).get(model_type, [])
        if not models:
            models = config.get("models", {}).get("text", [])
        if not models:
            models = ["no-model-available"]
        display_models = [f"{model_type}::{m}" for m in models]
        self.model_menu.configure(values=display_models)
        if display_models:
            self.model_var.set(display_models[0])

    def add_api(self):
        provider = self.provider_var.get()
        model = self.model_var.get()
        key = self.key_entry.get().strip()
        category = self.category_var.get()

        if not key:
            messagebox.showerror("Error", "API Key দিন!")
            return

        success, status = self.test_api_key(provider, key, model)
        masked = key[:12] + "..." + key[-8:] if len(key) > 20 else key

        api_dict = {
            "provider": provider,
            "model": model,
            "key": key,
            "masked": masked,
            "category": category,
            "status": status,
            "date_added": datetime.now().isoformat()
        }

        self.saved_apis.append(api_dict)
        self.add_to_history(api_dict)
        self.save_apis()
        self.refresh_list()
        self.key_entry.delete(0, "end")

        if success and "🟢" in status:
            messagebox.showinfo("✅ Success", f"{provider}\n{model}\n{status}")
        else:
            messagebox.showwarning("⚠️ Failed", f"{provider}\n{model}\n{status}")

    def test_all_apis(self):
        for api in self.saved_apis:
            success, status = self.test_api_key(api['provider'], api['key'], api['model'])
            api['status'] = status
        self.save_apis()
        self.refresh_list()
        active = len([a for a in self.saved_apis if "🟢" in a.get('status', '')])
        limit = len([a for a in self.saved_apis if "🟡" in a.get('status', '')])
        invalid = len([a for a in self.saved_apis if "🔴" in a.get('status', '')])
        messagebox.showinfo("Test Complete", f"✅ Active: {active}\n🟡 Limit: {limit}\n🔴 Invalid: {invalid}\n📊 Total: {len(self.saved_apis)}")

    def clean_invalid_apis(self):
        before = len(self.saved_apis)
        self.saved_apis = [api for api in self.saved_apis if "🔴" not in api.get('status', '')]
        after = len(self.saved_apis)
        self.save_apis()
        self.refresh_list()
        messagebox.showinfo("Cleaned", f"{before - after}টি Invalid API মুছে ফেলা হয়েছে\n{after}টি API রয়ে গেছে")

    def move_up(self, idx):
        if idx > 0:
            self.saved_apis[idx], self.saved_apis[idx - 1] = self.saved_apis[idx - 1], self.saved_apis[idx]
            self.save_apis()
            self.refresh_list()

    def move_down(self, idx):
        if idx < len(self.saved_apis) - 1:
            self.saved_apis[idx], self.saved_apis[idx + 1] = self.saved_apis[idx + 1], self.saved_apis[idx]
            self.save_apis()
            self.refresh_list()

    def delete_api(self, idx):
        if messagebox.askyesno("Delete", "এই API মুছে ফেলবেন?"):
            del self.saved_apis[idx]
            self.save_apis()
            self.refresh_list()

    def refresh_list(self):
        if self.list_frame is None:
            return
        for w in self.list_frame.winfo_children():
            w.destroy()

        for idx, api in enumerate(self.saved_apis):
            frame = ctk.CTkFrame(self.list_frame)
            frame.pack(fill="x", pady=3, padx=5)

            ctk.CTkLabel(frame, text=f"{api['provider'][:22]}", width=150, anchor="w").pack(side="left", padx=5)
            model_short = api['model'].split("::")[-1][:30] if "::" in api['model'] else api['model'][:30]
            ctk.CTkLabel(frame, text=model_short, width=170, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(frame, text=api['masked'], width=130, anchor="w").pack(side="left", padx=5)

            cat_color = "#00ff00" if api.get('category') == "General" else "#ffaa00" if api.get('category') == "Dev" else "#ff4444"
            ctk.CTkLabel(frame, text=api.get('category', 'General'), width=70, text_color=cat_color).pack(side="left", padx=5)

            color = "#00ff00" if "🟢" in api['status'] else "#ffff00" if "🟡" in api['status'] else "#ff4444"
            ctk.CTkLabel(frame, text=api['status'][:25], text_color=color, width=130).pack(side="left", padx=5)

            ctk.CTkButton(frame, text="↑", width=35, command=lambda i=idx: self.move_up(i)).pack(side="right", padx=2)
            ctk.CTkButton(frame, text="↓", width=35, command=lambda i=idx: self.move_down(i)).pack(side="right", padx=2)
            ctk.CTkButton(frame, text="🗑", width=35, fg_color="red", command=lambda i=idx: self.delete_api(i)).pack(side="right", padx=2)