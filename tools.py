import os
import subprocess
import requests
from memory_manager import MemoryManager

class ToolManager:
    def __init__(self):
        self.memory = MemoryManager()
        self.allowed_directories = [os.getcwd()]

    def route_request(self, user_input):
        text = user_input.lower().strip()
        
        big_task_keywords = ["বানাও", "তৈরি কর", "বানিয়ে দাও", "অ্যাপ", "সফটওয়্যার", 
                            "প্রজেক্ট", "টাস্ক", "কাজ", "develop", "create", "build"]
        if any(k in text for k in big_task_keywords) or len(text) > 80:
            return "BIG_TASK"
        
        memory_keywords = ["মনে রাখ", "সেভ কর", "মেমোরি", "আগের", "পূর্বের", "হিস্ট্রি", "remember"]
        if any(k in text for k in memory_keywords):
            return "MEMORY_LOOKUP"
        
        return "NORMAL_QUERY"

    def write_file(self, path, content):
        abs_path = os.path.abspath(path)
        if not any(abs_path.startswith(d) for d in self.allowed_directories):
            return "❌ Permission denied: Outside allowed directory"
        try:
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            with open(abs_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"✅ File created: {path}"
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def read_file(self, path):
        abs_path = os.path.abspath(path)
        try:
            with open(abs_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def browse_web(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            return response.text[:5000]
        except Exception as e:
            return f"❌ Web error: {str(e)}"

    def local_llm_call(self, prompt, history=None):
        return "NORMAL_QUERY"