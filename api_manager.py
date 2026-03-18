import openai
import google.generativeai as genai
import json
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="google.generativeai")


class ApiManager:
    def __init__(self):
        self.saved_apis = []
        self.current_index = 0
        self.load_apis()

        # ==================== প্রত্যেক প্রোভাইডারের জন্য আলাদা মডেল লিস্ট (ফ্রি ↑ → পেইড ↓) ====================
        # মডেলের প্রথম অংশ = আসল API ID (যাতে কল করার সময় এরর না হয়)
        self.models_dict = {
            "Google Gemini": [
                "gemini-2.5-flash [Text + Vision + Reasoning + Coding, Free]",
                "gemini-2.5-flash-lite [Text + Vision + Fast, Free]",
                "gemini-2.5-pro [Text + Vision + Deep Reasoning + Coding, Free with limits]",
                "gemini-3-flash-preview [Text + Vision, Free]",
                "gemini-3.1-pro-preview [Text + Vision + Image Generation + Multimodal, Paid]",
                "gemini-3.1-flash-lite-preview [Text + Vision, Paid]",
                "gemini-3.1-flash-image-preview [Text + Vision + Image Generation, Paid]"
            ],
            "OpenAI": [
                "gpt-5.4 [Text + Vision + Reasoning + Agentic, Paid]",
                "gpt-5.4-pro [Text + Vision + Advanced Reasoning + Professional Tasks, Paid]",
                "gpt-5.4-mini [Text + Vision + Fast & Cheap, Paid]",
                "dall-e-3 [Image Generation, Paid]",
                "sora [Video Generation, Paid]"
            ],
            "xAI Grok": [
                "grok-4.20-beta [Text + Reasoning + Agentic Tool Calling, Paid]",
                "grok-4.20-multi-agent-beta [Text + Function Calling + 2M Context + Multi-Agent, Paid]",
                "grok-4-fast [Text + Fast Reasoning, Paid]",
                "grok-3-mini [Text + Fast & Cheap, Paid]",
                "grok-imagine-image [Image Generation, Paid]",
                "grok-imagine-image-pro [High Quality Image Generation, Paid]",
                "grok-imagine-video [Video Generation, Paid]"
            ],
            "Anthropic Claude": [
                "claude-opus-4-6 [Text + Vision + 1M Context, Paid]",
                "claude-sonnet-4-6 [Text + Vision + Best Balance, Paid]",
                "claude-haiku-4-5-20251001 [Text + Vision + Fastest, Paid]",
                "claude-haiku-4-5 [Text + Vision + 200K Context, Paid]"
            ],
            "OpenRouter": [
                # Free A-Z
                "arcee-ai/trinity-large-preview:free [Creative writing + Storytelling + Role-play + Agentic + 131K Context, Free]",
                "arcee-ai/trinity-mini:free [Reasoning + Function calling + Multi-step agent + 131K Context, Free]",
                "cognitivecomputations/dolphin-mistral-24b-venice-edition:free [Uncensored chat + Role-play, Free]",
                "google/gemma-3-4b-it:free [Multimodal reasoning, Free]",
                "google/gemma-3-12b-it:free [Multimodal reasoning, Free]",
                "google/gemma-3-27b-it:free [Multimodal reasoning, Free]",
                "google/gemma-3n-e2b-it:free [Multimodal reasoning, Free]",
                "google/gemma-3n-e4b-it:free [Multimodal reasoning, Free]",
                "liquid/lfm-2.5-1.2b-instruct:free [Reasoning + Agentic + RAG, Free]",
                "liquid/lfm-2.5-1.2b-thinking:free [Reasoning + Agentic + RAG, Free]",
                "meta-llama/llama-3.2-3b-instruct:free [Multilingual dialogue + 128K Context, Free]",
                "meta-llama/llama-3.3-70b-instruct:free [Multilingual dialogue + 128K Context, Free]",
                "minimax/minimax-m2.5:free [Productivity + Office tasks, Free]",
                "mistralai/mistral-small-3.1-24b-instruct:free [Multimodal Text + Vision + Programming + 128K Context, Free]",
                "nvidia/nemotron-3-nano-30b-a3b:free [Agentic systems + 256K Context, Free]",
                "nvidia/nemotron-3-super-120b-a12b:free [Text MoE + 1M Context, Free]",
                "nvidia/nemotron-nano-12b-v2-vl:free [Multimodal Vision + Video + OCR + 128K Context, Free]",
                "nvidia/nemotron-nano-9b-v2:free [Reasoning + Non-reasoning tasks + 128K Context, Free]",
                "nousresearch/hermes-3-llama-3.1-405b:free [Agentic + Roleplay + Long context, Free]",
                "openai/gpt-oss-120b:free [Reasoning + Agentic + Tool use + 131K Context, Free]",
                "openai/gpt-oss-20b:free [Reasoning + Agentic + Tool use, Free]",
                "openrouter/free [Random Free Model Router – স্মার্ট সিলেক্ট, Free]",
                "openrouter/healer-alpha [Omni-modal Vision + Hearing + Action + Agentic + 262K Context, Free]",
                "openrouter/hunter-alpha [Agentic + Long-horizon planning + 1.05M Context, Free]",
                "qwen/qwen3-4b:free [Reasoning + Multilingual, Free]",
                "qwen/qwen3-next-80b-a3b-instruct:free [Reasoning + Code + Multilingual + Agentic + 262K Context, Free]",
                "stepfun/step-3.5-flash:free [Reasoning MoE + Programming + Long Context + 256K, Free]",
                "z-ai/glm-4.5-air:free [Agentic + Reasoning + Tool use + 131K Context, Free]",
                # Paid A-Z
                "aion-labs/aion-2.0 [Roleplaying storytelling, Paid]",
                "allenai/molmo-2-8b [Vision-language + Text + Image + Video, Paid]",
                "allenai/olmo-3.1-32b-instruct [Instruct chat, Paid]",
                "amazon/nova-2-lite-v1 [Multimodal reasoning + File support, Paid]",
                "anthropic/claude-haiku-4.5 [Fastest reasoning + 200K Context, Paid]",
                "anthropic/claude-opus-4.6 [Advanced coding + 1M Context, Paid]",
                "anthropic/claude-sonnet-4.6 [Best balance + Agentic coding, Paid]",
                "bytedance-seed/seed-1.6 [Multimodal agentic, Paid]",
                "bytedance-seed/seed-1.6-flash [Fast multimodal, Paid]",
                "bytedance-seed/seed-2.0-lite [Multimodal agentic + Vision, Paid]",
                "bytedance-seed/seed-2.0-mini [Fast multimodal, Paid]",
                "deepseek/deepseek-v3.2 [Reasoning + Agentic + 163K Context, Paid]",
                "google/gemini-2.5-flash-image [Image generation + Multimodal, Paid]",
                "google/gemini-3.1-flash [Fast reasoning + Multimodal, Paid]",
                "google/gemini-3.1-pro-preview [Frontier reasoning + 1M Context + Image Gen, Paid]",
                "inception/mercury-2 [Fast reasoning dLLM, Paid]",
                "liquid/lfm-2-24b-a2b [Efficient MoE, Paid]",
                "minimax/minimax-m2.1 [Coding + Agentic, Paid]",
                "minimax/minimax-m2.5 [Productivity + Office, Paid]",
                "mistralai/devstral-2512 [Agentic coding specialist, Paid]",
                "mistralai/mistral-large-2512 [Large multimodal + 262K Context, Paid]",
                "mistralai/mistral-small-2603 [Multimodal reasoning/coding/agentic, Paid]",
                "moonshotai/kimi-k2.5 [Multimodal coding + Agentic, Paid]",
                "nvidia/nemotron-3-nano-30b-a3b [Agentic MoE, Paid]",
                "openai/gpt-5.4 [Multimodal frontier + Reasoning, Paid]",
                "openai/gpt-5.4-pro [Advanced reasoning + Agentic, Paid]",
                "qwen/qwen3.5-9b [Multimodal reasoning, Paid]",
                "qwen/qwen3.5-27b [Vision-language, Paid]",
                "qwen/qwen3.5-35b-a3b [Vision-language MoE, Paid]",
                "qwen/qwen3.5-122b-a10b [Vision-language MoE, Paid]",
                "qwen/qwen3.5-397b-a17b [Large vision-language, Paid]",
                "qwen/qwen3.5-flash-02-23 [Fast vision-language, Paid]",
                "qwen/qwen3.5-plus-02-15 [Vision-language Plus, Paid]",
                "relace/relace-search [Codebase search agent, Paid]",
                "upstage/solar-pro-3 [MoE multilingual, Paid]",
                "writer/palmyra-x5 [Enterprise agents, Paid]",
                "x-ai/grok-4.20-beta [Agentic tool calling + Low hallucination, Paid]",
                "x-ai/grok-4.20-multi-agent-beta [Multi-agent + 2M Context, Paid]",
                "z-ai/glm-4.6v [Multimodal reasoning, Paid]",
                "z-ai/glm-4.7 [Programming + Reasoning, Paid]",
                "z-ai/glm-4.7-flash [Agentic coding, Paid]",
                "z-ai/glm-5 [Agentic systems, Paid]",
                "z-ai/glm-5-turbo [Agent-driven workflows, Paid]"
            ],
            "Local Ollama": [
                "llama3.1 [Local Ollama, Free]",
                "mistral [Local Ollama, Free]",
                "phi3 [Local Ollama, Free]",
                "gemma2 [Local Ollama, Free]"
            ]
        }

        # প্রত্যেক প্রোভাইডারের base_url (যাতে xAI Grok, OpenAI, Ollama সব কাজ করে)
        self.provider_config = {
            "OpenRouter": {"base_url": "https://openrouter.ai/api/v1"},
            "OpenAI": {"base_url": None},
            "xAI Grok": {"base_url": "https://api.x.ai/v1"},
            "Google Gemini": {"base_url": None},
            "Local Ollama": {"base_url": "http://localhost:11434/v1"},
            "Anthropic Claude": {"base_url": None}  # Claude-এর জন্য OpenAI client কাজ নাও করতে পারে (OpenRouter ব্যবহার করুন)
        }

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
        win.title("API ম্যানেজার – Provider + Model")
        win.geometry("820x800")
        win.lift()
        win.transient(parent)

        ctk.CTkLabel(win, text="প্রোভাইডার সিলেক্ট করো", font=("Arial", 14, "bold")).pack(pady=10)
        providers = ["OpenRouter", "OpenAI", "Google Gemini", "xAI Grok", "Anthropic Claude", "Local Ollama"]
        self.prov_var = tk.StringVar(value="OpenRouter")
        ctk.CTkOptionMenu(win, values=providers, variable=self.prov_var, width=550,
                          command=self.update_model_list).pack(pady=5)

        ctk.CTkLabel(win, text="মডেল সিলেক্ট করো (ফ্রি ↑ → পেইড ↓)", font=("Arial", 14, "bold")).pack(pady=(15,5))
        self.model_var = tk.StringVar()
        self.model_dropdown = ctk.CTkComboBox(win, variable=self.model_var, width=550)
        self.model_dropdown.pack(pady=5)

        self.update_model_list()

        ctk.CTkLabel(win, text="API Key", font=("Arial", 14, "bold")).pack(pady=(20,5))
        self.key_entry = ctk.CTkEntry(win, width=550, show="*", placeholder_text="sk-or-... বা অন্য কী")
        self.key_entry.pack(pady=5)

        ctk.CTkButton(win, text="🔍 Test & Add", fg_color="green", command=self.test_and_add).pack(pady=15)

        ctk.CTkLabel(win, text="সেভ করা API লিস্ট (🟢 Active | 🟡 Limit | 🔴 Inactive)", font=("Arial", 14, "bold")).pack(pady=10)
        self.list_frame = ctk.CTkScrollableFrame(win, height=280)
        self.list_frame.pack(fill="x", padx=20)
        self.refresh_list()

    def update_model_list(self, *args):
        provider = self.prov_var.get()
        models = self.models_dict.get(provider, ["No models available"])
        self.model_dropdown.configure(values=models)
        if models:
            self.model_var.set(models[0])

    def test_and_add(self):
        provider = self.prov_var.get()
        full_model_text = self.model_var.get()
        model = full_model_text.split(" [")[0].strip()   # আসল API ID
        key = self.key_entry.get().strip()

        if not key:
            messagebox.showerror("Error", "API Key দাও")
            return

        masked = key[:6] + "..." + key[-5:] if len(key) > 10 else key
        status = "🟢 Active"

        try:
            if provider == "Google Gemini":
                genai.configure(api_key=key)
                genai.GenerativeModel(model).generate_content("Test")
            else:
                base_url = self.provider_config.get(provider, {}).get("base_url")
                client = openai.OpenAI(api_key=key, base_url=base_url)
                client.chat.completions.create(model=model, messages=[{"role": "user", "content": "Test"}], max_tokens=10)
            status = "🟢 Active"
        except Exception as e:
            err_str = str(e).lower()
            if "rate limit" in err_str or "quota" in err_str:
                status = "🟡 Limit reached"
            else:
                status = f"🔴 {str(e)[:60]}"

        self.saved_apis.append({
            "provider": provider,
            "model": model,
            "key": key,
            "masked": masked,
            "status": status
        })
        self.save_apis()
        self.refresh_list()
        messagebox.showinfo("✅ Success", f"{provider} | {model}\n{status}")

    def delete_api(self, index):
        if messagebox.askyesno("Delete API", f"এই API ডিলিট করব?"):
            del self.saved_apis[index]
            self.save_apis()
            self.refresh_list()

    def refresh_list(self):
        for w in self.list_frame.winfo_children():
            w.destroy()

        for idx, api in enumerate(self.saved_apis):
            frame = ctk.CTkFrame(self.list_frame)
            frame.pack(fill="x", pady=4, padx=5)

            ctk.CTkLabel(frame, text=f"{api['provider']} | {api['model'][:35]}").pack(side="left", padx=5)

            masked_label = ctk.CTkLabel(frame, text=api['masked'])
            masked_label.pack(side="left", padx=15)

            # স্ট্যাটাস কালার সহ
            color = "#00FF00" if "🟢" in api['status'] else "#FFFF00" if "🟡" in api['status'] else "#FF0000"
            status_label = ctk.CTkLabel(frame, text=api['status'], text_color=color)
            status_label.pack(side="left", padx=10)

            # ডিলিট বাটন
            del_btn = ctk.CTkButton(frame, text="🗑️", width=30, fg_color="red", command=lambda i=idx: self.delete_api(i))
            del_btn.pack(side="right", padx=5)

    def call_llm(self, prompt):
        if not self.saved_apis:
            return "❌ কোনো API নেই। সেটিংসে যাও।"

        active_apis = [api for api in self.saved_apis if not api['status'].startswith("🔴")]
        if not active_apis:
            return "❌ কোনো Active API নেই। সেটিংসে গিয়ে ডিলিট/রি-টেস্ট করো।"

        for _ in range(len(self.saved_apis) * 2):
            api = self.saved_apis[self.current_index]
            if api['status'].startswith("🔴"):  # Inactive skip করবে
                self.current_index = (self.current_index + 1) % len(self.saved_apis)
                continue

            try:
                if api['provider'] == "Google Gemini":
                    genai.configure(api_key=api['key'])
                    return genai.GenerativeModel(api['model']).generate_content(prompt).text
                else:
                    base_url = self.provider_config.get(api['provider'], {}).get("base_url")
                    client = openai.OpenAI(api_key=api['key'], base_url=base_url)
                    resp = client.chat.completions.create(
                        model=api['model'],
                        messages=[{"role": "user", "content": prompt}]
                    )
                    return resp.choices[0].message.content
            except Exception as e:
                self.current_index = (self.current_index + 1) % len(self.saved_apis)

        return "❌ সব Active API চেষ্টা করা হয়েছে। (কী চেক করো বা নতুন API যোগ করো)"

if __name__ == "__main__":
    print("✅ ApiManager v4.3 FIXED – Delete button + Colored Status + Only Active APIs + Correct Model ID + Base URL for all providers")